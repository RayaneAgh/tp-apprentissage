from datetime import datetime
import random
import json
def load_server_data_from_file():
    with open('storage.json', 'r', encoding='utf-8') as f:
        return json.load(f)
def save_server_data_to_file(data):
    with open('storage.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
def power10(n):
    c = 0
    while n >=10:
        n = n//10
        c+=1
    return c
def Id(List):
    current_ids = [member["id"] for member in List]
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
def findIndexById(List, Id):
    c = 0
    for i in range(len(List)):
        if List[i]['id'] != Id:
            c+=1
        else: return c
def AddChannel():
    print('')
    name = input("Enter a name:")
    id = Id(server_data['channels'])
    server_data['channels']+= [{'name' : name, 'id' : id, "member_ids": []}]
    print('')
    print("You added ",id,". ", name, ' successfully.')
    save_server_data_to_file(server_data)
def AddUsers():
    print("")
    name = input("Enter a name:")
    id = Id(server_data['users'])
    print("")
    server_data['users']+= [{'name' : name, 'id' : id}]
    print("You added ",id,". ", name, ' successfully.')
    save_server_data_to_file(server_data)
def DeleteUsers():
    print("I. See current Users: ")
    print("R. return to User menu:")
    Id = input("Enter ID:")
    if Id.isdigit():
        server_data['users'].pop(findIndexById(server_data['users'], int(Id)))
        save_server_data_to_file(server_data)
        Users()
    elif Id.lower() == 'i':
        ShowUsers()
        DeleteUsers()
    elif Id.lower() == 'r':
        Users()

def ShowUsers():
    print("")
    for i in range(len(server_data["users"])):
        print(server_data['users'][i]['id'], '. ',server_data['users'][i]['name'])
def ChannelAddUsers():
    print("")
    choice = input('Choose channel id: ')
    if choice in [str(server_data["channels"][p]['id']) for p in range(len(server_data["channels"]))]:
        for i in range(len(server_data["users"])):
            print(server_data['users'][i]['id'], '. ',server_data['users'][i]['name'])
        User = input("Choose User Ids (only separated by commas): ")
        User = User.split(',')
        server_data['channels'][findIndexById(server_data['channels'], int(choice))]['member_ids'] += User
        save_server_data_to_file(server_data)
def ShowMess(choice):
    print("List of messages:")
    print("")
    for j in range(len(server_data['messages'])):
        if str(server_data['messages'][j]['channel']) == choice:
            print(server_data['messages'][j]['reception_date'],'. ',server_data['users'][findIndexById(server_data['users'], server_data['messages'][j]['sender_id'])]["name"],':  ', server_data['messages'][j]['content'])
def Menu():
    print()
    print('MENU:')
    print('X. Leave')
    print("M. List of Users")
    print("G. List of Channels")
    print('')
    choice = input('Select an option: ').lower()
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
    print('')
    print('User Menu:')
    print('X. Leave')
    print('R. Return to menu')
    print('U. See current Users: ')
    print('A. Add user:')
    print('D. Delete user:')
    print('')
    choice = input("Enter command: ").lower()
    if choice == 'x':
        return
    elif choice == 'r':
        Menu()
    elif choice == 'u':
        ShowUsers()
        Users()
    elif choice == 'a':
        AddUsers()
        Users()
    elif choice == 'd':
        DeleteUsers()
        Users()
def Channels():
    print("")
    print("Channel menu:")
    print("Enter channel id to see messages:")
    print()
    print('X. Leave')
    print("R. Return to menu")
    print("A. Add channel")
    print("U. Add users in channel")
    for i in range(len(server_data["channels"])):
        print(server_data["channels"][i]['id'],'. groupe: ',server_data['channels'][i]['name'])
    print('')
    choice = input("Enter command: ").lower()
    print()

    if choice == 'a':
        AddChannel()
        Channels()
    elif choice in [str(server_data["channels"][p]['id']) for p in range(len(server_data["channels"]))]:
        ShowMess(choice)
        Channels()
    elif choice == "u":
        ChannelAddUsers()
        Channels()
    elif choice == 'x':
        return
    elif choice == 'r':
        Menu()
    else:
            print('Unknown option:', choice)
            Channels
server_data = load_server_data_from_file()
print('=== Messenger ===')
Menu()