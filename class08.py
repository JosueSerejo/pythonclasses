class Queue:

    def __init__(self):
        self.__people = []

    def add_person(self, name):
        self.__people.append(name)

    def remove_person(self):
        if self.__people:
             removed = self.__people.pop(0)

        else:
            print("A fila está vazia. Ninguém para remover.")


    def show_queue(self):
        if self.__people:
            print("Fila atual:")
        for i, person in enumerate(self.__people, start=1):
                print(f"{i}. {person}")


def main():

    queue = Queue()

    # Adicionando pessoas à fila
    queue.add_person("Alice")
    queue.add_person("Bob")
 

    # Exibindo a fila
    queue.show_queue()

    # Removendo uma pessoa da fila
    queue.remove_person()
    queue.remove_person()
    # Exibindo a fila novamente
    queue.show_queue()





    # Tentando remover de uma fila vazia
    queue.remove_person()


if __name__ == '__main__':
    main()