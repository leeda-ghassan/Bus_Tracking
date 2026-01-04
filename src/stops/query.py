from enum import Enum
from pydantic import BaseModel, Field, EmailStr
from uuid import UUID
from datetime import datetime
from typing import Optional

class RouteCreate(BaseModel):
    id: UUID
    name: str
    description: Optional[str] = None
    # status: StatusEnum
    created_at: datetime = Field(default_factory=datetime.now)