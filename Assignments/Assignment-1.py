# Example: Instagram

# Task 1: Take Inputs (All Data Types)

# int
followers = int(input("Enter Followers Count: "))
following = int(input("Enter Following Count: "))

# float
avg_watch_time = float(input("Enter Average Watch Time per Reel (seconds): "))

# str
username = input("Enter Username: ")
name = input("Enter Name: ")

# list
instagram_features = list(input("Enter Instagram Features (comma-separated): ").split(","))

# tuple
content_details = tuple(map(int, (input("Enter Number of Posts: "), input("Enter Number of Reels: "))))

# set
interaction_types = set(input("Enter Interaction Types (comma-separated): ").split(","))

# dict
instagram_user = {
    "username": input("Enter your username: "),
    "full_name": input("Enter your full name: "),
    "age": int(input("Enter your age: ")),
    "followers": int(input("Enter number of followers: ")),
    "following": int(input("Enter number of following: ")),
    "posts_count": int(input("Enter number of posts: ")),
    "reels_count": int(input("Enter number of reels: ")),
}

# bool
is_verified = bool(input("Is the account verified? (yes/no): "))


# Task 2: Display Output Using Formatting Methods
print("\n--- Instagram Account Details ---\n")

# 1️ Comma Separation (sep=',')
print("Username, Name, Followers, Following:",
      username, name, followers, following, sep=", ")

# 2️ Percentage Formatting (% operator)
print("Instagram Average Watch Time per Reel (seconds): %.2f" % avg_watch_time)

# 3️ f-strings (f"")
print(f"Username: {username}")
print(f"Name: {name}")
print(f"Followers: {followers}")
print(f"Following: {following}")
print(f"Instagram Features: {instagram_features}")
print(f"Content Details (Posts, Reels): {content_details}")
print(f"Interaction Types: {interaction_types}")
print(f"Verified Account: {is_verified}")

# 4️ .format() method
print("User Profile: Username - {}, Full Name - {}, Age - {}".format(
    instagram_user["username"],
    instagram_user["full_name"],
    instagram_user["age"]
))

print("Account Stats: Followers - {}, Following - {}, Posts - {}, Reels - {}".format(
    instagram_user["followers"],
    instagram_user["following"],
    instagram_user["posts_count"],
    instagram_user["reels_count"]
))

'''
Output:
Enter Followers Count: 712
Enter Following Count: 587
Enter Average Watch Time per Reel (seconds): 28
Enter Username: hampy_reddy8883
Enter Name: Rajendar Reddy
Enter Instagram Features (comma-separated): Reels,Stories,Posts,Live,DMs,Highlights
Enter Number of Posts: 20
Enter Number of Reels: 2
Enter Interaction Types (comma-separated): Likes,Comments,Shares,Saves,Views
Enter your username: hampy_reddy8883
Enter your full name: Gajjela Rajendar Reddy
Enter your age: 25
Enter number of followers: 712
Enter number of following: 587
Enter number of posts: 20
Enter number of reels: 2
Is the account verified? (yes/no): yes

--- Instagram Account Details ---

Username, Name, Followers, Following:, hampy_reddy8883, Rajendar Reddy, 712, 587
Instagram Average Watch Time per Reel (seconds): 28.00
Username: hampy_reddy8883
Name: Rajendar Reddy
Followers: 712
Following: 587
Instagram Features: ['Reels', 'Stories', 'Posts', 'Live', 'DMs', 'Highlights']
Content Details (Posts, Reels): (20, 2)
Interaction Types: {'Shares', 'Comments', 'Saves', 'Likes', 'Views'}
Verified Account: True
User Profile: Username - hampy_reddy8883, Full Name - Gajjela Rajendar Reddy, Age - 25
Account Stats: Followers - 712, Following - 587, Posts - 20, Reels - 2
'''