from pydantic import BaseModel


class PostAuthorize(BaseModel):
    token: str
    user: str
