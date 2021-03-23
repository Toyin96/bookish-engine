# Toyin's Deli restaurant
sandwich_orders = ['pastrami', 'pepperoni-sauced', 'pastrami', 'garnished mint', "devil's belly", 'pastrami',
                   "rotten potato", "tuna", 'pastrami']
finished_sandwiches = []

print("the deli has run out of pastrami")
for sandwich in sandwich_orders:
    if sandwich.lower() == 'pastrami':
        sandwich_orders.remove(sandwich)
        print("so sorry we just ran out of pastrami")
        continue

    print(f"I made you {sandwich} sandwich")
    finished_sandwiches.append(sandwich.lower())

print(f"\n{finished_sandwiches}")