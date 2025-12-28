"""
Pytest configuration and fixtures for Serilux tests
"""

import pytest


@pytest.fixture
def clear_registry():
    """Fixture to clear the SerializableRegistry before and after tests."""
    from serilux import SerializableRegistry

    # Clear before test
    SerializableRegistry.registry.clear()

    yield

    # Clear after test
    SerializableRegistry.registry.clear()
