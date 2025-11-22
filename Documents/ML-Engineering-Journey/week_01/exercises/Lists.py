#3.1 List of friend's names
friend_list = ['Dave','Bob','Geoff','Fred']
print(friend_list)
print(friend_list[0])
print(friend_list[1])
for friend in friend_list:
    print(friend)
    
#3.2 Print of friends in list with a personal message

original_message = f"Hello {friend_list[0]}, welcome to Python programming 101, have fun"
print(original_message)

for friend in friend_list:
    new_message = f"Welcome to Python programming 101 {friend}, have fun!"
    print(new_message)

#Some experimenting    
friend_list.insert(0,"Phil")
print(friend_list)

friend_list.append("Martin")
print(friend_list)

friend_list.pop(-1)
print(friend_list)

#3.3 list with narrative - similar to above:
vehicles_list = ["Mustang","Chevy","Ferrari"]
favourite_vehicle = f"I would like to own a {vehicles_list[0]}"
print(favourite_vehicle)
favourite_garage = f"I would like to run a {vehicles_list[1]} garage someday"
print(favourite_garage)
favourite_drive = f"I would like to go for a drive in a {vehicles_list[2]} someday"
print(favourite_drive)

#3.4 and 3.5 Guest List (and amended list of guests)
guest_list = ["Harry", "Rob", "Andy", "Chet"]
popped_guests = guest_list.pop(0)
guest_list.append("Steve")
missing_message = f"Sorry you couldn't make it {popped_guests}"
print(missing_message)
for guest in guest_list:
    welcome_message = f"Welcome to the meal {guest}"
    print(welcome_message)
    
#3.6 More Guests
guest_list = ["Harry", "Rob", "Andy", "Chet"]
popped_guests = guest_list.pop(0)
guest_list.append("Steve")
missing_message = f"Sorry you couldn't make it {popped_guests}"
print(missing_message)
for guest in guest_list:
    welcome_message = f"Welcome to the meal {guest}"
    print(welcome_message)
new_table = "Good Evening All, it turns out we are able to find a bigger table!"
guest_list.insert(0,"Jack")
guest_list.append("Ryan")
guest_list.insert(3,"Jerry")
for guest in guest_list:
    new_welcome_message = f"Welcome to the new table {guest}"
    print(new_welcome_message)
    
#3.7 Shrinking List
guest_list = ["Harry", "Rob", "Andy", "Chet"]
popped_guests = guest_list.pop(0)
guest_list.append("Steve")
missing_message = f"Sorry you couldn't make it {popped_guests}"
print(missing_message)
for guest in guest_list:
    welcome_message = f"Welcome to the meal {guest}"
    print(welcome_message)
new_table = "Good Evening All, it turns out we are able to find a bigger table!"
guest_list.insert(0,"Jack")
guest_list.append("Ryan")
guest_list.insert(3,"Jerry")
for guest in guest_list:
    new_welcome_message = f"Welcome to the new table {guest}"
    print(new_welcome_message)
while True:
    removed_guest = guest_list.pop()
    removal_message = f"My apologies but I am no longer able to invite you {removed_guest}!"
    print(removal_message)
    if len(guest_list) == 2:
        break
for guest in guest_list:
    welcome_message = f"Welcome to the meal {guest}"
    print(welcome_message)
