#!/usr/bin/env python3
"""
function named index_range that takes
two integer arguments page and page_size
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of start index and
    end index for a given page and page size.

    Args:
        page (int): The current page (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing start index and
        end index for the requested page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
