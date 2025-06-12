from fastapi import FastAPI
from routes import user_routes, event_routes, speaker_routes, registration_routes
from services.speaker_service import initialize_speakers

app = FastAPI()

# Bringing in all the routers from different files
app.include_router(user_routes.router)
app.include_router(event_routes.router)
app.include_router(speaker_routes.router)
app.include_router(registration_routes.router)

#   When the app starts, we add 3 speakers by default
initialize_speakers()



# Final review complete – ready for submission.



