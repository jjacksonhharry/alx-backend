#!/usr/bin/env python3
""" LFU caching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Defines a LFU caching system
    """
    def __init__(self):
        """ Initializes the LFU cache
        """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # If cache is full, remove the least frequency used item
                min_frequency = min(self.frequency.values())
                # items = items to discard
                items = [k for k, v in self.frequency.items() if v == min_frequency]
                lru_key = min(items, key=lambda x: self.cache_data[x])
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.frequency[key] = 1

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            # Update the frequency of the accessed item
            self.frequency[key] += 1
            return self.cache_data[key]
        else:
            return None
