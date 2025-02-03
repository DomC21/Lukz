"""Cache utilities for performance optimization"""
from typing import Any, Dict, Optional
from datetime import datetime, timedelta
import threading

class DataCache:
    """Thread-safe cache for financial data"""
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(DataCache, cls).__new__(cls)
                cls._instance.initialize()
            return cls._instance
    
    def initialize(self):
        """Initialize cache storage"""
        self._cache: Dict[str, Dict[str, Any]] = {}
        self._lock = threading.Lock()
    
    def get(self, key: str) -> Optional[Dict[str, Any]]:
        """Get cached data if not expired"""
        with self._lock:
            if key not in self._cache:
                return None
            
            cached = self._cache[key]
            if datetime.now() > cached["expires"]:
                del self._cache[key]
                return None
                
            return cached["data"]
    
    def set(self, key: str, data: Any, ttl_seconds: int = 300):
        """Cache data with expiration"""
        with self._lock:
            self._cache[key] = {
                "data": data,
                "expires": datetime.now() + timedelta(seconds=ttl_seconds)
            }
    
    def clear(self):
        """Clear all cached data"""
        with self._lock:
            self._cache.clear()

# Global cache instance
cache = DataCache()
