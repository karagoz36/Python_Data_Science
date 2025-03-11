from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class: Cannot be instantiated, must be subclassed."""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Constructor for Character class."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Method to change the character's state"""
        self.is_alive = False


class Stark(Character):
    """Stark Class inheriting from Character class"""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Stark class"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Method to change the Stark character's state"""
        self.is_alive = False
