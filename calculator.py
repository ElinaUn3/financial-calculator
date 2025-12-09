def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    """
    Рассчитывает простые проценты.
    
    Args:
        principal: Основная сумма
        rate: Процентная ставка (в процентах)
        time: Время (в годах)
    
    Returns:
        Сумма простых процентов
    
    Raises:
        ValueError: Если аргументы отрицательные
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Аргументы должны быть неотрицательными")
    
    return principal * rate * time / 100


def calculate_compound_interest(principal: float, rate: float, time: float, n: int = 1) -> float:
    """
    Рассчитывает сложные проценты.
    
    Args:
        principal: Основная сумма
        rate: Процентная ставка (в процентах)
        time: Время (в годах)
        n: Количество начислений процентов в год
    
    Returns:
        Сумма сложных процентов
    
    Raises:
        ValueError: Если аргументы некорректны
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Аргументы должны быть неотрицательными")
    
    if n <= 0 or not isinstance(n, int):
        raise ValueError("n должно быть целым положительным числом")
    
    total_amount = principal * (1 + rate / (100 * n)) ** (n * time)
    
    return total_amount - principal


def calculate_tax(amount: float, tax_rate: float) -> float:
    """
    Рассчитывает сумму налога.
    
    Args:
        amount: Сумма, с которой рассчитывается налог
        tax_rate: Ставка налога (в процентах)
    
    Returns:
        Сумма налога
    
    Raises:
        ValueError: Если ставка налога не в диапазоне 0-100%
    """
    if not 0 <= tax_rate <= 100:
        raise ValueError("Ставка налога должна быть между 0 и 100")
    
    if amount < 0:
        raise ValueError("Сумма должна быть неотрицательной")
    
    return amount * tax_rate / 100