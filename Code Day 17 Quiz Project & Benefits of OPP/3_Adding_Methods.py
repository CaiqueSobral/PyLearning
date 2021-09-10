class User:
    def __init__(self, userID, username):
        self.id = userID
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User("001", "Angela")
user2 = User("002", "Jack")

user1.follow(user2)
