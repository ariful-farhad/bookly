from fastapi import APIRouter, Depends, status
from typing import List
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from src.auth.schemas import UserModel, UserCreateModel
from src.auth.service import AuthService
from src.db.main import get_session
from src.auth.utils import create_access_token, decode_token

auth_router = APIRouter()
auth_service = AuthService()


@auth_router.post(
    "/signup", status_code=status.HTTP_201_CREATED, response_model=UserModel
)
async def create_user_account(
    user_data: UserCreateModel, session: AsyncSession = Depends(get_session)
):
    email = user_data.email

    existing_user = await auth_service.user_exists(email, session)
    if existing_user is False:
        new_user = await auth_service.create_user(user_data, session)
        return new_user
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="user already exists"
        )
