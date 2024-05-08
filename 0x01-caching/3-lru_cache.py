#!/usr/bin/env python3
""" LRU caching module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Defines a LRU caching system
    """
    def __init__(self):
        """ Initializes the LRU cache
        """
        super().__init__()
        self.keys_in_order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # If cache is full, remove the least recently used item
                lru_key = self.keys_in_order.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)
            elif key in self.cache_data:
                # If the key is already present, remove it from the order list
                self.keys_in_order.remove(key)
            self.cache_data[key] = item
            self.keys_in_order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            # If the key exists, update its position in the order list
            self.keys_in_order.remove(key)
            self.keys_in_order.append(key)
            return self.cache_data[key]
        else:
            return None
