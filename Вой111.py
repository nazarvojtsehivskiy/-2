class Humanity:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def work(self):
        print("Людина працює")


class Programmer(Humanity):
    def __init__(self, name, age, language):
        super().__init__(name, age)
        self._language = language

    def work(self):
        print(f"Програміст пише код на {self._language}")


# головна частина програми
human = Humanity("Іван", 20)
programmer = Programmer("Марія", 22, "Python")

human.work()
programmer.work()
