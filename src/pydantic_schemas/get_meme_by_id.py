from __future__ import annotations

from typing import List, Union, Dict

from pydantic import BaseModel


class GetMemeById(BaseModel):
    id: Union[int | str]
    info: Dict
    tags: List
    text: str
    updated_by: str
    url: str
