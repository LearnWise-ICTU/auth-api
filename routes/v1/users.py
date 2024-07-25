from fastapi import APIRouter, BackgroundTasks, status, HTTPException
from beanie.exceptions import RevisionIdWasChanged

from services.email import send_account_verification_email


router = APIRouter(
    prefix="/users",
    tags=["users"],
)

from models.user import User, CreateUser


@router.get("/", response_model=list[User])
async def read_users():
    return await User.find_all().to_list()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=User, )
async def create_user(user: CreateUser):
    try:
        user = User(**user.model_dump())
        # await user.save()

        await send_account_verification_email(user)
    except RevisionIdWasChanged:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User already exists")
    return user.model_dump()
