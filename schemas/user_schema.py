from pydantic import BaseModel, EmailStr

# This is the format we will use when creating a new user
class User(BaseModel):
    name: str
    email: EmailStr
    is_active: bool = True  # By default, the user is active

# This is what we will send back when returning a user (including their ID)
class UserResponse(User):
    id: int

