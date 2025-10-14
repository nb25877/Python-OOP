from dataclasses import dataclass
from typing import List, Optional
from abc import ABC, abstractmethod

@dataclass
class Product:
    id: int
    name: str
    description: str
    price: float
    stock: int

class ProductRepository(ABC):
    @abstractmethod
    def save(self, product: Product) -> bool:
        pass
    
    @abstractmethod
    def find_by_id(self, product_id: int) -> Optional[Product]:
        pass
    
    @abstractmethod
    def search(self, query: str) -> List[Product]:
        pass

class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self._repository = product_repository
    
    def add_product(self, product: Product) -> bool:
        return self._repository.save(product)
    
    def search_products(self, query: str) -> List[Product]:
        return self._repository.search(query)