from unittest.mock import MagicMock
import sys

# Mock langchain_core.tools before importing the module
mock_langchain_core = MagicMock()

def tool(fn):
    return fn

mock_langchain_core.tool = tool
sys.modules["langchain_core"] = mock_langchain_core
sys.modules["langchain_core.tools"] = mock_langchain_core

from app.tools.dashboard_sync import update_planning_dashboard

def test_update_planning_dashboard_all_args():
    daily = [{"id": "1", "title": "Daily Task", "status": "pending"}]
    weekly = [{"id": "2", "title": "Weekly Goal", "status": "in_progress"}]
    monthly = [{"id": "3", "title": "Monthly Target", "status": "completed"}]

    result = update_planning_dashboard(
        daily_items=daily,
        weekly_items=weekly,
        monthly_items=monthly
    )

    assert result["type"] == "DASHBOARD_UPDATE"
    assert result["data"]["daily"] == daily
    assert result["data"]["weekly"] == weekly
    assert result["data"]["monthly"] == monthly

def test_update_planning_dashboard_no_args():
    result = update_planning_dashboard()

    assert result["type"] == "DASHBOARD_UPDATE"
    assert result["data"]["daily"] == []
    assert result["data"]["weekly"] == []
    assert result["data"]["monthly"] == []

def test_update_planning_dashboard_partial_args():
    daily = [{"id": "1", "title": "Daily Task", "status": "pending"}]

    result = update_planning_dashboard(daily_items=daily)

    assert result["type"] == "DASHBOARD_UPDATE"
    assert result["data"]["daily"] == daily
    assert result["data"]["weekly"] == []
    assert result["data"]["monthly"] == []

def test_update_planning_dashboard_structure():
    result = update_planning_dashboard()

    assert "type" in result
    assert "data" in result
    assert "daily" in result["data"]
    assert "weekly" in result["data"]
    assert "monthly" in result["data"]
