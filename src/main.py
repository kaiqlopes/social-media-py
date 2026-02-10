from fastapi import FastAPI

from src.api.exception_handler import user_not_found_handler
from src.domain.exceptions.user_not_found_exception import UserNotFoundError
from src.api.routers.user_router import router as user_router


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(user_router)
    app.add_exception_handler(UserNotFoundError, user_not_found_handler)

    return app
