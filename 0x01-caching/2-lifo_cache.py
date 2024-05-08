#!/usr/bin/env python3
""" LIFO caching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Defines a LIFO caching system
    """
    def __init__(self):
        """ Initializes the LIFO cache
        """
        super().__init__()
        self.keys_in_order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # If cache is full, remove the last item added
                discarded_key = self.keys_in_order.pop()
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item
            self.keys_in_order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
