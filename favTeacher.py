print('Welcome to Favorite Teachers Program')
fav_teacher = []
teacher = input('Who is your first favorite teacher: ').title().strip()
fav_teacher.append(teacher)
teacher = input('Who is your second favorite teacher: ').title().strip()
fav_teacher.append(teacher)
teacher = input('Who is your third favorite teacher: ').title().strip()
fav_teacher.append(teacher)
fav_teacher.append(input('Who is your forth favorite teacher: ').title().strip())

print(f'Your favorite teacher raked are:{fav_teacher}')
sort_teacher = sorted(fav_teacher)
print(f'Your favorite teacher alphabetically are:', sort_teacher)
r_sorted = sorted(fav_teacher, reverse=True)
print(f'Your favorite teacher reverse alphabetically are:', r_sorted)

print(f'Your top two teachers are: {fav_teacher[0]} and {fav_teacher[1]}.')
print(f'Your next two teachers are: {fav_teacher[2]} and {fav_teacher[3]}.')
print(f'Your last favorite teacher is: {fav_teacher[-1]}.')
print(f'You have a total of {len(fav_teacher)} favorite teachers')

# fav_teacher.pop(0)

fav_teacher.insert(0, input(
    f'Oops {fav_teacher[0]} is no longer your favorite teacher. Who is your fav teacher now:').title().strip())

print(f'Your favorite teacher raked are:{fav_teacher}')
sort_teacher = sorted(fav_teacher)
print(f'Your favorite teacher alphabetically are:', sort_teacher)
r_sorted = sorted(fav_teacher, reverse=True)
print(f'Your favorite teacher reverse alphabetically are:', r_sorted)

print(f'Your top two teachers are: {fav_teacher[0]} and {fav_teacher[1]}')
print(f'Your next two teachers are: {fav_teacher[2]} and {fav_teacher[3]}')
print(f'Your last favorite teacher is: {fav_teacher[-1]}')
print(f'You have a total of {len(fav_teacher)} favorite teachers.')

fav_teacher.remove(input('You have decided to remove a fav teacher. Which one would u like to remove?: ').title().strip())
print('Your fav teachers finally are:', fav_teacher)