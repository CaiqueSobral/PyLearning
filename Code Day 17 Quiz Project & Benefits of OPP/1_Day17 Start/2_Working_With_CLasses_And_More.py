class User:
    def __init__(self, userID, username):
        self.id = userID
        self.username = username
        self.followers = 0

user1 = User("001", "Angela")

print(user1.followers)

user2 = User("002", "Jack")
