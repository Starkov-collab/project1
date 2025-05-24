from datetime import datetime

from src.masks import get_mask_card_number


def mask_account_card(info_card: str) -> str:
    """Функция определяет счет это или номер карты и возвращает замаскированный"""
    info_card_list = info_card.split()
    if "Счет" in info_card_list:
        return f"Счет **{info_card_list[-1][-4:]}"
    else:
        card_name = " ".join(info_card_list[:-1])
        card_number = info_card_list[-1].replace(" ", "")
        return f"{card_name} {get_mask_card_number(card_number)}"


def get_date(date: str) -> str:
    """Парсим строку с датой в объект datetime"""
    date_obj = datetime.fromisoformat(date)
    """Форматируем дату в нужный формат "ДД.ММ.ГГГГ"""
    formatted_date = date_obj.strftime("%d.%m.%Y")
    return formatted_date
