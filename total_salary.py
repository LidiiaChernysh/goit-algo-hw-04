import math


def  total_salary(path):
    """ 
        The function parses the text file containing information about monthly salaries 
        of developers and returns the total and average salary of all developers.
        - The file contains developer salary data, separated by commas. 
        - Each line represents one developer.

        Parameters:
            path: path to the text file.

        Returns:
            tuple: two numbers: the total amount of salaries and the average salary.
        """
    all_wages = []
    try:
        # open the file for reading
        with open(path, 'r', encoding='utf-8') as my_file:
            for line in my_file.readlines():
                name, wage = line.split(",")
                all_wages.append(int(wage.strip()))
    except FileNotFoundError:
        return f"Помилка: Файл не знайдено."
    except PermissionError:
        return f"Помилка: Немає прав доступу до файлу."
    except UnicodeDecodeError:
        return f"Помилка: Файл має неправильне кодування або пошкоджений."
    except Exception as error:
        return f"Сталася помилка"
    

    sum_salary = math.fsum(all_wages)
    avg_salary = sum_salary/len(all_wages)
    
    return (round(sum_salary, 2), round(avg_salary, 2))
    


total, average = total_salary("../learning_repo/work_with_files/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
