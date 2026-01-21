"""Shared fixtures for recommendations tests."""

import pytest

from trakt_mcp_server.client.recommendations import RecommendationsClient
from trakt_mcp_server.models.auth import TraktAuthToken


@pytest.fixture
def authenticated_client(mock_auth_token: TraktAuthToken) -> RecommendationsClient:
    """Create an authenticated recommendations client for testing."""
    client = RecommendationsClient()
    client.auth_token = mock_auth_token
    return client
