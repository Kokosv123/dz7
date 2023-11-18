import os

def safe_calculate(func):
    def wrapper(expression):
        try:
            result = func(expression)
            safe_expression = "".join(c for c in expression if c.isalnum())
            filename = f"{safe_expression}.txt"
            with open(filename, 'w') as f:
                f.write(str(result))
            return result
        except ZeroDivisionError:
            return "Ошибка: Деление на ноль не поддерживается."
        except (SyntaxError, NameError, TypeError):
            return "Ошибка: Неправильное выражение."

    return wrapper

@safe_calculate
def calculate(expression):
    return eval(expression)

result = calculate("45+32")
print(result)
