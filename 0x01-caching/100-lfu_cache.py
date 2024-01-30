#!/usr/bin/python3
"""
LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system.
    """
    def __init__(self):
        """
        Initializes the object.
        """
        super().__init__()
        self.frequency = {}
        self.min_frequency = 0

    def put(self, key, item):
        """
        Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            if key not in self.cache_data:
                discard_key = None
                for k, v in self.frequency.items():
                    if v == self.min_frequency:
                        if discard_key is None or self.cache_data[k] < \
                                self.cache_data[discard_key]:
                            discard_key = k
                del self.frequency[discard_key]
                del self.cache_data[discard_key]
                print("DISCARD: {}".format(discard_key))
        if key in self.cache_data:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1
            self.min_frequency = 1
        self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item by key.
        """
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        if self.frequency[key] > self.min_frequency:
            self.min_frequency = self.frequency[key]
        return self.cache_data[key]
