from abc import abstractmethod, ABC

"""
1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
create an instance for each of the animal and call the unique method for it.
Determine if each of the animal is an instance of the Animals class
"""


class Animals:
    """
    Parent class, should have eat, sleep
    """

    def __init__(self, name, eat, sleep):
        self.name = name
        self.eat = eat
        self.sleep = sleep

    def eating(self):
        print(f'I am {self.name}, and I eating {self.eat}')

    def sleeping(self):
        print(f'I sleep {self.sleep} hours')


class Bird(Animals):
    """
    Some of the animal with 1-2 extra methods related to this animal
    """

    def __init__(self, name, eat, sleep, fly):
        super().__init__(name, eat, sleep)
        self.fly = fly

    def unique(self):
        print(f'Unique I can {self.fly}.')


class Wolf(Animals):
    def __init__(self, name, eat, sleep, yowl):
        super().__init__(name, eat, sleep)
        self.yowl = yowl

    def unique(self):
        print(f'Unique I say {self.yowl}.')


class Bee(Animals):
    def __init__(self, name, eat, sleep, take_honey_):
        super().__init__(name, eat, sleep)
        self.take_honey_ = take_honey_

    def unique(self):
        print(f'Unique I can {self.take_honey_}.')


class Elephant(Animals):
    def __init__(self, name, eat, sleep, nose):
        super().__init__(name, eat, sleep)
        self.nose = nose

    def unique(self):
        print(f'Unique I have {self.nose}.')


class Cow(Animals):
    def __init__(self, name, eat, sleep, milk):
        super().__init__(name, eat, sleep)
        self.milk = milk

    def unique(self):
        print(f'Unique I give {self.milk} .')


"""
1.
a.Create a new class Human and use multiple inheritance to create Centaur class, createan instance of Centaur class and
call the common method of these classes and unique.
"""


class Human:
    """
    Human class, should have eat, sleep, study, work
    """

    def __init__(self, name, eat, sleep, ):
        self.name = name
        self.eat = eat
        self.sleep = sleep

    def eating(self):
        print(f"{self.name} eating human's feed")

    def sleeping(self):
        print(f'{self.name} sleeps like human')

    def studying(self):
        print(f"{self.name} studying")

    def working(self):
        print(f"{self.name} working")


# 1
class Centaur(Animals, Human):
    """
    Centaur class should be inherited from Human and Animal and has unique method related to it.
    """

    def __init__(self, name, eat, sleep):
        super().__init__(name, eat, sleep)

    def rest(self):
        print(f'{self.name} catching butterfly')


# OUTPUT:

# I am Gosha, and I eating Feed
# I sleep 15 hours
# Gosha working
# Gosha studying

# 2
# class Centaur(Human, Animals):
#     """
#     Centaur class should be inherited from Human and Animal and has unique method related to it.
#     """
#
#     def __init__(self, name, eat, sleep):
#         super().__init__(name, eat, sleep)
#
#     def rest(self):
#         print(f'{self.name} catching butterfly')
#
#
# cent = Centaur('Gosha', 'Feed', 15)
# cent.eating()
# cent.sleeping()
# cent.working()
# cent.studying()

# OUTPUT:

# Gosha eating human's feed
# Gosha sleeps like human
# Gosha working
# Gosha studying


"""2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.
"""


# a.

class Person:
    """
    Make the class with composition.
    """

    def __init__(self):
        arm_1 = Arm('Left hand')
        arm_2 = Arm('Right hand')
        self.arms = [arm_1, arm_2]


class Arm:
    """
    Make the class with composition.
    """

    def __init__(self, hand):
        self.hand = hand


# b.

class CellPhone:
    """
    Make the class with aggregation
    """

    def __init__(self, screen):
        self.screen = screen


class Screen:
    """
    Make the class with aggregation
    """

    def __init__(self, screen_type):
        self.screen_type = screen_type


# 3.
class Profile:
    """
    Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
    Override a printable string representation of Profile class and return: list of the params mentioned above
    """

    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex
        self.about = [self.name, self.last_name, self.phone_number, self.address, self.email, self.birthday]

    def __str__(self):
        return f'About person: {self.about}'


"""
4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics 
and create an HPLaptop class by using your interface.
"""


class Laptop(ABC):
    @abstractmethod
    def Screen(self):
        raise NotImplementedError

    @abstractmethod
    def Keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def Touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def WebCam(self):
        raise NotImplementedError

    @abstractmethod
    def Ports(self):
        raise NotImplementedError

    @abstractmethod
    def Dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):
    def Screen(self):
        return 'HPLaptop screen'

    def Keyboard(self):
        return 'HPLaptop keyboard'

    def Touchpad(self):
        return 'HPLaptop touchpad'

    def WebCam(self):
        return 'HPLaptop webcam'

    def Ports(self):
        return 'HPLaptop ports'

    def Dynamics(self):
        return 'HPLaptop dynamics'

if __name__ == "__main__":

    bird = Bird('Chirik', 'worms', 3, 'fly')
    wolf = Wolf('Grey', 'meat', 5, 'YOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOWL')
    bee = Bee('Small Bee', 'flowers', 4, 'take honey')
    eleph = Elephant('Jack', 'grass', 8, 'long nose')
    cow = Cow('Milka', 'grass', 6, 'milk')

    a = (bird, wolf, bee, eleph, cow)

    for i in a:
        i.eating()
        i.sleeping()
        i.unique()

    for i in a:
        print(isinstance(i, Animals))

    cent = Centaur('Gosha', 'Feed', 15)

    cent.eating()
    cent.sleeping()
    cent.working()
    cent.studying()

    hand_ = Person()

    for hand_1_2 in hand_.arms:
        print(hand_1_2.hand)

    phone = Screen('IPS')
    my_phone = CellPhone(phone)

    print(phone.screen_type)
    print(my_phone.screen.screen_type)

    profile = Profile('Alex', 'B', 8965121321, "Evropeis'ka street", '123@i.ua', '01.01.2000', 21, 'male')
    print(profile)

    c = HPLaptop()
    b = [c.Screen(), c.Ports(), c.WebCam(), c.Dynamics(), c.Keyboard(), c.WebCam()]

    for i in b:
        print(i)
