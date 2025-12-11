# taranova_ttl.py
import time
import threading
from functools import wraps

def ttl_cache(ttl_seconds):
    if ttl_seconds is None:
        raise ValueError("ttl_seconds має бути числом")

    def decorator(func):
        cache = {}
        lock = threading.RLock()

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()

            with lock:
                entry = cache.get(key)
                if entry:
                    expire_at, value = entry
                    if expire_at is None or expire_at > now:
                        return value
                    del cache[key]

            result = func(*args, **kwargs)
            expire_at = None if ttl_seconds <= 0 else (now + ttl_seconds)
            with lock:
                cache[key] = (expire_at, result)
            return result

        def cache_clear():
            with lock:
                cache.clear()

        def cache_info():
            with lock:
                return {
                    "size": len(cache),
                    "items": [
                        {"key": k, "expires_at": v[0]} for k, v in cache.items()
                    ]
                }

        wrapper.cache_clear = cache_clear
        wrapper.cache_info = cache_info

        return wrapper

    return decorator
