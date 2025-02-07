from fastapi import APIRouter
from models import User

router = APIRouter()


@router.post("/")
def create_user():
    pass

@router.get("/{user_id}")
def get_user(user_id):
    pass

@router.delete("/{user_id}")
def delete_user(user_id):
    pass




