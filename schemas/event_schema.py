from pydantic import BaseModel
from datetime import date

# This is the structure for creating a new event
class Event(BaseModel):
    title: str
    location: str
    date: date
    is_open: bool = True  # By default, events are open for registration

# This is what we’ll return when showing an event (with its ID)
class EventResponse(Event):
    id: int

