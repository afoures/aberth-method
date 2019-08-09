"""
    function module
    
###############################################################################
    
    This module contains a Function class used to represent a polynomial.
    
    It can be used with the aberthMethod module to find a polynomial's roots.
    
"""


class   Function():
    """
    Function object that can represent a polynomial.

    Parameters
    ----------
    coef: a dict objet that represent the coeficients of a polynomial, with
        exponantiation as key and coeficient as value.

    Property
    ----------
    degree
    coef
    dcoef

    Methods
    ----------
    image
    derivative

    """

    def __init__(self, coef):
        """print(coef, min(coef), max(coef))
        keys = range(min(coef), max(coef)+1)
        self.__coef= {}
        for key in keys:
            self.__coef[key] = complex(coef[key]) if key in coef else complex(0)"""
        self.__coef = {key: complex(value) for key, value in coef.items() if value != 0}
        print(self.__coef)
            
    @property
    def degree(self):
        """
        Return the degree of the polynomial.
        """
        return max(self.__coef)

    @property
    def coef(self):
        """
        Return a list object composed with all the polynomial's coeficients
        shifted to have them starting with first exponantiation as 0.
        Exponantiation for each is now the index in the list.
        """
        indexes = list(self.__coef.keys())
        index = min(indexes) if min(indexes) < 0 else 0
        coef = []
        remains = len(indexes)
        while remains > 0:
            if index in self.__coef:
                remains -= 1
            coef.append(self.__coef.setdefault(index, 0))
            index += 1
            
        return coef

    @property
    def dcoef(self):
        """
        Return a list object composed with all the polynomial derivative's 
        coeficients shifted to have them starting with first exponantiation
        as 0.
        Exponantiation for each is now the index in the list.
        """
        coef = self.coef
        dcoef = []
        for i, c in enumerate(coef):
            dcoef.append(c*i)
        return dcoef[1:]

    def image(self, x):
        """
        Return the image of the polynomial for 'x'.
        """
        return sum(coef*(pow(x, i)) for i, coef in enumerate(self.coef))

    def derivative(self, x):
        """
        Return the derivative of the polynomial for 'x'.
        """
        return (self.image(x + 1.e-12) - self.image(x)) / 1.e-12
