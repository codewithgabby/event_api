# This list will hold all events in memory
events = []

# We’ll use this counter to assign a unique ID to each event
event_id_counter = 1

# Function to create a new event
def create_event(event_data):
    global event_id_counter
    new_event = event_data.dict()
    new_event["id"] = event_id_counter
    events.append(new_event)
    event_id_counter += 1
    return new_event

# This returns the list of all events that have been created so far
def get_all_events():
    return events

# Get a specific event by ID
def get_event_by_id(event_id: int):
    for event in events:
        if event["id"] == event_id:
            return event
    return None

# Update event details
def update_event(event_id: int, event_data):
    for event in events:
        if event["id"] == event_id:
            event.update(event_data.dict())
            return event
    return None

# Delete an event
def delete_event(event_id: int):
    for index, event in enumerate(events):
        if event["id"] == event_id:
            return events.pop(index)
    return None

# Function to close registration for an event
def close_event_registration(event_id: int):
    for event in events:
        if event["id"] == event_id:
            event["is_open"] = False
            return event
    return None

