# 练习
class A():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

class B(A):
    def sub(self):
        return self.a - self.b

# a = B(5,6)
# b = a.sub()
# print(b)

if __name__ == '__main__':
    # a = A(5,6)
    # b = a.add()
    a = B(5,6)
    b = a.sub()
    print(b)

