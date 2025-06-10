from pydantic import BaseModel

# This is the format for adding a new speaker
class Speaker(BaseModel):
    name: str
    topic: str

# This is what we return when showing a speaker (with ID)
class SpeakerResponse(Speaker):
    id: int

