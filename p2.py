from abc import ABC, abstractmethod


# Abstract Class Person
class Person(ABC):

    def __init__(self):
        super().__init__()
        
    # abstract method for class person, must be implemented by child classes
    @abstractmethod
    def get_gender(self):
        pass


class Male(Person):
    
    def get_gender(self):
        print("Male")
    

class Female(Person):
    
    def get_gender(self):
        print("Female")


class Trans(Person):
    
    # Creating object of this class gives error, as abstract method is not defined
    # A class that is derived from an abstract class cannot be instantiated unless all of its abstract methods are overridden.
    pass

m = Male()
m.get_gender()
f = Female()
f.get_gender()
t = Trans() # This will give error