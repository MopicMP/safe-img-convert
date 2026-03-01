"""Tests for safe-img-convert."""

import pytest
from safe_img_convert import convert


class TestConvert:
    """Test suite for convert."""

    def test_basic(self):
        """Test basic usage."""
        result = convert("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            convert("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = convert(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
