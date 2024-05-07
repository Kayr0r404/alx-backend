#!/usr/bin/env python3
"""Basic caching module."""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """inherit from Basecache and
    redefine setter and getter methods for cache class"""

    def put(self, key, item):
        """add value in cache"""
        if key and item:
            if self.MAX_ITEMS == len(self.cache_data):
                first_key_in_cache = list(self.cache_data.keys())[0]
                print(f"DISCARD: {first_key_in_cache}")
                del self.cache_data[first_key_in_cache]
            self.cache_data[key] = item

    def get(self, key):
        """return value in cache"""
        if key is None or not (key in self.cache_data):
            return
        return self.cache_data[key]
