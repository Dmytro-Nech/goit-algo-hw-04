from pathlib import Path
from colorama import Fore
import sys

# Перевірка наявності аргумента зі шляхом
if len(sys.argv) < 2:
    print("Будь ласка, вкажіть шлях до директорії як аргумент.")
    sys.exit(1)

# Створення об'єкту Path для директорії
directory = Path(sys.argv[1])

# Перевірка чи вказаний шлях існує і є директорією

if not directory.exists():
    print(f"{Fore.RED}Помилка: Шлях {directory} не існує.{Fore.RESET}")
    sys.exit(1)
if not directory.is_dir():
    print(f"{Fore.RED}Помилка: {directory} не є директорією.{Fore.RESET}")
    sys.exit(1)

# Рекурсивне виведення переліку всіх файлів та піддиректорій різними кольорами
for path in directory.rglob("*"):
   if path.is_dir():
        print(f"{Fore.BLUE}{path.parent}\\{Fore.RESET}{Fore.BLUE}{path.name}{Fore.RESET}")
   else:
        print(f"{Fore.BLUE}{path.parent}\\{Fore.RESET}{Fore.RED}{path.name}{Fore.RESET}")


