from pydantic import BaseModel, EmailStr, ConfigDict
from uuid import UUID
from datetime import datetime
from typing import Optional
from admins.schema import id as admin_id

class DriverBase(BaseModel):
    id : UUID
    name: str
    email: str
    bus_number: int
    phone: int 
    admin_id: str
    created_at: datetime = datetime.now()

class DriverUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    bus_number: Optional[int] = None
    phone: Optional[int] = None
    admin_id: Optional[str] = None
    updated_at: Optional[datetime]  = None

# --- Schema for Returning Driver Data ---
class Driver(DriverBase):
    id: UUID
    
    updated_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)

class DriverDelete(Driver):
    deleted_at: Optional[datetime] = None