class car :
    name = "faraari"
    model = "2026"
    engine = "v8"
    color = "red"
    def info(self):  # self keyword is used to access the attributes and methods of the class
        return(f"{self.name} is a {self.color} color car with a {self.engine} engine  and model is {self.model}")

a = car()
b = car()
a.color = "black"
a.engine = "v12"
print(a.info())

b.name = "mercedes"
b.color = "yellow"
print(b.info())