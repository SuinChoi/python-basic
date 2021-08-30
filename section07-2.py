# 다중상속
class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass
print(A.mro())

class B(Y, Z):
    pass

class C(B, A, Z):
    pass

print(C.mro())