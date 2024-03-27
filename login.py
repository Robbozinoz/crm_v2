# To implement a basic login system without external packages, you can create a simple username/password authentication mechanism in Python. Here's a step-by-step guide to implementing it:

# Define User Credentials:
# Start by defining predefined usernames and passwords. You can store this information in a dictionary for simplicity.

# Login Functionality:
# Create a function for the login process where users can enter their username and password. Check if the provided credentials match the predefined ones.

# Logout Functionality:
# Implement a logout option to exit the system.

# Define user credentials (username: password)
USER_CREDENTIALS = {
    "user1": "password1",
    "user2": "password2",
    # Add more users if needed
}

def login():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            print("Login successful!")
            return username
        else:
            print("Invalid username or password. Please try again.")

def logout(username):
    print(f"Goodbye, {username}!")

# Example usage:
if __name__ == "__main__":
    print("Welcome to the CRM system!")
    current_user = login()
    # Perform CRM operations here
    logout(current_user)
