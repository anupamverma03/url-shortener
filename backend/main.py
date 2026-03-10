from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import models
import schemas
import crud
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/shorten", response_model=schemas.URLResponse)
def shorten_url(url: schemas.URLCreate, db: Session = Depends(get_db)):

    db_url = crud.create_short_url(db, url.original_url)

    short_link = f"http://localhost:8000/{db_url.short_code}"

    return {"short_url": short_link}


@app.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):

    db_url = crud.get_url(db, short_code)

    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")

    crud.increment_click(db, db_url)

    return RedirectResponse(db_url.original_url)


@app.get("/stats/{short_code}", response_model=schemas.URLStats)
def url_stats(short_code: str, db: Session = Depends(get_db)):

    db_url = crud.get_url(db, short_code)

    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")

    return {
        "original_url": db_url.original_url,
        "clicks": db_url.clicks
    }