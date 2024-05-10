#!/usr/bin/env python3
"""Task 0"""


def index_range(page: int, page_size: int) -> tuple:
    """returns the satrt page and end page"""
    start_page = (page - 1) * page_size
    end_page = ((page - 1) * page_size) + page_size
    return (start_page, end_page)
