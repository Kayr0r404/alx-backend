#!/usr/bin/env python3
"""task 0"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """inherit from Basecache and
    redefine setter and getter methods for cache class"""

    def put(self, key, item):
        """add value in cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """return value in cache"""
        if key is None or not (key in self.cache_data):
            return
        return self.cache_data[key]
