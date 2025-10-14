from abc import ABC, abstractmethod
from typing import List
from dataclasses import dataclass

@dataclass
class Notification:
    user_id: int
    message: str
    type: str

class NotificationStrategy(ABC):
    @abstractmethod
    def send(self, notification: Notification) -> bool:
        pass

class EmailNotification(NotificationStrategy):
    def send(self, notification: Notification) -> bool:
        print(f"Sending email to user {notification.user_id}: {notification.message}")
        return True

class SMSNotification(NotificationStrategy):
    def send(self, notification: Notification) -> bool:
        print(f"Sending SMS to user {notification.user_id}: {notification.message}")
        return True

class NotificationService:
    def __init__(self):
        self._strategies: List[NotificationStrategy] = []
    
    def add_strategy(self, strategy: NotificationStrategy):
        self._strategies.append(strategy)
    
    def notify(self, notification: Notification):
        for strategy in self._strategies:
            strategy.send(notification)