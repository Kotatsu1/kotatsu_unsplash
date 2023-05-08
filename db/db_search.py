from sqlalchemy.orm import Session
from db.models import DbUserCart, DbItem



def get_items(db: Session, user_id: int):
    items = db.query(DbItem).join(DbUserCart).filter(DbUserCart.user_id == user_id).all()
    return items
