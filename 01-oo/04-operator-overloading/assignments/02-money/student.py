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
        if self.__currency != other.currency:
            raise ValueError("Mismatched currencies!")
        return Money(self.__amount + other.amount, self.__currency)
    
    def __sub__(self, other):
        if self.__currency != other.currency:
            raise ValueError("Mismatched currencies!")
        return Money(self.__amount - other.amount, self.__currency)

    def __mul__(self, k):
        return Money(self.__amount * k, self.__currency)
    def __rmul__(self, k):
        return self.__mul__(k,(int,float))
tieneuro = Money(10, "EUR")

vijfeuro = Money(5, "EUR")
tweeeuro = Money(2,"EUR")
dinar = Money(3,"DIN")
Money(10,"USD") *3
