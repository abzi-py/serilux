"""
Pytest configuration and fixtures for Serilux tests
"""

import sys
from pathlib import Path

# Add project root to Python path so tests can import serilux
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

import pytest  # noqa: E402


@pytest.fixture
def clear_registry():
    """Fixture to clear the SerializableRegistry before and after tests."""
    from serilux import SerializableRegistry

    # Clear before test
    SerializableRegistry.registry.clear()

    yield

    # Clear after test
    SerializableRegistry.registry.clear()
