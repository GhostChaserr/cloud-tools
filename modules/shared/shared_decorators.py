from functools import wraps
from .shared_models import Activity
from fastapi import Request

def activity(argument):
  def decorator(func):
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
      operation = request.url.components.path.split('/')[-1]
      activity = Activity(
        path_name=request.url.components.path,
        operation=operation,
        user_agent=request.headers.get('user-agent')
      )
      activity.save()
      return await func(request, *args, **kwargs)
    return wrapper
  return decorator