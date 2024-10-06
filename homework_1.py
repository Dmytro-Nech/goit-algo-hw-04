def total_salary(path) -> tuple:
    salary_list = []
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh.readlines():
                if not line.strip():  # Пропускаємо порожні строки
                    continue
                sal = line.split(",")
                if len(sal) < 2:  # Перевіряємо, що строка має хоча б 2 елемента
                    print(f"Incorrect line: {line.strip()}")
                    continue
                try:
                    salary_list.append(int(sal[1].strip()))
                except ValueError:
                    print(f"Incorrect salary value : {line.strip()}")
                    continue
        total = sum(salary_list)
        average = int(total / len(salary_list))
        return (total, average)
    except FileNotFoundError: # Обробляємо інші виключення
        print("File not found")
        return None
    except Exception as e:
        print("File is damaged or incorrect file data", e)
        return None
    
if __name__ == "__main__":
    try:
        total, average = total_salary("salary.txt")
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except Exception as e:
        print("Something goes wrong")