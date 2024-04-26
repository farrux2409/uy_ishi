
class Fibonacci:
    def __init__(self, stop):
        self.prev = 0
        self.current = 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.prev < self.stop:
            result = self.prev
            self.prev, self.current = self.current, result + self.current
            return result
        else:
            raise StopIteration


fibonacci = Fibonacci(7)


while True:
    try:
        print(next(fibonacci))
    except StopIteration:
        break