from datetime import datetime

def filter_by_state(operation_list: list[dict], state : str = "EXECUTED") -> list[dict] :
    """
    Фильтрует список словарей по значению ключа 'state'
    """
    return [operation_list for operation_list in operation_list if operation_list.get("state") == state]



def sort_by_date(operation_list: list[dict], reverse: bool = True) -> list[dict]:
    """
        Сортирует список словарей по дате (ключ "date") в указанном порядке.
    """
    return sorted(
        transactions,
        key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=reverse,
    )