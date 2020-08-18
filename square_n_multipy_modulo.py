class SqMl():

    # author: "MrMariosfish"

    # constructor
    def __init__(self, base, exp, mod):
        '''
        __init__ Constructor of a class object.

        Arguments:
            base {Integer} -- Takes an integer as a base.
            exp {Integer} -- Takes an integer as an exponent of the base.
            mod {Integer} -- Takes an integer as the modulo parameter n. Default value is 1.
        '''
        self.base = int(base)
        self.exp = int(exp)
        self.mod = int(mod)

    # convert the exponent from decimal->binary
    def decToBin(self):
        '''
        decToBin Converts the exponent from decimal to binary.

        Returns:
            List -- List with binary digits of the exponent.
        '''
        decUpper = bin(self.exp)[2:]
        return list(decUpper)

    # calculates the remainder of the (base^exp) % n
    def sqAndMul(self):
        '''
        sqAndMul Calculates the remainder of the (base^exp) % n.

        Returns:
            Integer -- Returns the remainder of the (base^exp) % n.
        '''
        product = self.base
        for i in self.decToBin()[1:]:
            if i == "0":
                product = (product**2) % self.mod
            elif i == "1":
                product = (product**2 * self.base) % self.mod
        return product
