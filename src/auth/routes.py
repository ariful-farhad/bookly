from datetime import timedelta

from fastapi import APIRouter, Depends, status
from typing import List
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from sqlmodel.ext.asyncio.session import AsyncSession

from src.auth.dependencies import RefreshTokenBearer
from src.auth.schemas import UserModel, UserCreateModel, UserLoginModel
from src.auth.service import AuthService
from src.db.main import get_session
from src.auth.utils import create_access_token, decode_token, verify_password

auth_router = APIRouter()
auth_service = AuthService()

REFRESH_TOKEN_EXPIRY = 2


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


@auth_router.post("/login")
async def login_user(
    login_data: UserLoginModel, session: AsyncSession = Depends(get_session)
):
    email = login_data.email
    password = login_data.password

    user = await auth_service.get_user_by_email(email, session)
    if user is not None:
        password_valid = verify_password(password, user.password_hash)
        if password_valid:
            access_token = create_access_token(
                user_data={"email": user.email, "user_uid": str(user.uid)}
            )

            refresh_token = create_access_token(
                user_data={"email": user.email, "user_uid": str(user.uid)},
                refresh=True,
                expiry=timedelta(days=REFRESH_TOKEN_EXPIRY),
            )

            return JSONResponse(
                content={
                    "message": "Login successul",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "user": {"email": user.email, "uid": str(user.uid)},
                }
            )
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, detail="Invalid email or password"
    )


@auth_router.get("/refresh_token")
async def get_new_access_token(token_details: dict = Depends(RefreshTokenBearer())):
    return {}
