def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        if args[0] in contacts:
            add_answer= input("Such contact name exists, overwrite yes/no?").strip().lower()
            if add_answer == "yes":
                name, phone = args
                contacts[name] = phone
                return "Contact overwritten"
            else:
                return "Contact not recorded"
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except (ValueError, IndexError):
        return "To add, you need to enter name and phone number."

def change_contact(args,contacts):
    try:
        for name, phone in contacts.items():
            if name == args[0]:
                contacts[name] = args[1]
                return "Contact updated."
        return "Name not found"
    except (IndexError, ValueError):
        return "something went wrong..."
    

def show_phone(args, contacts):
    try:
        for name, phone in contacts.items():
            if name == args[0]:
                return phone
        return "Name not found"
    except (IndexError, ValueError):
        return "something went wrong..."

def show_all(contacts):
    line = []
    for name, phone in sorted(contacts.items()):
        line.append(f"{name}: {phone}")
    return "\n".join(line)