"""
Edison Platform Client

A wrapper around the edison-client library providing a clean interface
for interacting with the Edison Scientific platform.
"""

import os
import logging
import sys
import time
import json
from typing import Dict, Any, Optional, Callable
from edison_client import EdisonClient, JobNames

try:
    from tqdm import tqdm
    TQDM_AVAILABLE = True
except ImportError:
    TQDM_AVAILABLE = False

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False
    # Create dummy color classes if colorama not available
    class Fore:
        GREEN = YELLOW = BLUE = CYAN = RED = MAGENTA = RESET = ""
    class Style:
        BRIGHT = RESET_ALL = ""


class EdisonPlatformClient:
    """
    Main client for interacting with the Edison Scientific platform.
    
    This class provides both synchronous and asynchronous methods for
    submitting and retrieving scientific research tasks.
    
    Attributes:
        api_key (str): The API key for authentication
        client (EdisonClient): The underlying Edison client instance
    """
    
    def __init__(self, api_key: Optional[str] = None, verbose: bool = True, show_progress: bool = True):
        """
        Initialize the Edison Platform Client.
        
        Args:
            api_key (str, optional): Edison API key. If not provided,
                will attempt to read from EDISON_API_KEY environment variable.
            verbose (bool): Enable verbose terminal output (default: True)
            show_progress (bool): Show progress indicators during task execution (default: True)
        
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
        self.verbose = verbose
        self.show_progress = show_progress
        
        # Configure logging to show INFO level if verbose
        if self.verbose:
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%H:%M:%S'
            )
    
    def _log_status(self, message: str, status: str = "info"):
        """Log a status message with optional color formatting."""
        if not self.verbose:
            return
            
        color_map = {
            "info": Fore.CYAN if COLORAMA_AVAILABLE else "",
            "success": Fore.GREEN if COLORAMA_AVAILABLE else "",
            "warning": Fore.YELLOW if COLORAMA_AVAILABLE else "",
            "error": Fore.RED if COLORAMA_AVAILABLE else "",
            "progress": Fore.BLUE if COLORAMA_AVAILABLE else "",
        }
        
        color = color_map.get(status, "")
        reset = Style.RESET_ALL if COLORAMA_AVAILABLE else ""
        
        timestamp = time.strftime("%H:%M:%S")
        print(f"{color}[{timestamp}] {message}{reset}", file=sys.stderr)
        sys.stderr.flush()
    
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
        job_name = task_data.get('name', 'Unknown')
        query = task_data.get('query', 'N/A')
        
        self._log_status(f"Starting {job_name} task...", "info")
        if query != 'N/A':
            self._log_status(f"Query: {query[:100]}{'...' if len(query) > 100 else ''}", "info")
        
        self.logger.info(f"Running task: {job_name}")
        
        try:
            # Create a progress indicator
            if self.show_progress and TQDM_AVAILABLE:
                with tqdm(
                    desc=f"Processing {job_name}",
                    unit="step",
                    bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]",
                    file=sys.stderr
                ) as pbar:
                    # Note: This is a placeholder - actual progress would need
                    # to be tracked from the underlying client if it supports callbacks
                    self._log_status("Task submitted, waiting for completion...", "progress")
                    
                    response = self.client.run_tasks_until_done(task_data)
                    
                    pbar.update(100)
                    pbar.set_description(f"{job_name} completed")
            else:
                self._log_status("Task submitted, waiting for completion...", "progress")
                response = self.client.run_tasks_until_done(task_data)
            
            self._log_status(f"{job_name} task completed successfully!", "success")
            self.logger.info("Task completed successfully")
            return response
        except Exception as e:
            self._log_status(f"Error running task: {str(e)}", "error")
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
        if self.verbose:
            self._log_status("=" * 60, "info")
            self._log_status("LITERATURE SEARCH", "info")
            self._log_status("=" * 60, "info")
            self._log_status(f"Researching: {query}", "info")
            self._log_status("This may take several minutes as Kosmos reads papers and analyzes data...", "progress")
        
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
        if self.verbose:
            self._log_status("=" * 60, "info")
            self._log_status("PRECEDENT SEARCH", "info")
            self._log_status("=" * 60, "info")
            self._log_status(f"Searching for: {query}", "info")
        
        task_data = {
            "name": JobNames.PRECEDENT,
            "query": query
        }
        return self.run_task(task_data)
    
    def analyze_data(self, dataset: Optional[str] = None, **kwargs) -> Any:
        """
        Convenience method for data analysis tasks.
        
        Args:
            dataset (str, optional): Identifier for the dataset to analyze.
            **kwargs: Additional context for the analysis. Use ``query`` to
                supply a fully-formed prompt or ``task_overrides`` to pass extra
                TaskRequest fields (e.g., ``metadata``).
        
        Returns:
            Task response with analysis results.
        
        Example:
            >>> client = EdisonPlatformClient(api_key="your_key")
            >>> result = client.analyze_data("my_dataset", analysis_type="differential")
        """
        params_for_prompt = dict(kwargs)
        custom_query = params_for_prompt.pop("query", None)
        task_overrides = params_for_prompt.pop("task_overrides", None) or {}
        
        if self.verbose:
            self._log_status("=" * 60, "info")
            self._log_status("DATA ANALYSIS", "info")
            self._log_status("=" * 60, "info")
            self._log_status(f"Analyzing dataset: {dataset}", "info")
            if params_for_prompt:
                self._log_status(f"Parameters: {params_for_prompt}", "info")
        
        if custom_query:
            query = custom_query
        else:
            parts = []
            if dataset:
                parts.append(f"Dataset: {dataset}")
            if params_for_prompt:
                parts.append("Parameters:")
                for key, value in params_for_prompt.items():
                    if isinstance(value, (dict, list)):
                        value_str = json.dumps(value, indent=2, sort_keys=True)
                    else:
                        value_str = str(value)
                    parts.append(f"- {key}: {value_str}")
            query = "\n".join(parts).strip()
        
        if not query:
            raise ValueError(
                "Analysis requests require at least a dataset or a query string."
            )
        
        task_data = {
            "name": JobNames.ANALYSIS,
            "query": query
        }
        
        if task_overrides:
            task_data.update(task_overrides)
        
        return self.run_task(task_data)
    
    def chemistry_task(self, query: str, **kwargs) -> Any:
        """
        Convenience method for chemistry/molecular tasks.
        
        Args:
            query (str): The chemistry-related query or task.
            **kwargs: Additional context for the chemistry task. Use ``task_overrides``
                to inject raw TaskRequest fields (e.g., ``metadata``).
        
        Returns:
            Task response with chemistry task results.
        
        Example:
            >>> client = EdisonPlatformClient(api_key="your_key")
            >>> result = client.chemistry_task("Design a drug for target protein X")
        """
        params_for_prompt = dict(kwargs)
        task_overrides = params_for_prompt.pop("task_overrides", None) or {}
        
        if self.verbose:
            self._log_status("=" * 60, "info")
            self._log_status("CHEMISTRY TASK", "info")
            self._log_status("=" * 60, "info")
            self._log_status(f"Task: {query}", "info")
            if params_for_prompt:
                self._log_status(f"Parameters: {params_for_prompt}", "info")
        
        prompt = query.strip()
        if params_for_prompt:
            extra_lines = ["Parameters:"]
            for key, value in params_for_prompt.items():
                if isinstance(value, (dict, list)):
                    value_str = json.dumps(value, indent=2, sort_keys=True)
                else:
                    value_str = str(value)
                extra_lines.append(f"- {key}: {value_str}")
            prompt = f"{prompt}\n\n" + "\n".join(extra_lines)
        
        task_data = {
            "name": JobNames.MOLECULES,
            "query": prompt
        }
        if task_overrides:
            task_data.update(task_overrides)
        return self.run_task(task_data)
