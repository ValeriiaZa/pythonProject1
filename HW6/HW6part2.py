

class Frange:
    def __init__(self, *args):
        if len(args) == 1:
            self.start = 0
            self.step = 1
            self.end = args[0]
        elif len(args) == 2:
            self.start = args[0]
            self.step = 1
            self.end = args[1]
        else:
            self.start = args[0]
            self.step = args[2]
            self.end = args[1]

    def __next__(self):
        if self.step > 0:
            if self.start + self.step >= self.end+self.step:
                raise StopIteration
            result = self.start
            self.start += self.step
            return result
        elif self.step < 0:
            if self.start + self.step > self.end + self.step:
                result = self.start
                self.start += self.step
                return result
            raise StopIteration

    def __iter__(self):
        return self


frange = Frange

for i in frange(5):
    print(i)
