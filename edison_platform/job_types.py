"""
Job types available in the Edison Scientific platform.
"""

from enum import Enum


class JobTypes(Enum):
    """
    Enum representing the different job types available in Edison Scientific.
    
    Attributes:
        LITERATURE: Search and generate answers based on scientific literature
        ANALYSIS: Analyze biological datasets
        PRECEDENT: Query prior scientific work
        MOLECULES: Chemistry tasks, leveraging cheminformatics tools
    """
    LITERATURE = "LITERATURE"
    ANALYSIS = "ANALYSIS"
    PRECEDENT = "PRECEDENT"
    MOLECULES = "MOLECULES"
    
    @classmethod
    def get_description(cls, job_type):
        """Get a description for a specific job type."""
        descriptions = {
            cls.LITERATURE: "Search and generate answers based on scientific literature",
            cls.ANALYSIS: "Analyze biological datasets",
            cls.PRECEDENT: "Query prior scientific work",
            cls.MOLECULES: "Chemistry tasks, leveraging cheminformatics tools"
        }
        return descriptions.get(job_type, "Unknown job type")
