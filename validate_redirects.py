#!/usr/bin/env python3
"""
Script to validate redirects from docs.json by checking if source URLs
redirect to the expected destination URLs on localhost:3000.
"""

import json
import requests
from pathlib import Path
from typing import List, Dict
from urllib.parse import urljoin
import time


class RedirectValidator:
    def __init__(self, base_url: str = "http://localhost:3000"):
        self.base_url = base_url
        self.session = requests.Session()
        self.results = {
            "total": 0,
            "passed": 0,
            "failed": 0,
            "errors": [],
            "failed_redirects": [],
        }

    def load_docs_json(
        self,
        file_path: str = "/home/raeder/mintlify/softr-public-documentation/docs.json",
    ) -> List[Dict]:
        """Load redirects from docs.json file."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data.get("redirects", [])
        except FileNotFoundError:
            print(f"Error: docs.json not found at {file_path}")
            return []
        except json.JSONDecodeError as e:
            print(f"Error: Failed to parse docs.json: {e}")
            return []

    def check_redirect(self, source: str, destination: str) -> Dict:
        """
        Check if accessing source redirects to destination.

        Returns:
            Dict with validation result
        """
        source_url = urljoin(self.base_url, source)

        result = {
            "source": source,
            "destination": destination,
            "status": "unknown",
            "actual_redirect": None,
            "error": None,
            "status_code": None,
        }

        try:
            # Make request and follow redirects (up to 30)
            response = self.session.get(source_url, timeout=5, allow_redirects=True)
            result["status_code"] = response.status_code

            # Check if there was any redirect in the history
            if response.history:
                # Get the final URL after all redirects
                final_url = response.url
                # Extract the path from the final URL
                from urllib.parse import urlparse

                parsed = urlparse(final_url)
                actual_dest = parsed.path

                # Also check the first redirect location if available
                if response.history:
                    redirect_location = response.history[0].headers.get("location")
                    result["actual_redirect"] = redirect_location

                # Compare destinations (normalize trailing slashes)
                expected_dest = destination.rstrip("/")
                actual_dest_normalized = actual_dest.rstrip("/")

                if expected_dest == actual_dest_normalized:
                    result["status"] = "passed"
                else:
                    result["status"] = "failed"
                    result["error"] = (
                        f"Expected redirect to '{destination}' but got '{actual_dest}'"
                    )
            else:
                # No redirect occurred
                result["status"] = "failed"
                result["error"] = f"No redirect occurred. Got status {response.status_code} instead"

        except requests.exceptions.Timeout:
            result["status"] = "error"
            result["error"] = "Request timeout"
        except requests.exceptions.ConnectionError as e:
            result["status"] = "error"
            result["error"] = f"Connection error: {str(e)}"
        except requests.exceptions.RequestException as e:
            result["status"] = "error"
            result["error"] = f"Request failed: {str(e)}"

        return result

    def validate_all(self, redirects: List[Dict], delay: float = 0.5) -> Dict:
        """
        Validate all redirects.

        Args:
            redirects: List of redirect objects with 'source' and 'destination'
            delay: Delay between requests in seconds (to avoid overwhelming server)
        """
        print(f"\nValidating {len(redirects)} redirects from docs.json...")
        print("=" * 80)

        self.results["total"] = len(redirects)

        for idx, redirect in enumerate(redirects, 1):
            source = redirect.get("source")
            destination = redirect.get("destination")

            if not source or not destination:
                print(
                    f"[{idx}/{len(redirects)}] ⚠ Skipped: Missing source or destination"
                )
                continue

            print(
                f"[{idx}/{len(redirects)}] Testing: {source} → {destination}",
                end=" ... ",
            )

            result = self.check_redirect(source, destination)

            if result["status"] == "passed":
                print("✓ PASSED")
                self.results["passed"] += 1
            elif result["status"] == "failed":
                print("✗ FAILED")
                self.results["failed"] += 1
                self.results["failed_redirects"].append(result)
            else:
                print(f"⚠ ERROR: {result['error']}")
                self.results["failed"] += 1
                self.results["failed_redirects"].append(result)

            # Add delay to avoid overwhelming the server
            if idx < len(redirects):
                time.sleep(delay)

        return self.results

    def generate_report(
        self,
        output_file: str = "/home/raeder/mintlify/softr-public-documentation/redirect_validation_report.json",
    ):
        """Generate a JSON report of validation results."""
        report = {
            "summary": {
                "total_redirects": self.results["total"],
                "passed": self.results["passed"],
                "failed": self.results["failed"],
                "success_rate": f"{(self.results['passed'] / self.results['total'] * 100) if self.results['total'] > 0 else 0:.1f}%",
            },
            "failed_redirects": self.results["failed_redirects"],
        }

        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(report, f, indent=2)
            print(f"\n✓ Report saved to: {output_file}")
            return True
        except Exception as e:
            print(f"\n✗ Error writing report: {e}")
            return False

    def print_summary(self):
        """Print validation summary to console."""
        print("\n" + "=" * 80)
        print("VALIDATION SUMMARY")
        print("=" * 80)
        print(f"Total redirects:  {self.results['total']}")
        print(
            f"Passed:           {self.results['passed']} ({(self.results['passed'] / self.results['total'] * 100) if self.results['total'] > 0 else 0:.1f}%)"
        )
        print(f"Failed:           {self.results['failed']}")
        print("=" * 80)

        if self.results["failed_redirects"]:
            print("\nFAILED REDIRECTS:")
            print("-" * 80)
            for idx, result in enumerate(self.results["failed_redirects"], 1):
                print(f"\n{idx}. Source: {result['source']}")
                print(f"   Expected destination: {result['destination']}")
                print(f"   Actual redirect: {result['actual_redirect']}")
                if result["error"]:
                    print(f"   Error: {result['error']}")
                print(f"   Status code: {result['status_code']}")


def main():
    validator = RedirectValidator(base_url="http://localhost:3000")

    # Load redirects from docs.json
    redirects = validator.load_docs_json()

    if not redirects:
        print("No redirects found in docs.json")
        return

    # Validate all redirects
    validator.validate_all(redirects)

    # Print summary
    validator.print_summary()

    # Generate report
    validator.generate_report()


if __name__ == "__main__":
    main()
