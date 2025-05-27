from datetime import datetime

from src.masks import get_mask_card_number


def mask_account_card(info_card: str) -> str:
    """Функция определяет счет это или номер карты и возвращает замаскированный.

        Параметры:
            info_card (str): Строка с информацией о карте/счете, например "Карта 1234567812345678".

        Возвращает:
            str: Замаскированная строка, например "Карта 1234 56** **** 5678".
        """
    # 1. Извлекаем номер (последнюю группу цифр)
    number = ''.join(filter(str.isdigit, info_card))  # Оставляем только цифры

    # 2. Определяем тип (карта или счет)
    if len(number) == 16:  # Номер карты обычно 16 цифр
        # 3. Маскируем номер карты
        masked = (number[:4] + " " + number[4:6] + "** **** " + number[-4:])
        return info_card.split()[0] + " " + masked  # Сохраняем исходный префикс ("Карта")
    elif len(number) == 20:  # Номер счета обычно 20 цифр
        # 4. Маскируем номер счета
        masked = "**" + number[-4:]
        return info_card.split()[0] + " " + masked

def get_date(date: str) -> str:
    """Парсим строку с датой в объект datetime"""
    date_obj = datetime.fromisoformat(date)
    """Форматируем дату в нужный формат "ДД.ММ.ГГГГ"""
    formatted_date = date_obj.strftime("%d.%m.%Y")
    return formatted_date
