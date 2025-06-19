def log(filename=None):
    def my_decor(func):
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                success_message = f"Функция {func.__name__} успешно завершена. Результат: {result}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(success_message + "\n")
                else:
                    print(success_message)
                return result
            except Exception as e:
                error_message = f"Ошибка в {func.__name__}: {type(e).__name__}, args: {args}, kwargs: {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as text:
                        text.write(error_message + "\n")
                else:
                    print(error_message)
        return inner
    return my_decor