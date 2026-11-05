from typing import override

from Product import Product

class PhysicalProduct(Product):
    def __init__(self, product_id: int, name: str, price: float, stock: int, weight: int) -> None:
        super().__init__(product_id=product_id, name=name, price=price, stock=stock)
        self.__weight = weight

    @override
    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight}")
