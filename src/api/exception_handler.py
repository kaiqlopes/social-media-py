from starlette.responses import JSONResponse

from src.domain.exceptions.user_not_found_exception import UserNotFoundError
from fastapi import Request

async def user_not_found_handler(request: Request, ex: UserNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"detail": str(ex)},
    )