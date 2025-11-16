"""
Unit tests for Edison Platform Client.
"""

import pytest
import os
from unittest.mock import Mock, patch
from edison_platform import EdisonPlatformClient, JobTypes
from edison_client import JobNames


class TestJobTypes:
    """Test JobTypes enum."""
    
    def test_job_types_values(self):
        """Test that all job types have correct values."""
        assert JobTypes.LITERATURE.value == "LITERATURE"
        assert JobTypes.ANALYSIS.value == "ANALYSIS"
        assert JobTypes.PRECEDENT.value == "PRECEDENT"
        assert JobTypes.MOLECULES.value == "MOLECULES"
    
    def test_get_description(self):
        """Test that descriptions are returned correctly."""
        desc = JobTypes.get_description(JobTypes.LITERATURE)
        assert "literature" in desc.lower()
        
        desc = JobTypes.get_description(JobTypes.ANALYSIS)
        assert "dataset" in desc.lower() or "analysis" in desc.lower()


class TestEdisonPlatformClient:
    """Test EdisonPlatformClient class."""
    
    @patch('edison_platform.client.EdisonClient')
    def test_init_with_api_key(self, mock_edison_client):
        """Test client initialization with API key."""
        mock_client_instance = Mock()
        mock_edison_client.return_value = mock_client_instance
        
        client = EdisonPlatformClient(api_key="test_key")
        assert client.api_key == "test_key"
        assert client.client is not None
        mock_edison_client.assert_called_once_with(api_key="test_key")
    
    def test_init_without_api_key_raises_error(self):
        """Test that initialization without API key raises ValueError."""
        # Clear environment variable if it exists
        old_key = os.environ.pop("EDISON_API_KEY", None)
        try:
            with pytest.raises(ValueError, match="API key is required"):
                EdisonPlatformClient()
        finally:
            # Restore environment variable
            if old_key:
                os.environ["EDISON_API_KEY"] = old_key
    
    @patch('edison_platform.client.EdisonClient')
    def test_init_with_env_variable(self, mock_edison_client):
        """Test client initialization with environment variable."""
        mock_client_instance = Mock()
        mock_edison_client.return_value = mock_client_instance
        
        with patch.dict(os.environ, {"EDISON_API_KEY": "env_test_key"}):
            client = EdisonPlatformClient()
            assert client.api_key == "env_test_key"
            mock_edison_client.assert_called_once_with(api_key="env_test_key")
    
    @patch('edison_platform.client.EdisonClient')
    def test_run_task(self, mock_edison_client):
        """Test synchronous task execution."""
        # Setup mock
        mock_client_instance = Mock()
        mock_client_instance.run_tasks_until_done.return_value = {"status": "completed"}
        mock_edison_client.return_value = mock_client_instance
        
        # Test
        client = EdisonPlatformClient(api_key="test_key")
        task_data = {"name": JobNames.LITERATURE, "query": "test query"}
        result = client.run_task(task_data)
        
        # Verify
        assert result == {"status": "completed"}
        mock_client_instance.run_tasks_until_done.assert_called_once_with(task_data)
    
    @patch('edison_platform.client.EdisonClient')
    def test_create_task(self, mock_edison_client):
        """Test task creation."""
        # Setup mock
        mock_client_instance = Mock()
        mock_client_instance.create_task.return_value = "task_123"
        mock_edison_client.return_value = mock_client_instance
        
        # Test
        client = EdisonPlatformClient(api_key="test_key")
        task_data = {"name": JobNames.PRECEDENT, "query": "test query"}
        task_id = client.create_task(task_data)
        
        # Verify
        assert task_id == "task_123"
        mock_client_instance.create_task.assert_called_once_with(task_data)
    
    @patch('edison_platform.client.EdisonClient')
    def test_get_task(self, mock_edison_client):
        """Test task retrieval."""
        # Setup mock
        mock_client_instance = Mock()
        mock_client_instance.get_task.return_value = {"status": "completed", "result": "data"}
        mock_edison_client.return_value = mock_client_instance
        
        # Test
        client = EdisonPlatformClient(api_key="test_key")
        result = client.get_task("task_123")
        
        # Verify
        assert result == {"status": "completed", "result": "data"}
        mock_client_instance.get_task.assert_called_once_with("task_123")
    
    @patch('edison_platform.client.EdisonClient')
    def test_literature_search_convenience_method(self, mock_edison_client):
        """Test literature search convenience method."""
        # Setup mock
        mock_client_instance = Mock()
        mock_client_instance.run_tasks_until_done.return_value = {"answer": "test answer"}
        mock_edison_client.return_value = mock_client_instance
        
        # Test
        client = EdisonPlatformClient(api_key="test_key")
        result = client.literature_search("test query")
        
        # Verify
        assert result == {"answer": "test answer"}
        call_args = mock_client_instance.run_tasks_until_done.call_args[0][0]
        assert call_args["name"] == JobNames.LITERATURE
        assert call_args["query"] == "test query"
    
    @patch('edison_platform.client.EdisonClient')
    def test_precedent_search_convenience_method(self, mock_edison_client):
        """Test precedent search convenience method."""
        # Setup mock
        mock_client_instance = Mock()
        mock_client_instance.run_tasks_until_done.return_value = {"result": "test result"}
        mock_edison_client.return_value = mock_client_instance
        
        # Test
        client = EdisonPlatformClient(api_key="test_key")
        result = client.precedent_search("test precedent query")
        
        # Verify
        assert result == {"result": "test result"}
        call_args = mock_client_instance.run_tasks_until_done.call_args[0][0]
        assert call_args["name"] == JobNames.PRECEDENT
        assert call_args["query"] == "test precedent query"
    
    @patch('edison_platform.client.EdisonClient')
    def test_analyze_data_convenience_method(self, mock_edison_client):
        """Test data analysis convenience method."""
        # Setup mock
        mock_client_instance = Mock()
        mock_client_instance.run_tasks_until_done.return_value = {"analysis": "complete"}
        mock_edison_client.return_value = mock_client_instance
        
        # Test
        client = EdisonPlatformClient(api_key="test_key")
        result = client.analyze_data("dataset_1", analysis_type="differential")
        
        # Verify
        assert result == {"analysis": "complete"}
        call_args = mock_client_instance.run_tasks_until_done.call_args[0][0]
        assert call_args["name"] == JobNames.ANALYSIS
        assert "Dataset: dataset_1" in call_args["query"]
        assert "analysis_type: differential" in call_args["query"]
    
    @patch('edison_platform.client.EdisonClient')
    def test_analyze_data_custom_query_and_overrides(self, mock_edison_client):
        """Ensure custom query text and overrides pass through untouched."""
        mock_client_instance = Mock()
        mock_client_instance.run_tasks_until_done.return_value = {"analysis": "ok"}
        mock_edison_client.return_value = mock_client_instance
        
        client = EdisonPlatformClient(api_key="test_key")
        result = client.analyze_data(
            query="custom analysis plan",
            task_overrides={"metadata": {"priority": "high"}}
        )
        
        assert result == {"analysis": "ok"}
        call_args = mock_client_instance.run_tasks_until_done.call_args[0][0]
        assert call_args["query"] == "custom analysis plan"
        assert call_args["metadata"] == {"priority": "high"}
    
    @patch('edison_platform.client.EdisonClient')
    def test_chemistry_task_convenience_method(self, mock_edison_client):
        """Test chemistry task convenience method."""
        # Setup mock
        mock_client_instance = Mock()
        mock_client_instance.run_tasks_until_done.return_value = {"molecule": "designed"}
        mock_edison_client.return_value = mock_client_instance
        
        # Test
        client = EdisonPlatformClient(api_key="test_key")
        result = client.chemistry_task("design molecule", target="protein_x")
        
        # Verify
        assert result == {"molecule": "designed"}
        call_args = mock_client_instance.run_tasks_until_done.call_args[0][0]
        assert call_args["name"] == JobNames.MOLECULES
        assert call_args["query"] == "design molecule"
        assert call_args["target"] == "protein_x"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
