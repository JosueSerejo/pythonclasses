class Person:
    def __init__(self):
        self.__name = ''
        self.__age = ''

    def get__name(self):
        print(self.__name)

    def get__age(self):
        print(self.__age)

    def set_name(self, new_name):
        self.__name = new_name

    def set_age(self, new_age):
        if new_age > 0:
         self.__age = new_age


def main():




if __name__ == '__main__':
 main()

    

    

    