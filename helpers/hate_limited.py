from time import time
from functools import wraps
from fastapi import Request, HTTPException, status

def rate_limeted(max_call: int, time_frame: int):
    '''
        **params
        max_call: maximum number of calls supported
        time_frame: waiting time for requests to be returned**
    '''
    def decorator(func):
        calls = []

        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            now = time()
            call_time_frame = [calls for call in calls if call > now - time_frame]

            if len(call_time_frame) >= max_call:
                raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail='Rate limit exceded.')
            
            calls.append(now)
            return await func(request, *args, **kwargs)
        return wrapper
    return decorator
