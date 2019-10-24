class stack():
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def get_stack(self,items):
        return self.items
    def is_empty(self):
        return self.items == []
    

def check_balance(paren_string):
    s = stack()
    index = 0
    is_Balanced = True
    while index < len(paren_string) and is_Balanced :
        paren = paren_string[index]
        if paren in "{[(":
            s.push(paren)
        else:
            if s.is_empty():
                is_Balanced = False
            else:
                top = s.pop()
                if not match(top,paren):
                    is_Balanced = False
    
        index +=1
    
    if s.is_empty and is_Balanced:
        return True
    else:
        return False


def match(a,b):
    if a == '{' and b == "}":
        return True
    elif a=="[" and b== "]":
        return True
    elif a=="(" and b==")":
        return True


print(check_balance(""))
                
                


