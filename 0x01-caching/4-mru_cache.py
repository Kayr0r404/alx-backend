#!/usr/bin/env python3
"""Basic caching module."""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """inherit from Basecache and
    redefine setter and getter methods for cache class"""

    def put(self, key, item):
        """add value in cache"""
        if key and item:
            if self.MAX_ITEMS == len(self.cache_data):
                last_index = self.MAX_ITEMS - 1
                lst_key_in_cache = list(self.cache_data.keys())[last_index]
                print(f"DISCARD: {lst_key_in_cache}")
                del self.cache_data[lst_key_in_cache]
            if key in self.cache_data:
                self._move_key_to_front(key)
            self.cache_data[key] = item

    def get(self, key):
        """return value in cache"""
        if key is None or not (key in self.cache_data):
            return
        self._move_key_to_front(key)

        return self.cache_data[key]

    def _move_key_to_front(self, key):
        """move keys to the front of the dict"""
        val = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data.update({key: val})
