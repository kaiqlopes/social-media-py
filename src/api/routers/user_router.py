from fastapi import APIRouter
from fastapi import Depends
from src.api.dependencies import get_user_service
from src.api.schemas.user_schema import UserSchema
from src.application.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/{user_id}", response_model=UserSchema)
def get_user(user_id: int, service: UserService = Depends(get_user_service)):
        return service.get_user_by_id(user_id)


