class Money:
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency 
    
    @property
    def amount(self):
        return self.__amount
    @property
    def currency(self):
        return self.__currency
    
    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.__currency != other.currency:
            raise RuntimeError("Mismatched currencies!")
        return Money(self.__amount + other.amount, self.__currency)
    
    def __sub__(self, other):
        if not isinstance(other, Money):
           return NotImplemented
        if self.__currency != other.currency:
            raise RuntimeError("Mismatched currencies!")
        return Money(self.__amount - other.amount, self.__currency)

    def __mul__(self, k):
        if not isinstance(k, (int, float)):
            return NotImplemented
        return Money(self.__amount * k, self.__currency)

    def __rmul__(self, k):
        return self.__mul__(k)
    
tieneuro = Money(10, "EUR")

vijfeuro = Money(5, "EUR")
tweeeuro = Money(2,"EUR")
dinar = Money(3,"DIN")
print(3*Money(10,"USD"))
