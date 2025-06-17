import os
from functools import wraps

import pytest

from src.decorators import log


# Тестируемые функции для демонстрации работы декоратора
@log()
def successful_func(a, b):
    return a + b


@log()
def failing_func(a, b):
    return a / b


@log(filename="test_log.txt")
def file_logged_func(a, b):
    return a * b


@log(filename="test_log.txt")
def file_logged_failing_func(a, b):
    return a / b


def test_successful_execution_with_console_output(capsys):
    """Тест успешного выполнения с выводом в консоль"""
    result = successful_func(2, 3)
    captured = capsys.readouterr()

    assert result == 5
    assert "Функция successful_func успешно завершена. Результат: 5" in captured.out


def test_failing_execution_with_console_output(capsys):
    """Тест ошибки с выводом в консоль"""
    result = failing_func(10, 0)
    captured = capsys.readouterr()

    assert result is None
    assert "Ошибка в failing_func: ZeroDivisionError" in captured.out
    assert "args: (10, 0)" in captured.out
    assert "kwargs: {}" in captured.out


def test_successful_execution_with_file_output():
    """Тест успешного выполнения с записью в файл"""
    # Удаляем файл, если он существует
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    result = file_logged_func(4, 5)

    assert result == 20
    assert os.path.exists("test_log.txt")

    with open("test_log.txt", "r", encoding="utf-8") as f:
        content = f.read()
        assert "Функция file_logged_func успешно завершена. Результат: 20" in content


def test_failing_execution_with_file_output():
    """Тест ошибки с записью в файл"""
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    result = file_logged_failing_func(10, 0)

    assert result is None
    assert os.path.exists("test_log.txt")

    with open("test_log.txt", "r", encoding="utf-8") as f:
        content = f.read()
        assert "Ошибка в file_logged_failing_func: ZeroDivisionError" in content
        assert "args: (10, 0)" in content
        assert "kwargs: {}" in content


def test_file_output_appends_not_overwrites():
    """Тест, что записи в файл добавляются, а не перезаписываются"""
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    file_logged_func(1, 2)
    file_logged_func(3, 4)

    with open("test_log.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        assert len(lines) == 2
        assert "Результат: 2" in lines[0]
        assert "Результат: 12" in lines[1]


def test_decorator_preserves_function_metadata():
    """Тест, что декоратор сохраняет метаданные функции"""

@log()
def func_with_metadata(a, b):
    """Test function"""
    return a + b

    assert func_with_metadata.__name__ == "func_with_metadata"
    assert func_with_metadata.__doc__ == "Test function"