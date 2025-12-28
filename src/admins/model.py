from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class AdminCreate(BaseModel):
    id: UUID
    name: str
    email: str
    password: str
    created_at: datetime = datetime.now()


class AdminUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    updated_at: Optional[datetime] = None


class AdminDelete(AdminCreate):
    deleted_at: Optional[datetime] = None