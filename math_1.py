#Импортируем математическую библиотеку 
import math 

#создаём класс
class Math_1:
    #Создаём пустые переменные
    x = None
    y = None 
    #Создаём тело 
    def __init__(self, x, y):
        #Сохраняем в self переменные
        self.x = x
        self.y = y

    #Функция cos
    def Cos(self):
        print(math.cos(self.x))
    
    #Функция sin
    def Sin(self):
        print(math.sin(self.x))
    
    #Функция tangents
    def Tan(self):
        print(math.tan(self.x))
    
    #Функция арксинус
    def Asin(self):
        print(math.asin(self.x))
    
    #Функция арккосинус
    def Acos(self):
        print(math.acos(self.x))
    
    #Функция арктангенс
    def Atan(self):
        print(math.atan(self.x))
    
    #Функция арктангенс двух аргументов
    def Atan2(self):
        print(math.atan2(self.x, self.y))
    


#Приглашаем на ввод числа
x = int(input("Введите число: "))
y = int(input("Введите число: "))
#Запихиваем числа в функцию 
math_1 = Math_1(x, y)
#Вызываем таким способом функцию
math_1.Cos()
