# What is abc in Python?

# abc stands for Abstract Base Class.

# It’s a module in Python used for creating abstract classes.

# Abstract classes allow you to define a template for other classes.

# They cannot be instantiated directly.

# They can include abstract methods, which must be implemented by child classes.

# Think of it like a blueprint:

# Blueprint (abstract class) → cannot build a house with just blueprint

# Builder (child class) → implements the blueprint

from abc import ABC, abstractmethod 

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

print("anandhu")
    
