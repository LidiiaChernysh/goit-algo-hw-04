def add_contact(args, contacts):
    """
    The function add a user name and phone numer as kay-value to the dict

    Parameters:
        args: list that contains entered and parsed as username and phone
        contacts: dict of contacts
    Returns:
        str: a string containing an explanation of the result
    Raises:
        ValueError: if data entered incorrectly
    """
    try: 
        name, phone = args
        name = name.strip().lower()
        if contacts.get(name) is None: 
            contacts[name] = phone
            return "Contact added."
        else:
            return "Such a name already exists. If you want update it, input command 'change [name] [phone number]'."
    except ValueError:
        return f'After the add command, enter the [name] and [phone number] separated by a space.'
    

def change_contact(args, contacts):
    """
    The function change a user's phone numer

    Parameters:
        args: list that contains entered and parsed as username and phone
        contacts: dict of contacts
    Returns:
        str: a string containing an explanation of the result
    Raises:
        ValueError: if data entered incorrectly
    """
    try: 
        name, phone = args
        name = name.strip().lower()
        if contacts.get(name) is not None:
            contacts[name] = phone
            return "Contact updated."
        else:
            return "Such a name does not exists. If you want to add it, input command 'add [name] [phone number]'."
    except ValueError:
        return f'After the Change command, enter the [name] and [phone number] separated by a space.'


def show_phone(args, contacts):
    """
    The function show a user's phone numer by name

    Parameters:
        args: list that contains entered and parsed a username and phone
        contacts: dict of contacts
    Returns:
        str: a phone number of the user or  string containing an explanation of the result
    Raises:
        ValueError: if data entered incorrectly
    """
    try: 
        name = args[0].strip().lower()
        if contacts.get(name) is not None:
            return contacts[name]
        else:
            return "Such a name does not exists."
    except ValueError:
        return f'After the Change command, enter the [name] and [phone number] separated by a space.'


def show_all(contacts):
    """
    The function show all added contacts

    Parameters:
        contacts: dict of contacts
    Returns:
        dict: dict of contacts
        or str:  string containing an explanation of the result
    """

    if len(contacts) != 0:
        return contacts
    else:
        return 'There is no saved contacts'
    
