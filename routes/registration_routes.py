from fastapi import APIRouter, HTTPException
from services import registration_service

router = APIRouter()






# Register a user for an event
@router.post("/registrations")
def register_user(user_id: int, event_id: int):
    result = registration_service.register_user_for_event(user_id, event_id)
    
    # If there's an error, return it as an HTTP 400 response
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    
    return result

# Mark attendance for a specific registration
@router.patch("/registrations/{registration_id}/attend")
def mark_attendance(registration_id: int):
    updated = registration_service.mark_attendance(registration_id)
    if not updated:
        raise HTTPException(status_code=404, detail="Registration not found")
    return updated

# Get all registrations
@router.get("/registrations")
def get_all_registrations():
    return registration_service.get_all_registrations()

# Get all registrations for a specific user
@router.get("/users/{user_id}/registrations")
def get_user_registrations(user_id: int):
    return registration_service.get_user_registrations(user_id)





# Get users who attended at least one event
@router.get("/attendees")
def users_who_attended():
    return registration_service.get_users_who_attended()

