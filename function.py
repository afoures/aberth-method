class   Function():
    def __init__(self, coef):
        self.__coef = {key: complex(value) for key, value in coef.items() if value != 0}

    @property
    def degree(self):
        return len(self.__coef) - 1

    @property
    def coef(self):
        indexes = list(self.__coef.keys())
        index = min(indexes)
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
        coef = self.coef
        dcoef = []
        for i, c in enumerate(coef):
            dcoef.append(c*i)
        return dcoef[1:]

    def image(self, x):
        return sum(coef*(pow(x, i)) for i, coef in enumerate(self.coef))

    def derivative(self, x):
        return sum(coef*(pow(x, i)) for i, coef in enumerate(self.dcoef))
