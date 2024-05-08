#!/usr/bin/env python3
"""Basic caching module."""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """inherit from Basecache and
    redefine setter and getter methods for cache class"""

    def __init__(self):
        super().__init__()
        self.__age_bits = dict()

    def put(self, key, item):
        """add value in cache"""
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                print(f"DISCARD: {self._get_least_used()}")
                del self.cache_data[self._get_least_used()]
                del self.__age_bits[self._get_least_used()]
            self._count(key)
            self.cache_data[key] = item

    def get(self, key):
        """return value in cache"""
        if key is None or not (key in self.cache_data):
            return
        self._count(key)
        return self.cache_data[key]

    def _count(self, key):
        """count how frequent keys in cache are used"""
        if key in self.__age_bits:
            self.__age_bits[key] += 1
        else:
            self.__age_bits[key] = 1

    def _get_least_used(self):
        """retrieve least frequently used key from cache"""
        min = float("inf")
        for key, val in self.__age_bits.items():
            if val < min:
                min = val
                least_used_key = key
        return least_used_key
