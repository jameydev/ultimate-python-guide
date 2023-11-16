guest_list = [
                'Albert Einstein', 
                'John Lennon', 
                'Linus Torvalds', 
                'Steve Jobs', 
                'Nikola Tesla'
            ]

for guest in guest_list:
    print(f"Dear {guest}, I would like to invite you to dinner.")

print(f"\n{guest_list[2]} can't make it to dinner.\n")
guest_list[2] = 'Neil Armstrong'

for guest in guest_list:
    print(f"Dear {guest}, I would like to invite you to dinner.")

print("\nI found a bigger table, so I'm inviting more people.\n")

guest_list.insert(0, 'Ada Lovelace')
guest_list.insert(3, 'Grace Hopper')
guest_list.append('Margaret Hamilton')
guest_list.append('Katherine Johnson')
guest_list.insert(0, 'Alan Turing')
guest_list.insert(3, 'Dennis Ritchie')
guest_list.append('Ken Thompson')
guest_list.insert(1, 'Bill Gates')
guest_list.append('John D. Rockefeller')
guest_list.insert(5, 'Andrew Carnegie')

for guest in guest_list:
    print(f"Dear {guest}, I would like to invite you to dinner.")