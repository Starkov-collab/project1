import logging
import os
from typing import Union

# Создаем папку для логов, если её нет
os.makedirs('logs', exist_ok=True)

# Настройка логгера для модуля masks
logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)  # Устанавливаем уровень DEBUG

# Создаем обработчик для записи в файл
file_handler = logging.FileHandler('logs/masks.log', mode='w')
file_handler.setLevel(logging.DEBUG)

# Настраиваем формат записи
file_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
file_handler.setFormatter(file_formatter)

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """
    Принимает номер карты из 16 цифр и возвращает в формате ХХХХ ХХ** **** XXXX,
    где Х - это замаскированная цифра
    :param card_number: Номер карты
    :return: Маскированный номер карты или сообщение об ошибке
    """
    logger.debug(f'Начало обработки номера карты: {card_number}')
    str_card = str(card_number)

    if not str_card.isdigit():
        logger.error(f'Номер карты содержит не только цифры: {card_number}')
        return "Номер карты должен содержать только цифры"

    if len(str_card) != 16:
        logger.error(f'Номер карты не содержит 16 цифр: {card_number} (длина: {len(str_card)})')
        return "Номер карты должен содержать 16 цифр"

    mask_card = f"{str_card[:4]} {str_card[4:6]}** **** {str_card[-4:]}"
    logger.info(f'Успешно сформирована маска карты: {mask_card}')
    return mask_card


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета"""
    logger.debug(f'Начало обработки номера счета: {account_number}')
    str_account = str(account_number)

    if not str_account.isdigit():
        logger.error(f'Номер счета содержит не только цифры: {account_number}')
        return "Номер счета должен содержать только цифры"

    if len(str_account) != 20:
        logger.error(f'Номер счета не содержит 20 цифр: {account_number} (длина: {len(str_account)})')
        return "Номер счета должен содержать 20 цифр"

    masked_account = f"**{account_number[-4:]}"
    logger.info(f'Успешно сформирована маска счета: {masked_account}')
    return masked_account


if __name__ == '__main__':
    # Тестовые вызовы для проверки
    print(get_mask_card_number("1234567890123456"))
    print(get_mask_card_number("1234"))
    print(get_mask_account("12345678901234567890"))
    print(get_mask_account("123456"))



