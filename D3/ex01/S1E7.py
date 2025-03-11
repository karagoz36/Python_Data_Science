from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Method to change the Baratheon character's state"""
        self.is_alive = False

    def __str__(self):
        """String representation of Baratheon character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs})"

    def __repr__(self):
        """Official string representation of Baratheon character."""
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Lannister class."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Method to change the Lannister character's state."""
        self.is_alive = False

    def __str__(self):
        """String representation of Lannister character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs})"

    def __repr__(self):
        """Official string representation of Lannister character."""
        return self.__str__()

    # decorator
    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Class method to create a Lannister character."""
        return cls(first_name, is_alive)
