class Employee:

    total_employees = 0

    def __init__(self, name, salary = 1250):
        self.name = name
        self.salary = salary

        Employee.total_employees += 1


    def show_total_employees():
        print(f'total de funcionários: {Employee.total_employees}')

    def __str__(self):
        return (f' Nome: {self.name}, Salário: R$ {self.salary}')

def main():

    fun1 = Employee('João', 3000)
    print(fun1)

    fun2 = Employee('Ana')
    print(fun2)

    Employee.show_total_employees()


if __name__ == '__main__':
    main()


