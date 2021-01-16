from fastapi import Request


async def image_middleware(self, request, call_next):
  response = await call_next(request)
  response.headers['Custom'] = 'Example'
  return response