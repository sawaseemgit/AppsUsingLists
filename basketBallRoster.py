print('Welcome to the Basketball Roster Program')
roster = []
player = input('Who is the point guard? ').title().strip()
roster.append(player)
player = input('Who is the shooting guard? ').title().strip()
roster.append(player)
player = input('Who is the small forward? ').title().strip()
roster.append(player)
player = input('Who is the power forward? ').title().strip()
roster.append(player)
player = input('Who is the center? ').title().strip()
roster.append(player)

print(f'\tYour starting 5 for the upcoming basketball season are:')
print('\t\tPoint Guard:\t', roster[0])
print('\t\tShooting Guard:\t', roster[1])
print('\t\tSmall Forward:\t', roster[2])
print('\t\tPower Guard:\t', roster[3])
print('\t\tCenter:\t', roster[4])

injured_player = roster.pop(2)
print(f'Oh no {injured_player} is injured.')

print(f'Your roster will have only {len(roster)} players.')
player = input(f"Who will take {injured_player}'s spot: ").title().strip()
roster.insert(2,player)

print('\t\tPoint Guard:\t', roster[0])
print('\t\tShooting Guard:\t', roster[1])
print('\t\tSmall Forward:\t', roster[2])
print('\t\tPower Guard:\t', roster[3])
print('\t\tCenter:\t', roster[4])

print(f'Your roster has {len(roster)} players now')
