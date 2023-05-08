from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db

router = APIRouter()



items = ['oracle', 'python', 'java', 'c++', 'c#', 'javascript', 'php', 'ruby', 'swift', 'kotlin', 'go']



@router.get("/search")
def search( q: str):
    

    return