class Calculator:
    #Умножение 
    def multiply(self,x,y):
        return x * y
    #Сложение
    def adding(self,x,y):
        return x + y
    #Деление
    def division(self, x,y):
        if y == 0:
            return f'Ошибка!'
        else:
            return x /y
    #Деление на ноль
    #Вычитание
    def subtraction(self, x,y):
        return x - y 

    