class User:
    def __init__(self,user_id, username):#it's a constructor of this function
    #initalize the attribute
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        user.following += 1


user_1 = User("001","Somrat")
user_2 = User("002","Priya")
print(user_1.id)
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


# #attribute using class
# user_1.name = "somrat"
# user_1.id = "001"
#
# print(user_1.name)
#
# #constructor also name as initialize


