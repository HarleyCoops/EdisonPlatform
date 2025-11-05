"""
Edison Platform Client

A wrapper around the edison-client library providing a clean interface
for interacting with the Edison Scientific platform.
"""

import os
import logging
from typing import Dict, Any, Optional
from edison_client import EdisonClient, JobNames


class EdisonPlatformClient:
    """
    Main client for interacting with the Edison Scientific platform.
    
    This class provides both synchronous and asynchronous methods for
    submitting and retrieving scientific research tasks.
    
    Attributes:
        api_key (str): The API key for authentication
        client (EdisonClient): The underlying Edison client instance
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Edison Platform Client.
        
        Args:
            api_key (str, optional): Edison API key. If not provided,
                will attempt to read from EDISON_API_KEY environment variable.
        
        Raises:
            ValueError: If no API key is provided or found in environment.
        """
        self.api_key = api_key or os.getenv("EDISON_API_KEY")
        
        if not self.api_key:
            raise ValueError(
                "API key is required. Provide it as an argument or set the "
                "EDISON_API_KEY environment variable."
            )
        
        self.client = EdisonClient(api_key=self.api_key)
        self.logger = logging.getLogger(__name__)
    
    def run_task(self, task_data: Dict[str, Any]) -> Any:
        """
        Run a task synchronously until completion.
        
        Args:
            task_data (dict): Task request data containing at minimum:
                - name: The job type (from JobNames enum)
                - Additional fields specific to the job type
        
        Returns:
            The task response with results.
        
        Example:
            >>> client = EdisonPlatformClient(api_key="your_key")
            >>> task = {
            ...     "name": JobNames.LITERATURE,
            ...     "query": "What are the latest treatments for diabetes?"
            ... }
            >>> response = client.run_task(task)
        """
        self.logger.info(f"Running task: {task_data.get('name', 'Unknown')}")
        try:
            response = self.client.run_tasks_until_done(task_data)
            self.logger.info("Task completed successfully")
            return response
        except Exception as e:
            self.logger.error(f"Error running task: {str(e)}")
            raise
    
    async def arun_task(self, task_data: Dict[str, Any]) -> Any:
        """
        Run a task asynchronously until completion.
        
        Args:
            task_data (dict): Task request data containing at minimum:
                - name: The job type (from JobNames enum)
                - Additional fields specific to the job type
        
        Returns:
            The task response with results.
        
        Example:
            >>> client = EdisonPlatformClient(api_key="your_key")
            >>> task = {
            ...     "name": JobNames.LITERATURE,
            ...     "query": "What are the latest treatments for diabetes?"
            ... }
            >>> response = await client.arun_task(task)
        """
        self.logger.info(f"Running async task: {task_data.get('name', 'Unknown')}")
        try:
            response = await self.client.arun_tasks_until_done(task_data)
            self.logger.info("Async task completed successfully")
            return response
        except Exception as e:
            self.logger.error(f"Error running async task: {str(e)}")
            raise
    
    def create_task(self, task_data: Dict[str, Any]) -> str:
        """
        Create and submit a task, returning the task ID.
        
        Args:
            task_data (dict): Task request data.
        
        Returns:
            str: The task ID for later retrieval.
        
        Example:
            >>> client = EdisonPlatformClient(api_key="your_key")
            >>> task = {
            ...     "name": JobNames.PRECEDENT,
            ...     "query": "Has anyone used CRISPR to cure sickle cell anemia?"
            ... }
            >>> task_id = client.create_task(task)
        """
        self.logger.info(f"Creating task: {task_data.get('name', 'Unknown')}")
        try:
            task_id = self.client.create_task(task_data)
            self.logger.info(f"Task created with ID: {task_id}")
            return task_id
        except Exception as e:
            self.logger.error(f"Error creating task: {str(e)}")
            raise
    
    async def acreate_task(self, task_data: Dict[str, Any]) -> str:
        """
        Create and submit a task asynchronously, returning the task ID.
        
        Args:
            task_data (dict): Task request data.
        
        Returns:
            str: The task ID for later retrieval.
        
        Example:
            >>> client = EdisonPlatformClient(api_key="your_key")
            >>> task = {
            ...     "name": JobNames.ANALYSIS,
            ...     "dataset": "example_dataset"
            ... }
            >>> task_id = await client.acreate_task(task)
        """
        self.logger.info(f"Creating async task: {task_data.get('name', 'Unknown')}")
        try:
            task_id = await self.client.acreate_task(task_data)
            self.logger.info(f"Async task created with ID: {task_id}")
            return task_id
        except Exception as e:
            self.logger.error(f"Error creating async task: {str(e)}")
            raise
    
    def get_task(self, task_id: str) -> Any:
        """
        Retrieve the status and results of a task by its ID.
        
        Args:
            task_id (str): The ID of the task to retrieve.
        
        Returns:
            Task status and results.
        
        Example:
            >>> client = EdisonPlatformClient(api_key="your_key")
            >>> task_id = "some_task_id"
            >>> result = client.get_task(task_id)
        """
        self.logger.info(f"Retrieving task: {task_id}")
        try:
            result = self.client.get_task(task_id)
            self.logger.info(f"Task retrieved: {task_id}")
            return result
        except Exception as e:
            self.logger.error(f"Error retrieving task {task_id}: {str(e)}")
            raise
    
    async def aget_task(self, task_id: str) -> Any:
        """
        Retrieve the status and results of a task by its ID asynchronously.
        
        Args:
            task_id (str): The ID of the task to retrieve.
        
        Returns:
            Task status and results.
        
        Example:
            >>> client = EdisonPlatformClient(api_key="your_key")
            >>> task_id = "some_task_id"
            >>> result = await client.aget_task(task_id)
        """
        self.logger.info(f"Retrieving async task: {task_id}")
        try:
            result = await self.client.aget_task(task_id)
            self.logger.info(f"Async task retrieved: {task_id}")
            return result
        except Exception as e:
            self.logger.error(f"Error retrieving async task {task_id}: {str(e)}")
            raise
    
    def literature_search(self, query: str) -> Any:
        """
        Convenience method for literature search tasks.
        
        Args:
            query (str): The scientific question to research.
        
        Returns:
            Task response with literature search results.
        
        Example:
            >>> client = EdisonPlatformClient(api_key="your_key")
            >>> result = client.literature_search(
            ...     "Which neglected diseases had a treatment developed by AI?"
            ... )
        """
        task_data = {
            "name": JobNames.LITERATURE,
            "query": query
        }
        return self.run_task(task_data)
    
    def precedent_search(self, query: str) -> Any:
        """
        Convenience method for precedent search tasks.
        
        Args:
            query (str): The query about prior scientific work.
        
        Returns:
            Task response with precedent search results.
        
        Example:
            >>> client = EdisonPlatformClient(api_key="your_key")
            >>> result = client.precedent_search(
            ...     "Has anyone used CRISPR to cure sickle cell anemia?"
            ... )
        """
        task_data = {
            "name": JobNames.PRECEDENT,
            "query": query
        }
        return self.run_task(task_data)
    
    def analyze_data(self, dataset: str, **kwargs) -> Any:
        """
        Convenience method for data analysis tasks.
        
        Args:
            dataset (str): The dataset identifier to analyze.
            **kwargs: Additional parameters specific to the analysis.
        
        Returns:
            Task response with analysis results.
        
        Example:
            >>> client = EdisonPlatformClient(api_key="your_key")
            >>> result = client.analyze_data("my_dataset", analysis_type="differential")
        """
        task_data = {
            "name": JobNames.ANALYSIS,
            "dataset": dataset,
            **kwargs
        }
        return self.run_task(task_data)
    
    def chemistry_task(self, query: str, **kwargs) -> Any:
        """
        Convenience method for chemistry/molecular tasks.
        
        Args:
            query (str): The chemistry-related query or task.
            **kwargs: Additional parameters specific to the chemistry task.
        
        Returns:
            Task response with chemistry task results.
        
        Example:
            >>> client = EdisonPlatformClient(api_key="your_key")
            >>> result = client.chemistry_task("Design a drug for target protein X")
        """
        task_data = {
            "name": JobNames.MOLECULES,
            "query": query,
            **kwargs
        }
        return self.run_task(task_data)
