class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# Applying the metaclass to multiple classes
class SingletonClass1(metaclass=SingletonMeta):
    pass

class SingletonClass2(metaclass=SingletonMeta):
    pass

# Usage
instance1_a = SingletonClass1()
instance1_b = SingletonClass1()

instance2_a = SingletonClass2()
instance2_b = SingletonClass2()

print(instance1_a is instance1_b)  # True
print(instance2_a is instance2_b)  # True
print(instance1_a is instance2_a)  # False (they are different singleton classes)
