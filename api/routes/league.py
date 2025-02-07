from fastapi import APIRouter
from models import League

router = APIRouter()


@router.post("/")
def create_league():
    pass

@router.get("/{user_id}")
def get_league(user_id):
    pass





