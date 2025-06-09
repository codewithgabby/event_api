from fastapi import APIRouter, HTTPException
from schemas.user_schema import User, UserResponse
from services import user_service

router = APIRouter()

# Create a new user
@router.post("/users", response_model=UserResponse)
def create_user(user: User):
    return user_service.create_user(user)

# Get list of all users
@router.get("/users", response_model=list[UserResponse])
def get_users():
    return user_service.get_all_users()

# Get a single user by ID
@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Update user info
@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, updated_data: User):
    user = user_service.update_user(user_id, updated_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Delete a user
@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    deleted = user_service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}

# Deactivate a user (set is_active to False)
@router.patch("/users/{user_id}/deactivate", response_model=UserResponse)
def deactivate_user(user_id: int):
    user = user_service.deactivate_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

