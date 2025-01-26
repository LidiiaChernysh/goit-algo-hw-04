def get_cats_info(path):
    """ 
        The function reads this file and returns a list of dictionaries 
        with information about each cat.
        The file contains data about cats, where each record contains 
        a unique identifier, the cat's name, and its age.
        The function returns a list of dictionaries, 
        where each dictionary contains information about one cat.

        Parameters:
            path: path to the text file.

        Returns:
            list: a list of dictionaries that contains information about each cat.
    """

    list_of_cats = []
    try:
        # open the file for reading
        with open(path, 'r', encoding='utf-8') as cats_file:
            for line in cats_file.readlines():
                id, name, age = line.split(",")
                # add dicts with info to the list
                list_of_cats.append({"id": id.strip(), "name":name.strip(), "age": int(age.strip())})

    except FileNotFoundError:
        return f"Помилка: Файл не знайдено."

    except PermissionError:
        return f"Помилка: Немає прав доступу до файлу."
    except UnicodeDecodeError:
        return f"Помилка: Файл має неправильне кодування або пошкоджений."
    except Exception as error:
        return f"Сталася помилка"

    
    return list_of_cats


cats_info = get_cats_info("./work_with_files/cats.txt")
print(cats_info)
#print(*cats_info, sep="\n")
