import colorama
import inspect

colorama.init(autoreset=True)

print("Інтроспекція colorama:\n")
for name, data in inspect.getmembers(colorama):
    if not name.startswith("__"):
        print(f"{name}: {type(data)}")

print("\nНайважливіші атрибути та демонстрація їх роботи:\n")

from colorama import Fore, Back, Style

print(Fore.BLUE + "Це синій текст")
print(Fore.RED + "Це червоний текст")
print(Fore.WHITE + Back.BLUE + "Білий текст на синьому")
print(Style.BRIGHT + "Яскравий стиль тексту")
print(Style.DIM + "Темний стиль тексту")
print(Style.RESET_ALL + "Стиль скинуто до стандартного")

print("\ncolorama дозволяє робити кольоровий текст у консолі — зручно для логів, меню, повідомлень.")
