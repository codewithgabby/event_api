from datetime import date
from services import user_service, event_service







# This list will store all registration records
registrations = []

# Counter to assign unique ID to each registration
registration_id_counter = 1

# Function to register a user for an event
def register_user_for_event(user_id: int, event_id: int):
    global registration_id_counter

    # First, get the user and event
    user = user_service.get_user_by_id(user_id)
    event = event_service.get_event_by_id(event_id)

    # Check if user or event doesn’t exist
    if not user or not event:
        return {"error": "User or Event not found"}

    # Check if user is inactive
    if not user["is_active"]:
        return {"error": "User is not active"}

    # Check if event is closed
    if not event["is_open"]:
        return {"error": "Event is not open for registration"}

    # I had to add this check to avoid duplicate registrations
    # Took me a while to figure out it wasn’t handled by FastAPI itself
    for reg in registrations:
        if reg["user_id"] == user_id and reg["event_id"] == event_id:
            return {"error": "User already registered for this event"}

    # If everything is fine, create the registration
    new_registration = {
        "id": registration_id_counter,
        "user_id": user_id,
        "event_id": event_id,
        "registration_date": date.today(),
        "attended": False
    }
    registrations.append(new_registration)
    registration_id_counter += 1
    return new_registration






# Mark attendance for a registration
def mark_attendance(registration_id: int):
    for reg in registrations:
        if reg["id"] == registration_id:
            reg["attended"] = True
            return reg
    return None

# Get all registrations
def get_all_registrations():
    return registrations

# Get registrations by user ID
def get_user_registrations(user_id: int):
    return [reg for reg in registrations if reg["user_id"] == user_id]








# Filter users who attended at least one event
def get_users_who_attended():
    attended_ids = set([reg["user_id"] for reg in registrations if reg["attended"]])              
    return [user for user in user_service.get_all_users() if user["id"] in attended_ids]

# I was trying to fix a bug here earlier
# This part confused me at first but it worked


