# This list will hold all the speakers in memory (no database)
speakers = []

# This will help us assign unique IDs to each speaker
speaker_id_counter = 1

# This function runs at app startup to add 3 speakers automatically
def initialize_speakers():
    global speaker_id_counter

    initial_speakers = [
        {"name": "Johnson Gabriel", "topic": "Building APIs with FastAPI"},
        {"name": "Jane Abah", "topic": "Intro to Cloud Services"},
        {"name": "Amaka Bassey", "topic": "Career in Backend Engineering"}
    ]

    for speaker in initial_speakers:
        speaker["id"] = speaker_id_counter
        speakers.append(speaker)
        speaker_id_counter += 1

# This function returns all the speakers
def get_all_speakers():
    return speakers

