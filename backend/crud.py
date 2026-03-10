from sqlalchemy.orm import Session
import models
from utils import generate_short_code

def create_short_url(db: Session, original_url: str):

    short_code = generate_short_code()

    db_url = models.URL(
        original_url=original_url,
        short_code=short_code
    )

    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    return db_url


def get_url(db: Session, short_code: str):

    return db.query(models.URL).filter(models.URL.short_code == short_code).first()


def increment_click(db: Session, url):

    url.clicks += 1
    db.commit()