from pydantic import BaseModel


class Dataset(BaseModel):
    name: str
    content: str