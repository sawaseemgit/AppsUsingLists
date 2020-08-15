import datetime

time = datetime.datetime.now()
print('Welcome to the Grocery List App')
print(f'Current Date and Time: {time.month}/{time.day}\t{time.hour}:{time.minute}')
grocery = ['Cheese','Meat']
for i in range(3):
    item = input('Add item to grocery list: ')
    grocery.append(item.title())

print(f'Here is your grocery list:', grocery)
grocery.sort()
print(f'Here is your grocery list:', grocery)

print('Simulating grocery shopping...\n')
print('Current grocery list:', len(grocery), ' items')
while len(grocery) >2:
    removeItem = input('What food item did you just buy: ').title()
    grocery.remove(removeItem)
    print(f'Removing {removeItem} from the list\n')

print(f'Current grocery list: {len(grocery)} items')
print(grocery)
print(f'Sorry, we are out of {grocery[1]}.')
grocery.pop()
item = input('What item would you like instead? ').title()
grocery.insert(0, item)
print('Here is what remains in your grocery list:', grocery)
