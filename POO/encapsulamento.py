class Foo:
    def __init__(self) -> None:
        self.public = 'Isso é público'
        self._protected = '[ _ ] Isso é protegido e só pode ser usado na classe e suas subclasses'
        self.__private = '[ __ ] Isso é privado e só pode ser usado nesta classe'

f = Foo()

print(f.public)
print(f._protected)        
#print(f.__private)