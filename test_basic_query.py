"""
Test script to run the basic usage query from README
"""
import os
import sys
from dotenv import load_dotenv
from edison_platform import EdisonPlatformClient

# Load environment variables from .env file
load_dotenv()

# Initialize the client with verbose logging (reads API key from environment)
client = EdisonPlatformClient(verbose=True, show_progress=True)

# Run a literature search - the exact query from README
query = "Which neglected diseases had a treatment developed by artificial intelligence?"

print("\n" + "=" * 80)
print("EDISON PLATFORM - LITERATURE SEARCH DEMO")
print("=" * 80)
print(f"\nQuery: {query}\n")

try:
    result = client.literature_search(query)
    
    print("\n" + "=" * 80)
    print("RESULTS")
    print("=" * 80)
    print(result)
    print("=" * 80 + "\n")
    
except KeyboardInterrupt:
    print("\n\nTask interrupted by user.")
    sys.exit(1)
except Exception as e:
    print(f"\n\nError: {e}")
    sys.exit(1)

