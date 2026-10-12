class UserSession:
    def __init__(self, username):
        self.username = username
        self.__token = f"token_{username}"
        self.__active = True
        print(f"UserSession created for: {username}")

    def is_active(self):
        return self.__active

    def logout(self):
        if self.__active:
            self.__active = False
            print(f"UserSession logout: {self.username}")
        else:
            print(f"UserSession already inactive: {self.username}")

    def __del__(self):
        if self.__active:
            self.logout()


# Create three sessions and store in a list
sessions = []
sessions.append(UserSession("Alice"))
sessions.append(UserSession("Bob"))
sessions.append(UserSession("Charlie"))

print("\n--- Manually log out one session ---")
sessions[1].logout()

print("\n--- Delete the list ---")
del sessions

print("\n--- Observing destructor messages above ---")