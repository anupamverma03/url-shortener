from pydantic import BaseModel

class URLCreate(BaseModel):
    original_url: str

class URLResponse(BaseModel):
    short_url: str

class URLStats(BaseModel):
    original_url: str
    clicks: int