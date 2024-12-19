class Temperature:

    def __init__(self, celsius):
        self.__celsius = celsius

    def set_temperature(seçf, value):
        if value < -273.15:
            raise Exception(f'Temperatura inválida, meu chapa')
            self.__celsius = value



def main():

 temp1 = Temperature(75)
 print(temp1)
    

if __name__ == '__main__':
   main()