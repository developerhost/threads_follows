from threads import Threads
threads = Threads(username='kanon_div', password='password')

user_id = threads.public_api.get_user_id(username='kanon_div')
print(user_id) # 2046290109

user_followers = threads.private_api.get_user_followers(id=2046290109)

# print(user_followers)

usernames_followers = [user['username'] for user in user_followers['users']]

# print(usernames_followers)

user_follows = threads.private_api.get_user_following(id=2046290109)

# print(user_follows)

usernames_follows = [user['username'] for user in user_follows['users']]

# Convert lists to sets
set_followers = set(usernames_followers)
set_following = set(usernames_follows)

# Get the intersection (users that are both followed by and following)
both_following_and_followers = list(set_followers & set_following)

# Get the difference (users that are followed by but not following)
only_following_not_followers = list(set_following - set_followers)

# Get the difference (users that are following but not followed by)
only_followers_not_following = list(set_followers - set_following)

# Now you have the three lists:
print("両思い:")
print(both_following_and_followers)

print("フォローだけ、フォロワーではない:")
print(only_following_not_followers)

print("フォロワーだけ、フォローはしてない:")
print(only_followers_not_following)