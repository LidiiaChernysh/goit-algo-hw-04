# import needed functions
from command_parser import parse_input
from command_handler import add_contact, change_contact, show_phone, show_all


def main():
    
    # Create a dict for saving contacts 
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        # parse inputed command 
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")

        # add contact to dict: name and phone number
        elif command == "add":
            print(add_contact(args, contacts))

        # change username's phone
        elif command == "change": 
            print(change_contact(args, contacts))

        # display a phon by given name
        elif command == "phone": 
            print(show_phone(args, contacts))
        
        # show all contacts
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()