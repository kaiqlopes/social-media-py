from fastapi import Request
from fastapi.responses import JSONResponse

from src.domain.exceptions.user_not_found_exception import UserNotFoundError


async def user_not_found_handler(request: Request, ex: UserNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"detail": str(ex)},
    )