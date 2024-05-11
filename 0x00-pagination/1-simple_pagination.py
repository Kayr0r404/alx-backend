import csv
import math
from typing import List

index_range = __import__("0-simple_helper_function").index_range


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get a page"""
        assert isinstance(page, int) and isinstance(
            page_size, int
        ), "page and page_size must be integers"
        assert (
            page >= 1 and page_size >= 1
        ), "page and page_size must be positive integers"

        # Calculate index range for the specified page and page_size
        start_index, end_index = index_range(page, page_size)

        # Retrieve the dataset slice corresponding to the calculated index range
        dataset_slice = self.dataset()[start_index:end_index]

        return dataset_slice
