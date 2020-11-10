class Vector():
    def __init__(self, x = 0, y = 0, z=0):
        self.x = int(x)
        self.y = int(y)
        self.z= int(z)
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y,self.z + other.z)
    def __sub__(self, other):
        return Vector(self.x -other.x, self.y - other.y,self.z -other.z)

    def __mul__(self, other):
        return self.x * other.x+ self.y * other.y+self.z*other.z
    def __matmul__(self, other):
        return Vector(self.y*other.z-other.y*self.z, self.z*other.x-self.x*other.z,self.x*other.y-self.y*other.x)

    def __str__(self):
        return '({},{},{})'.format(self.x,self.y,self.z)
    def lenght(self):
        return (self.x**2+self.y**2+self.z**2)**(1/2)

if __name__ == "__main__":
    # N=int(input())
    # a=[]
    # max_lenght=0
    # sum_x=0
    # sum_y=0
    # sum_z=0
    # point=None
    # for i in range(N):
    #     x,y,z=map(int,input().split(','))
    #     v=Vector(x,y,z)
    #     sum_x+=v.x
    #     sum_y+=v.y
    #     sum_z+=v.z
    #     if v.lenght()>max_lenght:
    #         max_lenght=v.lenght()
    #         point=v
    # koord_centra_mass=Vector(int(sum_x/N),int(sum_y/N),int(sum_z/N))
    # print('Максимально удаленная точка', point)
    # print('Координаты центра тяжести данного множества точек', koord_centra_mass)

# Площадь параллелограмма и объём параллелепипеда
    vect_1=Vector(1,-1,2)
    vect_2=Vector(0,4,3)
    vect_3=Vector(3,2,-6)
    area=(vect_1@vect_2).lenght()
    print(area)
    volume=abs((vect_1@vect_2)*vect_3)
    print(volume)