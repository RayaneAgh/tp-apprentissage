from datetime import datetime
import random

server_data = {
    'users': [
        {'id': 41, 'name': 'Alice'},
        {'id': 23, 'name': 'Bob'}
    ],
    'channels': [
        {'id': 12, 'name': 'Town square', 'member_ids': [41, 23]}
    ],
    'messages': [
        {
            'id': 18,
            'reception_date': datetime.now(),
            'sender_id': 41,
            'channel': 12,
            'content': 'Hi 👋'
        }
    ]
}
def power10(n):
    c = 0
    while n >=10:
        n = n//10
        c+=1
    return c
def UserId():
    current_ids = [member["id"] for member in server_data["users"]]
    if not current_ids:
        return 0
    max_id = max(current_ids)
    interval = (max_id // 100) + 1

    start = 100 * (interval - 1)
    end = 100 * interval
    possible_ids = [x for x in range(start, end) if x not in current_ids]
    if not possible_ids:
        start = end
        end = start + 100
        possible_ids = [x for x in range(start, end) if x not in current_ids]
    return random.choice(possible_ids)
def Menu():
    print('MENU:')
    print('X. Leave')
    print("M. List of Users")
    print("G. List of Channels")
    choice = input('Select an option: ').lower()
    print("---------")
    print("\n")
    if choice == 'm':
        Users()
    elif choice == 'x':
        return "Bye"
    elif choice == 'g':
        Channels()
    else:
        print('Unknown option:', choice)
    Menu()
def Users():
    print('User Menu:')
    print('X. Leave')
    print('U: See current Users: ')
    print('A: Add user:')
    print('---------')
    choice = input("Enter command: ").lower()
    if choice == 'x':
        return
    elif choice == 'u':
        for i in range(len(server_data["users"])):
            print(server_data['users'][i]['id'], '. ',server_data['users'][i]['name'])
    elif choice == 'a':
        name = input("Enter a name:")
        id = UserId()
        server_data['users']+= [{'name' : name, 'id' : id}]
    Users()
def Channels():
    print("CHANNEL MENU:")
    print("ENTER CHANNEL ID TO SEE MESSAGES:")
    print('X. Leave')
    for i in range(len(server_data["channels"])):
        print(server_data["channels"][i]['id'],'. groupe: ',server_data['channels'][i]['name'])
    choice = input("Enter command: ").lower()
    print("\n")
    if choice in [str(server_data["channels"][p]['id']) for p in range(len(server_data["channels"]))]:
        print("LIST OF MESSAGES:")
        for j in range(len(server_data['messages'])):
            if str(server_data['messages'][j]['channel']) == choice:
                print(server_data['messages'][j]['reception_date'],'. ', server_data['messages'][j]['content'])
        print("---------")
    elif choice == 'x':
        return
    else:
            print('Unknown option:', choice)
    Channels()
print('=== Messenger ===')
Menu()