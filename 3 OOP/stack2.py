import sys

class Stack:
    def __init__(self):
        self.size = 0
        self.__stack_list = []

def push(self):
    self.__stack_list.append(value)
    self.size += 1
    
def pop(self):
        value = self.__stack_list[-1]
        del self.__stack_list[-1]
        self.size -=1
        return value
        
def __str__(self):
    print(f"Pila = , {self.__stack_list}")

stack_object= Stack()
stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())

try:
    print(len(stack_object.stack_list))
except AttributeError:
    print("El atributo es privado")
    sys.exit(1)