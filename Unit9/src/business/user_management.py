from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class User:
    id: int
    username: str
    email: str
    _password: str  # Hashed password
    
class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> bool:
        pass
    
    @abstractmethod
    def find_by_id(self, user_id: int) -> Optional[User]:
        pass
    
    @abstractmethod
    def find_by_username(self, username: str) -> Optional[User]:
        pass

class UserService:
    def __init__(self, user_repository: UserRepository):
        self._repository = user_repository
    
    def create_user(self, username: str, email: str, password: str) -> User:
        # Hash password and create user
        hashed_password = self._hash_password(password)
        user = User(id=0, username=username, email=email, _password=hashed_password)
        self._repository.save(user)
        return user
    
    def _hash_password(self, password: str) -> str:
        # Implementation of password hashing
        return f"hashed_{password}"