#!/usr/bin/env python3
"""
Edison Platform API Test Suite

This script tests the Edison Platform API using credentials from the .env file.
It performs basic connectivity, authentication, and functionality tests.

Usage:
    python tests/api_test.py

Requirements:
    - requests library: pip install requests
    - python-dotenv library: pip install python-dotenv
    - .env file with API_KEY and API_BASE_URL configured

Environment Variables:
    API_KEY: Your API authentication key (required)
    API_BASE_URL: Base URL for API requests (required)
    API_TIMEOUT: Request timeout in seconds (optional, default: 30)
    API_VERIFY_SSL: Verify SSL certificates (optional, default: true)
"""

import os
import sys
from dotenv import load_dotenv

# Try to import requests, provide helpful error if not installed
try:
    import requests
except ImportError:
    print("❌ Error: 'requests' library not found")
    print("Install it with: pip install requests")
    sys.exit(1)


class APITester:
    """API testing class for Edison Platform"""
    
    def __init__(self):
        """Initialize the API tester with configuration from .env"""
        # Load environment variables from .env file
        load_dotenv()
        
        # Get required configuration
        self.api_key = os.getenv('API_KEY')
        self.base_url = os.getenv('API_BASE_URL')
        
        # Get optional configuration with defaults
        try:
            self.timeout = int(os.getenv('API_TIMEOUT', 30))
        except ValueError:
            print("⚠️  Warning: API_TIMEOUT must be an integer. Using default: 30")
            self.timeout = 30
        
        self.verify_ssl = os.getenv('API_VERIFY_SSL', 'true').lower() != 'false'
        self.verbose = os.getenv('VERBOSE', 'false').lower() == 'true'
        
        # Test results tracking
        self.tests_passed = 0
        self.tests_failed = 0
        self.test_results = []
    
    def validate_config(self):
        """Validate that required configuration is present"""
        print("\n🔍 Edison Platform API Test Suite")
        print("=" * 37)
        print("\nTesting configuration...")
        
        config_valid = True
        
        if not self.api_key:
            print("❌ API_KEY is not set in .env file")
            config_valid = False
        else:
            print("✅ API_KEY is set")
        
        if not self.base_url:
            print("❌ API_BASE_URL is not set in .env file")
            config_valid = False
        else:
            print("✅ API_BASE_URL is set")
        
        if not config_valid:
            print("\n⚠️  Please configure your .env file with required variables")
            print("See .env.example for a template")
            return False
        
        return True
    
    def get_headers(self):
        """Get request headers with authentication"""
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'User-Agent': 'EdisonPlatform-TestSuite/1.0'
        }
    
    def test_health_check(self):
        """Test 1: Health check endpoint"""
        test_name = "Health Check"
        endpoint = "/health"
        
        print(f"\nTest 1: {test_name}")
        print(f"  Endpoint: GET {endpoint}")
        
        try:
            response = requests.get(
                f"{self.base_url}{endpoint}",
                timeout=self.timeout,
                verify=self.verify_ssl
            )
            
            print(f"  Status: {response.status_code} {response.reason}")
            
            # Check if request was successful
            if response.status_code == 200:
                try:
                    data = response.json()
                    if self.verbose:
                        print(f"  Response: {data}")
                    print("  ✅ PASSED")
                    self.tests_passed += 1
                    self.test_results.append((test_name, "PASSED", None))
                    return True
                except ValueError:
                    print("  ⚠️  Response is not valid JSON")
                    print("  ✅ PASSED (with warning)")
                    self.tests_passed += 1
                    self.test_results.append((test_name, "PASSED", "Response not JSON"))
                    return True
            else:
                error_msg = f"Expected 200, got {response.status_code}"
                print(f"  ❌ FAILED: {error_msg}")
                self.tests_failed += 1
                self.test_results.append((test_name, "FAILED", error_msg))
                return False
                
        except requests.exceptions.RequestException as e:
            error_msg = f"Request failed: {str(e)}"
            print(f"  ❌ FAILED: {error_msg}")
            self.tests_failed += 1
            self.test_results.append((test_name, "FAILED", error_msg))
            return False
    
    def test_authentication(self):
        """Test 2: Authentication with API key"""
        test_name = "Authentication Test"
        endpoint = "/user"
        
        print(f"\nTest 2: {test_name}")
        print(f"  Endpoint: GET {endpoint}")
        
        try:
            response = requests.get(
                f"{self.base_url}{endpoint}",
                headers=self.get_headers(),
                timeout=self.timeout,
                verify=self.verify_ssl
            )
            
            print(f"  Status: {response.status_code} {response.reason}")
            
            # Check if authentication was successful
            if response.status_code == 200:
                try:
                    data = response.json()
                    if self.verbose:
                        print(f"  Authenticated user: {data.get('email', 'N/A')}")
                    print(f"  Authenticated successfully")
                    print("  ✅ PASSED")
                    self.tests_passed += 1
                    self.test_results.append((test_name, "PASSED", None))
                    return True
                except ValueError:
                    error_msg = "Response is not valid JSON"
                    print(f"  ❌ FAILED: {error_msg}")
                    self.tests_failed += 1
                    self.test_results.append((test_name, "FAILED", error_msg))
                    return False
            elif response.status_code == 401:
                error_msg = "Authentication failed - check your API_KEY"
                print(f"  ❌ FAILED: {error_msg}")
                self.tests_failed += 1
                self.test_results.append((test_name, "FAILED", error_msg))
                return False
            else:
                error_msg = f"Unexpected status code: {response.status_code}"
                print(f"  ❌ FAILED: {error_msg}")
                self.tests_failed += 1
                self.test_results.append((test_name, "FAILED", error_msg))
                return False
                
        except requests.exceptions.RequestException as e:
            error_msg = f"Request failed: {str(e)}"
            print(f"  ❌ FAILED: {error_msg}")
            self.tests_failed += 1
            self.test_results.append((test_name, "FAILED", error_msg))
            return False
    
    def test_list_resources(self):
        """Test 3: List resources endpoint"""
        test_name = "List Resources"
        endpoint = "/resources"
        
        print(f"\nTest 3: {test_name}")
        print(f"  Endpoint: GET {endpoint}")
        
        try:
            response = requests.get(
                f"{self.base_url}{endpoint}",
                headers=self.get_headers(),
                timeout=self.timeout,
                verify=self.verify_ssl
            )
            
            print(f"  Status: {response.status_code} {response.reason}")
            
            # Check if request was successful
            if response.status_code == 200:
                try:
                    data = response.json()
                    if self.verbose:
                        print(f"  Response: {data}")
                    # Check for expected response format (data field with array)
                    if 'data' in data:
                        print(f"  Resources retrieved successfully")
                        print("  ✅ PASSED")
                        self.tests_passed += 1
                        self.test_results.append((test_name, "PASSED", None))
                        return True
                    else:
                        error_msg = "Response missing expected 'data' field"
                        print(f"  ⚠️  {error_msg}")
                        print("  ✅ PASSED (with warning)")
                        self.tests_passed += 1
                        self.test_results.append((test_name, "PASSED", error_msg))
                        return True
                except ValueError:
                    error_msg = "Response is not valid JSON"
                    print(f"  ❌ FAILED: {error_msg}")
                    self.tests_failed += 1
                    self.test_results.append((test_name, "FAILED", error_msg))
                    return False
            elif response.status_code == 401:
                error_msg = "Authentication failed - check your API_KEY"
                print(f"  ❌ FAILED: {error_msg}")
                self.tests_failed += 1
                self.test_results.append((test_name, "FAILED", error_msg))
                return False
            else:
                error_msg = f"Unexpected status code: {response.status_code}"
                print(f"  ❌ FAILED: {error_msg}")
                self.tests_failed += 1
                self.test_results.append((test_name, "FAILED", error_msg))
                return False
                
        except requests.exceptions.RequestException as e:
            error_msg = f"Request failed: {str(e)}"
            print(f"  ❌ FAILED: {error_msg}")
            self.tests_failed += 1
            self.test_results.append((test_name, "FAILED", error_msg))
            return False
    
    def run_all_tests(self):
        """Run all API tests"""
        if not self.validate_config():
            return False
        
        print("\n🧪 Running API tests...\n")
        
        # Run all tests
        self.test_health_check()
        self.test_authentication()
        self.test_list_resources()
        
        # Print summary
        self.print_summary()
        
        return self.tests_failed == 0
    
    def print_summary(self):
        """Print test results summary"""
        print("\n" + "=" * 37)
        total_tests = self.tests_passed + self.tests_failed
        print(f"Test Results: {self.tests_passed}/{total_tests} passed")
        
        if self.tests_failed == 0:
            print("✅ All tests passed successfully!")
        else:
            print(f"❌ {self.tests_failed} test(s) failed")
            print("\nFailed tests:")
            for name, status, error in self.test_results:
                if status == "FAILED":
                    print(f"  - {name}: {error}")
        
        print("=" * 37)


def main():
    """Main entry point for the test suite"""
    tester = APITester()
    success = tester.run_all_tests()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
