from fastapi import APIRouter
from services.speaker_service import get_all_speakers

router = APIRouter()

# This route will return the list of all initialized speakers
@router.get("/speakers")
def list_speakers():
    return get_all_speakers()

