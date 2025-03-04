import  products

class Store:
    def __init__(self, list_of_products):
        self.list_of_products = list_of_products


    def add_product(self, product):
        '''Adds a product to the list of products'''
        self.list_of_products.append(product)


    def remove_product(self, product):
        '''Removes a product from the list of products'''
        self.list_of_products.remove(product)


    def get_total_quantity(self):
        '''Returns the total quantity of all products'''
        return sum([product.get_quantity() for product in self.list_of_products])


    def order(self, shopping_list):
        '''Orders a list of products'''
        total_price = 0
        for product, quantity in shopping_list.items():
            for p in self.list_of_products:
                if p.name == product:
                    total_price += p.buy(quantity)
        return total_price



