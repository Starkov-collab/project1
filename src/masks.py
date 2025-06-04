from typing import Union


def get_mask_card_number(card_number: Union[int,str]) -> str:
    """
    Принимает номер карты из 16 цифр и возвращает в формате ХХХХ ХХ** **** XXXX,
    где Х - это замаскированная цифра
    :param card_number: Номер карты
    :return: Возвращаем маску карты
    """
    str_card = str(card_number)
    """Преобразованием в строку если номер карты запрашивается не через input"""
    if not str_card.isdigit() :
        """проверка на то,чтобы были только цифры"""
        return "Номер карты должен содержать только цифры"

    if len(str_card) != 16 :
        """Проверка длины карты"""
        return "Номер карты должен содержать 16 цифр"

    mask_card: str = f"{str_card[:4]} {str_card[4:6]}** **** {str_card[-4:]}"
    return mask_card



def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета"""
    str_card = str(account_number)

    if not str_card.isdigit() :
        """проверка на то,чтобы были только цифры"""
        return "Номер счет должен содержать только цифры"

    if len(str_card) != 20 :
        return  "Номер счета должен содержать 20 цифр"

    if str_card < account_number and str_card > account_number :
        return "Неверное колличество символов"

    return f"**{account_number[-4:]}"



