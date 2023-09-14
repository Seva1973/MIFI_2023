def make_Cocktail(func):
    def wrapper(*args):
        print("Ингридиенты для котейля: ")
        print("Мороженное, Молоко, Бананы")
        print("Рецепт: \n"
              "1. Залить молоко в миксер\n"
              "2. Добавить мороженое в молоко\n"
              "3. Нарезать бананы\n"
              "4. Запустить миксер\n")
        func(args, "Молоко", "Бананы", "Мороженное")
    return wrapper


def make_Meat(func):
    def wrapper(*args):
        print("Ингридиенты для мяса: ")
        print("Мясо, Специи, Лук")
        print("Рецепт:\n"
              "1. Пожарить лук\n"
              "2. Пожарить мясо\n"
              "3. Добавить специи\n")
        func(args, "Мясо", "Специи", "Лук")
    return wrapper


@make_Meat
@make_Cocktail
def cook_Dinner(*args):
    print(f"Игоговый список покупок: {args}")


cook_Dinner()
