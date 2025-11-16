"""
Test script to run the basic usage query from README
"""
from edison_platform import EdisonPlatformClient

# Initialize the client (reads API key from environment)
client = EdisonPlatformClient()

# Run a literature search - the exact query from README
result = client.literature_search(
    "Which neglected diseases had a treatment developed by artificial intelligence?"
)

print("=" * 80)
print("LITERATURE SEARCH RESULTS")
print("=" * 80)
print(result)
print("=" * 80)

