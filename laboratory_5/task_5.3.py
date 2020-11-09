class Animal:
    __name = None
    __age = 0
    __sex= None
    def __init__(self, name, age,sex):
        self.__name = name
        self.__age = age
        self.__sex=sex
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_sex(self):
        return self.__sex
    def __str__(self):
        return self.get_str()

class Zebra(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age,sex)
    __description='Зе́бры — подрод рода лошади, включающий виды бурчеллова зебра, \n' \
                  ' зебра Греви и горная зебра. Гибридные формы между зебрами и \n' \
                  ' домашними лошадьми называют зеброидами, между зебрами и ослами — зебрулами.'
    __kind_of_animal='Зебра'
    def get_kind_of_animal(self):
        return self.__kind_of_animal
    def get_descripton(self):
        return self.__description
    def get_str(self):
        return " ".join([" Вид животного:", self.get_kind_of_animal(), "\n",
                         "Имя:", self.get_name(), "\n",
                         "Возраст:", self.get_age(), "\n",
                         "Пол:", self.get_sex(), "\n",
                         "Описание:", self.get_descripton(), "\n",
                         "------------------------------------------------\n"])

class Dolphin(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)
    __description='Дельфи́ны — водные млекопитающие инфраотряда китообразных,\n' \
                  ' принадлежащие либо к семейству дельфиновых — морские,\n' \
                  ' либо к надсемейству речных дельфинов — пресноводные.'
    __kind_of_animal = 'Дельфин'

    def get_kind_of_animal(self):
        return self.__kind_of_animal
    def get_descripton(self):
        return self.__description
    def get_str(self):
        return " ".join([" Вид животного:", self.get_kind_of_animal(), "\n",
                         "Имя:", self.get_name(), "\n",
                         "Возраст:", self.get_age(), "\n",
                         "Пол:", self.get_sex(), "\n",
                         "Описание:", self.get_descripton(), "\n",
                         "------------------------------------------------\n"])

if __name__ == "__main__":
    zebra=Zebra('Марти', '10', 'м')
    dolphin=Dolphin('Галина', '2', 'ж')
    print(dolphin)
    print(zebra)