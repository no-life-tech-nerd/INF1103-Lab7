class Product:
    def __init__(self, product_id: int, name: str, price: float, stock: int):
        self.__product_id = int(product_id)
        self.__name = str(name)
        self.__price = float(price)
        self.__stock = int(stock)

    def get_product_id(self) -> int:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock

    def update_stock(self, new_quantity: int) -> None:
        self.__stock = new_quantity

    def display_information(self) -> None:
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${round(self.__price, 2):.2f} | Stock: {self.__stock}")
