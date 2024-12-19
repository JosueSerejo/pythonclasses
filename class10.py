class Product:
    def __init__(self, name):
        self.name = name
        self.price = 0
        self.stock = 0

    def buy(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            print(f"Você comprou {quantity} unidade(s) de {self.name}.")
        else:
            print(f"Estoque insuficiente para {self.name}. Disponível: {self.stock}")

    def restock(self, quantity):
        self.stock += quantity
        print(f"{quantity} unidade(s) de {self.name} foram adicionadas ao estoque.")

    def show_info(self):
        return f"Produto: {self.name}, Preço: R${self.price:.2f}, Estoque: {self.stock}"

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Produto {product.name} adicionado à loja.")

    def list_products(self):
         for product in self.products:
                print(product.show_info())



def main():
    # Criando alguns produtos
    p1 = Product("Notebook")
    p1.price = 3000
    p1.stock = 10

    p2 = Product("Mouse")
    p2.price = 50
    p2.stock = 100

    p3 = Product("Teclado")
    p3.price = 150
    p3.stock = 50

    # Criando a loja
    store = Store()

    # Adicionando produtos à loja
    store.add_product(p1)
    store.add_product(p2)
    store.add_product(p3)

    # Listando os produtos disponíveis
    store.list_products()

    # Comprando produtos
    p1.buy(3)  # Compra 3 notebooks
    p2.buy(150)  # Estoque insuficiente

    # Reabastecendo produtos
    p2.restock(50)

    # Listando os produtos novamente
    store.list_products()


if __name__ == '__main__':
    main()