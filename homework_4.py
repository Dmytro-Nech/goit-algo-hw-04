def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args # Очікуємо два аргументи: ім'я та телефон
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        print("Ivalid data")

def change_contact(args, contacts):
    try:
        name, phone = args  # Очікуємо два аргументи
        if name in contacts:
            contacts[name] = phone
            return "Contact changed."
        else:
            return "This contact doesn't exist."
    except ValueError:
        return "Invalid data. Usage: change <name> <phone>"

    
def phone_username(args, contacts):
    try:
        username = args[0].strip()  # Отримуємо ім'я контакту
        if username in contacts:
            return f"{username}'s phone is: {contacts[username]}"
        else:
            return f"Contact {username} not found."
    except IndexError:
        return "Invalid data. Usage: phone <name>"

    
def print_all(contacts):
    if contacts:
        return contacts
    else:
        return "Phonebook is empty"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(phone_username(args, contacts))
        elif command == "all":
            print(print_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
