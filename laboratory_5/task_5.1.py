class Shape:
    __width=0
    __height=0
    def set_width(self, width):
        self.__width=width
    def set_height(self, height):
        self.__height=height
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height

class Rectangle(Shape):
    shape = 'прямоугольник'
    def area(self):
        return self.get_width() * self.get_height()

class Triangle(Shape):
    shape='треугольник'
    def area(self):
        return self.get_width() * self.get_height()/2


if __name__ == "__main__":
    while True:
        chose=int(input('Если рассматриваем треугольник, напишите <<0>> \n'
                    'Если рассматриваем прямоугольник, напишите <<1>>\n'))
        if chose==0:
            figure_in_question=Triangle()
            break
        elif chose==1:
            figure_in_question = Rectangle()
            break
        else:
            print('Введена неправильная цифра')
    width,height=map(int, input('Введите ширину и высоту для этой фигуры: {} \n'.format(figure_in_question.shape)).split())
    figure_in_question.set_width(width)
    figure_in_question.set_height(height)
    print(figure_in_question.area())