class Mother:
    __who='Я мать'
    def __str__(self):
        return Mother.__who

class Daughter(Mother):
    __who = 'Я дочка матери'

    def __str__(self):
        return Daughter.__who

if __name__ == "__main__":
    Mother=Mother()
    Daughter=Daughter()
    print(Mother)
    print(Daughter)