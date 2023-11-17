current_users = ['admin', 'eric', 'john', 'james', 'jane', 'kathy', 'sarah', 'sally']
new_users = ['sarah', 'sally', 'joe', 'jill', 'jack']

# make sure all current_users are lowercase
current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"Sorry {user}, that name is taken.")
    else:
        print(f"Great, {user} is still available.")