from fastapi import APIRouter
from fastapi import Depends
from src.api.dependencies import get_user_service
from src.api.schemas.user_create_schema import UserCreateSchema
from src.api.schemas.user_response_schema import UserResponseSchema
from src.application.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/{user_id}", response_model=UserResponseSchema)
def get_user(user_id: int, user_service: UserService = Depends(get_user_service)):
        return user_service.get_by_id(user_id)

@router.post("/", status_code=201, response_model=UserResponseSchema)
def create_user(user: UserCreateSchema, user_service: UserService = Depends(get_user_service)):
        return user_service.create(user)
        
