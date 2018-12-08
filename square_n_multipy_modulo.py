class SqMl():

    """This is an implementation of the square and multiply algorithm in some 
    modulo n in Python. The general form is ' (b^exp) % n '.\n
    base--> Takes an integer as a base.\n
    exp--> Takes an integer as an exponent of the base.\n
    mod--> Takes an integer as the modulo parameter n. Default value is 1.\n
    This algorithm is very usefull in cryptography and has O(log n) 
    computational time for big exponents."""

    @author: "MrMariosfish"
    # constructor
    def __init__(self, base, exp, mod):
        self.base = int(base)
        self.exp = int(exp)
        self.mod = int(mod)

    # convert the exponent from decimal->binary
    def decToBin(self):
        decUpper = bin(self.exp)[2:]
        return list(decUpper)

    # calculates the remainder of the (base^exp) % n
    def sqAndMul(self):
        product = self.base
        for i in self.decToBin()[1:]:
            if i == "0":
                product = (product**2) % self.mod
            elif i == "1":
                product = (product**2 * self.base) % self.mod
        return product
