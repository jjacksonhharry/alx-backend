#!/usr/bin/env python3
""" MRU caching module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Defines a MRU caching system
    """
    def __init__(self):
        """ Initializes the MRU cache
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # If cache is full, remove the most recently used item
                mru_key = next(reversed(self.cache_data))
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            # Move the accessed item to the end of the cache_data
            item = self.cache_data.pop(key)
            self.cache_data[key] = item
            return item
        else:
            return None
