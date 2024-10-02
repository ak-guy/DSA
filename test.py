s = 'A'
s.isupper()
class A:
    def __init__(self):
        self.x = 10

    def double(self):
        return 2 * self.x
    
def createClass(name):
    base = ()
    instanceVar = 10
    def double():
        return instanceVar * 2
    nameSpace = {'instanceVar': instanceVar, 'double': instanceVar}
    c = type(name, base, nameSpace)

    return c()

carObj = createClass('Car')
print(carObj.double(20))
