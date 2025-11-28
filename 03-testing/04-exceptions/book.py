class Book:
    def __init__(self, title, isbn):
        self._validate_title(title)
        self._validate_isbn(isbn)
        
        self.__title = title
        self.__isbn = self._normalize_isbn(isbn)
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        """Setter للعنوان مع التحقق من الصحة"""
        self._validate_title(value)
        self.__title = value
    
    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self, value):
        """Setter للـ ISBN مع التحقق من الصحة"""
        self._validate_isbn(value)
        self.__isbn = self._normalize_isbn(value)
    
    def _validate_title(self, title):
        """يتحقق من أن العنوان غير فارغ"""
        if not title or not title.strip():
            raise RuntimeError("Title must not be empty")
    
    def _normalize_isbn(self, isbn):
        """يزيل المسافات والشرطات من ISBN"""
        return ''.join(char for char in isbn if char.isdigit())
    
    def _validate_isbn(self, isbn):
        """يتحقق من صحة ISBN"""
        normalized_isbn = self._normalize_isbn(isbn)
        
        # التحقق من الطول
        if len(normalized_isbn) != 13:
            raise RuntimeError("ISBN must contain exactly 13 digits")
        
        # التحقق من أن كل الحروف أرقام
        if not normalized_isbn.isdigit():
            raise RuntimeError("ISBN must contain only digits, spaces, or dashes")
        
        # التحقق من checksum
        if not self._is_valid_checksum(normalized_isbn):
            raise RuntimeError("Invalid ISBN checksum")
    
    def _is_valid_checksum(self, isbn_digits):
        """يتحقق من صحة checksum الـ ISBN"""
        digits = [int(digit) for digit in isbn_digits]
        
        # ضرب الأرقام في المواضع الفردية (تبدأ من 1) في 3
        for i in range(1, len(digits), 2):  # المواضع 1, 3, 5, ... (تبدأ من 0 في بايثون)
            digits[i] *= 3
        
        # حساب المجموع
        total_sum = sum(digits)
        
        # يجب أن يكون المجموع قابلاً للقسمة على 10
        return total_sum % 10 == 0
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.isbn}')"
    
    def __eq__(self, other):
        """يسمح بمقارنة الكتب بناءً على العنوان والـ ISBN"""
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.isbn == other.isbn