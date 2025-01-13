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

class AddingStack(Stack):
    def __init__(self):
        self.__sum = 0
        
    def get_sum(self):
        return self.__sum
    def push(self, value):
        self.__sum += value
        Stack.push(self, value)
    def pop(self):
        value = Stack.pop(self)
        self.__sum -=value
        return val
        
            
stack_object = AddingStack()
for i in range(5):
    stack_object.push(i)
    
print(stack_object)
print(stack_object.get_sum())

for i in range(5):
    print(Stack_object.pop())
