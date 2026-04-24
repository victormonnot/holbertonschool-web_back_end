#!/usr/bin/env python3
"""Simple helper function for pagination."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of start and end index for pagination.

    Args:
        page: the current page number (1-indexed).
        page_size: the number of items per page.

    Returns:
        A tuple (start_index, end_index).
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
