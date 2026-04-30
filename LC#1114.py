# 1114. Print in Order
class Foo:
    def __init__(self):
        # pass  
        self.second_event = threading.Event()
        self.third_event = threading.Event()
    
    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.second_event.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        self.second_event.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.third_event.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.third_event.wait()
        printThird()
        
