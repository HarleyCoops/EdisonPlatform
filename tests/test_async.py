"""
Async tests for Edison Platform Client.
"""

import pytest
import os
from unittest.mock import Mock, patch, AsyncMock
from edison_platform import EdisonPlatformClient
from edison_client import JobNames


class TestEdisonPlatformClientAsync:
    """Test async methods of EdisonPlatformClient."""
    
    @pytest.mark.asyncio
    @patch('edison_platform.client.EdisonClient')
    async def test_arun_task(self, mock_edison_client):
        """Test asynchronous task execution."""
        # Setup mock
        mock_client_instance = Mock()
        mock_client_instance.arun_tasks_until_done = AsyncMock(
            return_value={"status": "completed"}
        )
        mock_edison_client.return_value = mock_client_instance
        
        # Test
        client = EdisonPlatformClient(api_key="test_key")
        task_data = {"name": JobNames.LITERATURE, "query": "test query"}
        result = await client.arun_task(task_data)
        
        # Verify
        assert result == {"status": "completed"}
        mock_client_instance.arun_tasks_until_done.assert_called_once_with(task_data)
    
    @pytest.mark.asyncio
    @patch('edison_platform.client.EdisonClient')
    async def test_acreate_task(self, mock_edison_client):
        """Test async task creation."""
        # Setup mock
        mock_client_instance = Mock()
        mock_client_instance.acreate_task = AsyncMock(return_value="async_task_123")
        mock_edison_client.return_value = mock_client_instance
        
        # Test
        client = EdisonPlatformClient(api_key="test_key")
        task_data = {"name": JobNames.ANALYSIS, "query": "test analysis"}
        task_id = await client.acreate_task(task_data)
        
        # Verify
        assert task_id == "async_task_123"
        mock_client_instance.acreate_task.assert_called_once_with(task_data)
    
    @pytest.mark.asyncio
    @patch('edison_platform.client.EdisonClient')
    async def test_aget_task(self, mock_edison_client):
        """Test async task retrieval."""
        # Setup mock
        mock_client_instance = Mock()
        mock_client_instance.aget_task = AsyncMock(
            return_value={"status": "completed", "result": "async data"}
        )
        mock_edison_client.return_value = mock_client_instance
        
        # Test
        client = EdisonPlatformClient(api_key="test_key")
        result = await client.aget_task("async_task_123")
        
        # Verify
        assert result == {"status": "completed", "result": "async data"}
        mock_client_instance.aget_task.assert_called_once_with("async_task_123")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
