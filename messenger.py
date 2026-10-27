from datetime import datetime

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

print('=== Messenger ===')
while True:
    print('MENU:')
    print('X. Leave')
    print("M. List of Users")
    print("G. List of Channels")
    choice = input('Select an option: ').lower()
    if choice == 'm':
        print('The users are: ') #[server_data['users'][i]['name']for i in range(len(server_data["users"]))])
        for i in range(len(server_data["users"])):
            print(server_data['users'][i]['name'])
        print('\n')
    elif choice == 'x':
        break
    elif choice == 'g':
            print('The channels are:')
            for i in range(len(server_data["channels"])):
                print("'",server_data['channels'][i]['name'],"'", " id: ", server_data['channels'][i]['id'])
            print("\n")
            while choice != 'x':
                print("CHANNEL MENU:")
                print("ENTER CHANNEL ID TO SEE MESSAGES:")
                print('X. Leave')
                for i in range(len(server_data["channels"])):
                     print(server_data["channels"][i]['id'],'. groupe: ',server_data['channels'][i]['name'])
                choice = input("Enter command: ").lower()
                if choice in [str(server_data["channels"][p]['id']) for p in range(len(server_data["channels"]))]:
                    c=0
                    print("LIST OF MESSAGES:")
                    for j in range(len(server_data['messages'])):
                        if str(server_data['messages'][j]['channel']) == choice:
                           c+=1
                           print(c,'. ', server_data['messages'][j]['content'])
                    print("\n")
                elif choice == 'x':
                    print("\n")
                    break
    else:
        print('Unknown option:', choice)
print('Bye')