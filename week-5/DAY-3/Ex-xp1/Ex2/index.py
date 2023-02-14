class Currency:

    def __init__(self, currency: str, amount: int) -> None:
        self.currency= currency
        self.amount=amount

    def __str__(self) -> str: # str(1) -> '1'
        return f'{self.amount} {self.currency}s'

    def __repr__(self) -> str: # more technical 
        return str(self) + ' ' + str(id(self))

    def __int__(self) -> int: # int('1') -> 1
        return self.amount


    def __add__(self, value) -> int: # __add__ <=> +
        if isinstance(value, int): # True if value is integer
            return self.amount + value
        if isinstance(value, Currency): # True if value is Currency object
            if self.currency == value.currency: # check if the same currency (dollar == dollar)
                return self.amount + value.amount
            else:
                raise TypeError(f"Cannot add not the same currecies {self.currency} and {value.currency}") 


    def __iadd__(self, value) -> None: # += 
        if isinstance(value, int): # check if value is integer
            self.amount += value
        if isinstance(value, Currency): # check if value is Currency object
            if self.currency == value.currency: # check if the same currency (dollar == dollar)
                self.amount += value.amount
            else:
                raise TypeError(f"Cannot add not the same currecies {self.currency} and {value.currency}") 
        return self

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
# '5 dollars'
print(int(c1))
# 5
print(repr(c1))
# 5 dollars 140486367023056
print(c1 + 5)
# 10
print(c1 + c2)

c1 += 5
print(c1.amount)
# 10 dollars

c1 + c3