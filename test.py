from calculator import Calculator
cal = Calculator()

#Умножение
def test_multiply_positive():
    x = 3
    y = 3
    res = 9
    assert cal.multiply(x,y) == res, f"Проверка умножения не пройдена {x} * {y} = {res}"

def test_multiply_negative():
    cal = Calculator()
    assert cal.multiply(3,3) !=10
    

#Сложение
def test_adding_positive():
    x = 2
    y = 2
    res = 4
    assert cal.adding(x,y) == res, f"Проверка сложения не пройдена {x} + {y} = {res}"

def test_adding_negative():
    cal = Calculator()
    assert cal.adding(2,2) !=5

#Деление
def test_division_positive():
    x = 8
    y = 2
    res = 4
    assert cal.division(x,y) == res, f"Проверка деления не пройдена {x} / {y} = {res}"

def test__division_negative():
    cal = Calculator()
    assert cal.division(8,2) !=5

#Деление на ноль 
def test_division():
    cal = Calculator()
    assert cal.division(8,0) in 'Ошибка!'

    



#Вычитание
def test_subtraction_positive():
    x = 4
    y = 2
    res = 2
    assert cal.subtraction(x,y) == res, f"Проверка вычитание не пройдена {x} - {y} = {res}"

def test__subtraction_negative():
    cal = Calculator()
    assert cal.subtraction(4,2) !=1