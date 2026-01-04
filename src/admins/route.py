from fastapi import APIRouter, HTTPException, Depends
from uuid import UUID
from src.admins.model import AdminCreate, Admin
from src.admins.service import UsersService
from src.admins.query import AdminQueries

router = APIRouter(prefix="/admins", tags=["Admins"])

def get_admin_service():
    return UsersService(AdminQueries())

@router.post("/", response_model=Admin)
async def register_admin(
    payload: AdminCreate, 
    service: UsersService = Depends(get_admin_service)
):
    status_code, admin_user = service.create_user(payload)
    
    if status_code == 409:
        raise HTTPException(status_code=409, detail="Admin already exists")
    if status_code == 400:
        raise HTTPException(status_code=400, detail="Could not create admin")
        
    return admin_user