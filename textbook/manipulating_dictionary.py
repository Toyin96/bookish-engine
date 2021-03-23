visited_users = ['ben', 'tam', 'gbenga', 'festus', 'brendan']
verified_users = []

while visited_users:
    current_users = visited_users.pop().capitalize()
    print(f"Adding user: {current_users}...")

    verified_users.append(current_users)
    print(f"Successfully added user: {current_users}")

    if len(visited_users) == 0:
        print(f"\nHere is a list of verified users: {verified_users}")

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']


while 'cat' in pets:
    pets.remove('cat')

print(pets)