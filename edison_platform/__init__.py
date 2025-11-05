"""
Edison Platform API Integration

This package provides a wrapper for the Edison Scientific API client,
making it easy to interact with the Edison platform for scientific research tasks.
"""

from .client import EdisonPlatformClient
from .job_types import JobTypes

__version__ = "0.1.0"
__all__ = ["EdisonPlatformClient", "JobTypes"]
