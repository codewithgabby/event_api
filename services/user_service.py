# This list will store all users in memory
users = []

# We'll use this to assign a unique ID to each user
user_id_counter = 1

# Function to create a new user
def create_user(user_data):
    global user_id_counter
    created_user = user_data.dict()
    created_user["id"] = user_id_counter
    users.append(created_user)
    user_id_counter += 1
    return created_user


# Function to get all users
def get_all_users():
    return users

# Function to get one user by ID
def get_user_by_id(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

# Function to update user info
def update_user(user_id: int, user_data):
    for user in users:
        if user["id"] == user_id:
            user.update(user_data.dict())
            return user
    return None

# Function to delete a user
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user["id"] == user_id:
            return users.pop(index)
    return None

# This one just sets is_active to False — pretty straightforward
def deactivate_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            user["is_active"] = False
            return user
    return None

