from threading import Lock, Thread

class Singleton(type):
    _classObj = None
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock: 
            if not isinstance(cls._classObj, cls):
                obj = super().__call__(*args, **kwargs)
                cls._classObj = obj
        return cls._classObj
    
class Test(metaclass=Singleton):
    def __init__(self, x):
        self.x = x

    
def createTest(x):
    obj = Test(x)
    print(obj.x)

t1 = Thread(target=createTest, args=(110,))
t2 = Thread(target=createTest, args=(2000,))

t1.start()
t2.start()

t1.join()
t2.join()

print(type(Test))