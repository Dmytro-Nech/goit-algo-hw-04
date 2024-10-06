def get_cats_info(path) -> list:
    cats_list = []
    try:
        with open(path, "r", encoding="utf-8") as file:
           for line in file:
                if not line.strip():  # Пропускаємо порожні строки
                    continue
                el = line.split(",")
                if len(el) < 3:  # Перевіряємо чи в строці достатньо даних
                    print(f"Incorrect line: {line.strip()}")
                    continue
                # Створюємо словник
                cat_dict = { 
                    "id": el[0].strip(),
                    "name": el[1].strip(),
                    "age": el[2].strip()
                }
                cats_list.append(cat_dict)
        return cats_list
    except FileNotFoundError: # Обробляємо виключення
        print("File not found")
        return None
    except Exception as e:
        print("File is damaged or contains incorrect data", e)
        return None
    

if __name__ == "__main__":
    print(get_cats_info("test_files\cats.txt"))

