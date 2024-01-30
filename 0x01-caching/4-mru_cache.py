#!/usr/bin/python3
"""
MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initialize the MRUCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache using MRU algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Discard the most recently used item (MRU)
                mru_key = self.order.pop()
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)

            self.cache_data[key] = item
            # Update the order to indicate recent use
            self.order.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None and key in self.cache_data:
            # Update the order to indicate recent use
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
