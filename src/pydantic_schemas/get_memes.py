from __future__ import annotations

from typing import Dict, List, Union

from pydantic import BaseModel


class Datum(BaseModel):
    id: Union[int, str]
    info: Dict
    tags: List
    text: str
    updated_by: str
    url: str


class GetMemes(BaseModel):
    data: List[Datum]
