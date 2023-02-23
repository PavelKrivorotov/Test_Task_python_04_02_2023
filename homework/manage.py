from typing import Callable, Iterable, Any


class Person: pass

class Person:
    def __init__(self, iam: bool, name: str):
        self.iam = iam
        self.name = name

    @property
    def iam(self):
        return self._iam

    @iam.setter
    def iam(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError(f"Input argument is not a 'bool'!")
        self._iam = value

    @iam.deleter
    def iam(self):
        del self._iam

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise ValueError(f"Input argument is not a 'str'!")
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    @staticmethod
    def check_person(func: Callable[[Person, Any], None]) -> Callable[[Person, Any], None]:
        def wraper(*args: Iterable, **kwargs: Any) -> None:
            try:
                person: Person = args[0]
            except IndexError:
                person: Person = kwargs.get('person', None)

            if not isinstance(person, Person):
                raise TypeError("The 'person' object is not isinstanse 'Person'!")
            
            if getattr(person, '_iam') == False:
                raise ValueError("The attribute '_iam' is False!")

            return func(*args, **kwargs)
        return wraper


@Person.check_person
def welcome(person: Person, message: str = "Ok-ok") -> None:
    print(f"Welcome {person.name}")
    print(f"Message is {message}")


if __name__ == "__main__":
    # 
    # Check Person: __init__, getter, setter, deleter methods:
    # 
    person1 = Person(True, "Test1")

    # Check exists '_iam' and '_name' attributes:
    # 
    assert hasattr(person1, "_iam") == True
    assert hasattr(person1, "_name") == True

    # Check types of '_iam' and '_name' attributes:
    # 
    assert isinstance(getattr(person1, "_iam"), bool) == True
    assert isinstance(getattr(person1, "_name"), str) == True

    # Check getter methods:
    # 
    assert person1.iam == True
    assert person1.name == "Test1"

    # Check setter methods:
    # 
    person1.iam = False
    person1.name = "New"

    assert person1.iam == False
    assert person1.name == "New"

    # Check input valid type to set new '_iam' value:
    # 
    try:
        person1.iam = "Bug"
        assert False, "Set argument is not a 'bool'!"
    except ValueError:
        pass

    # Check input valid type to set new '_name' value:
    # 
    try:
        person1.name = True
        assert False, "Set argument is not a 'str'!"
    except ValueError:
        pass

    # Check deleter methods:
    # 
    del person1.iam
    del person1.name

    assert hasattr(person1, "_iam") == False
    assert hasattr(person1, "_name") == False


    # 
    # Check 'check_person' decorator:
    # 
    func = lambda person, *args, **kwargs: None
    try:
        Person.check_person(func)(None)
        assert False, "Give positional argument 'person': None, but check_person not raise ValueError!"
    except TypeError:
        pass

    person2 = Person(True, "Test2")
    del person2.iam
    func = lambda person, *args, **kwargs: person2
    try:
        Person.check_person(func)(person2)
        assert False, "Give positional argument 'person' without attribute '_iam', but not raise Attribute error!"
    except AttributeError:
        pass

    person3 = Person(False, "Test3")
    func = lambda person, *args, **kwargs: person3
    try:
        Person.check_person(func)(person3)
        assert False, "Give positional argument 'person' with attribute '_iam' is False, but not raise Attribute error!"
    except ValueError:
        pass

    person4 = Person(True, "Test4")
    func = lambda person, *args, **kwargs: person4
    try:
        Person.check_person(func)(person4)
    except TypeError:
        assert False, "Give positional argument 'person': Person, but check_person raise ValueError!"
    except AttributeError:
        assert False, "Give positional argument 'person' with attribute '_iam', but raise Attribute error!"
    except ValueError:
        assert False, "Give positional argument 'person' with attribute '_iam' is True, but raise Attribute error!"


    # 
    # Check 'welcome' function for person2 with '_iam' attribute is True:
    # 
    person5 = Person(True, "Test5")
    try:
        welcome(person = person5, message="Lol-lol")
    except Exception:
        assert False, "The person5 have '_iam' is True, but check_person raise Exception!"


    # 
    # Check 'welcome' function for person3 with '_iam' attribute is False:
    # 
    person6 = Person(False, "Test6")
    try:
        welcome(person6)
        assert False, "The person6 have '_iam' is False, but check_person not a raise Exception!"
    except Exception:
        pass
