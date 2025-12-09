import pytest
from calculator import (
    calculate_simple_interest,
    calculate_compound_interest,
    calculate_tax
)


class TestCalculateSimpleInterest:
    """Тесты для функции calculate_simple_interest"""
    
    def test_correct_calculation_example1(self):
        """Проверка правильности расчета: пример 1"""
        result = calculate_simple_interest(1000, 5, 2)
        assert result == 100.0
    
    def test_correct_calculation_example2(self):
        """Проверка правильности расчета: пример 2"""
        result = calculate_simple_interest(500, 10, 3)
        assert result == 150.0
    
    def test_zero_values(self):
        """Проверка работы с нулевыми значениями"""
        assert calculate_simple_interest(0, 5, 2) == 0.0
        assert calculate_simple_interest(1000, 0, 2) == 0.0
        assert calculate_simple_interest(1000, 5, 0) == 0.0
    
    def test_negative_values(self):
        """Проверка вызова ValueError при отрицательных значениях"""
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_simple_interest(-1000, 5, 2)
        
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_simple_interest(1000, -5, 2)
        
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_simple_interest(1000, 5, -2)


class TestCalculateCompoundInterest:
    """Тесты для функции calculate_compound_interest"""
    
    def test_correct_calculation_example1(self):
        """Проверка правильности расчета: пример 1 (ежегодное начисление)"""
        result = calculate_compound_interest(1000, 5, 2)
        expected = 1000 * (1 + 5/(100*1))**(1*2) - 1000
        assert result == pytest.approx(expected)
    
    def test_correct_calculation_example2(self):
        """Проверка правильности расчета: пример 2 (ежеквартальное начисление)"""
        result = calculate_compound_interest(1000, 12, 1, n=4)
        expected = 1000 * (1 + 12/(100*4))**(4*1) - 1000
        assert result == pytest.approx(expected)
    
    def test_zero_values(self):
        """Проверка работы с нулевыми значениями"""
        assert calculate_compound_interest(0, 5, 2) == 0.0
        assert calculate_compound_interest(1000, 0, 2) == 0.0
        assert calculate_compound_interest(1000, 5, 0) == 0.0
    
    def test_negative_values(self):
        """Проверка вызова ValueError при отрицательных значениях"""
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_compound_interest(-1000, 5, 2)
        
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_compound_interest(1000, -5, 2)
        
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_compound_interest(1000, 5, -2)
    
    def test_invalid_n(self):
        """Проверка некорректного значения n"""
        with pytest.raises(ValueError, match="n должно быть целым положительным числом"):
            calculate_compound_interest(1000, 5, 2, n=0)
        
        with pytest.raises(ValueError, match="n должно быть целым положительным числом"):
            calculate_compound_interest(1000, 5, 2, n=-1)
        
        with pytest.raises(ValueError, match="n должно быть целым положительным числом"):
            calculate_compound_interest(1000, 5, 2, n=1.5)


class TestCalculateTax:
    """Тесты для функции calculate_tax"""
    
    def test_correct_calculation_example1(self):
        """Проверка правильности расчета: пример 1"""
        result = calculate_tax(1000, 20)
        assert result == 200.0
    
    def test_correct_calculation_example2(self):
        """Проверка правильности расчета: пример 2"""
        result = calculate_tax(500, 15)
        assert result == 75.0
    
    def test_zero_values(self):
        """Проверка работы с нулевыми значениями"""
        assert calculate_tax(0, 20) == 0.0
        assert calculate_tax(1000, 0) == 0.0
    
    def test_invalid_tax_rate(self):
        """Проверка некорректной ставки налога"""
        with pytest.raises(ValueError, match="Ставка налога должна быть между 0 и 100"):
            calculate_tax(1000, 150)
        
        with pytest.raises(ValueError, match="Ставка налога должна быть между 0 и 100"):
            calculate_tax(1000, -10)
    
    def test_boundary_values(self):
        """Проверка граничных значений"""
        assert calculate_tax(1000, 0) == 0.0
        
        assert calculate_tax(1000, 100) == 1000.0
    
    def test_negative_amount(self):
        """Проверка отрицательной суммы"""
        with pytest.raises(ValueError, match="Сумма должна быть неотрицательной"):
            calculate_tax(-1000, 20)