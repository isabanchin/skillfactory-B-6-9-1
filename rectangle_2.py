from rectangle import Rectangle, Square, Circle
#создаем два прямоугольника
rect1 = Rectangle(3,4)
rect2 = Rectangle(12,5)
#создаем два квадрата
square_1 = Square(5)
square_2 = Square(10)
#создаем два круга
circle_1 = Circle(4)
circle_2 = Circle(6)

#вывод площади двух прямоугольников
# print(rect1.get_area())
# print(rect2.get_area())
#вывод площади двух квадратов
# print(square_1.get_area_square(), square_2.get_area_square())

#объединяем все фигуры в один список
figures = [rect1, rect2, square_1, square_2, circle_1, circle_2]
#проходим циклом по списку с проверкой принадлежности каждого объекта списка соответствующему классу
# и расчетом площади в соответствии с классом
for figure in figures:
    if isinstance(figure,Square):
        print(figure.get_area_square())
    elif isinstance(figure,Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())
