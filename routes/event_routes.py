from fastapi import APIRouter, HTTPException
from schemas.event_schema import Event, EventResponse
from services import event_service

router = APIRouter()

# Create a new event
@router.post("/events", response_model=EventResponse)
def create_event(event: Event):
    return event_service.create_event(event)

# Get all events
@router.get("/events", response_model=list[EventResponse])
def get_events():
    return event_service.get_all_events()

# Get a specific event by ID
@router.get("/events/{event_id}", response_model=EventResponse)
def get_event(event_id: int):
    event = event_service.get_event_by_id(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

# Update an event
@router.put("/events/{event_id}", response_model=EventResponse)
def update_event(event_id: int, updated_event: Event):
    event = event_service.update_event(event_id, updated_event)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

# Delete an event
@router.delete("/events/{event_id}")
def delete_event(event_id: int):
    deleted = event_service.delete_event(event_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"message": "Event deleted"}

# Close registration for an event (sets is_open = False)
@router.patch("/events/{event_id}/close", response_model=EventResponse)
def close_registration(event_id: int):
    event = event_service.close_event_registration(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

