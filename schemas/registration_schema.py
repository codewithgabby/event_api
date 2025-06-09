from pydantic import BaseModel
from datetime import date

#   This is the format for registering a user to an event
class Registration(BaseModel):
    user_id: int
    event_id: int
    registration_date: date  # We'll set this during registration
    attended: bool = False   #   By default,   attendance is not marked

# This is the response format that includes the registration ID
class RegistrationResponse(Registration):
    id: int

