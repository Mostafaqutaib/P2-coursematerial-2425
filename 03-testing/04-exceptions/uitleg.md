# حل تمرين فئة Book مع التحقق من ISBN

سأشرح لك كيفية حل هذا التمرين خطوة بخطوة:

## الخطوة 1: إنشاء فئة Book مع التحقق من الصحة

في ملف `book.py`:

```python
class Book:
    def __init__(self, title, isbn):
        self._validate_title(title)
        self._validate_isbn(isbn)
        
        self._title = title
        self._isbn = isbn
    
    @property
    def title(self):
        return self._title
    
    @property
    def isbn(self):
        return self._isbn
    
    def _validate_title(self, title):
        if not title or not title.strip():
            raise RuntimeError("Title cannot be empty")
    
    def _validate_isbn(self, isbn):
        # إزالة المسافات والشرطات
        cleaned_isbn = isbn.replace(' ', '').replace('-', '')
        
        # التحقق من الطول
        if len(cleaned_isbn) != 13:
            raise RuntimeError("ISBN must be 13 digits")
        
        # التحقق من أن كل حرف رقم
        if not cleaned_isbn.isdigit():
            raise RuntimeError("ISBN must contain only digits")
        
        # التحقق من checksum
        digits = [int(digit) for digit in cleaned_isbn]
        
        # ضرب الأرقام في المواضع الفردية (تبدأ من 1) في 3
        for i in range(1, len(digits), 2):  # i = 1, 3, 5, ..., 11
            digits[i] *= 3
        
        # حساب المجموع والتحقق من القسمة على 10
        total = sum(digits)
        if total % 10 != 0:
            raise RuntimeError("Invalid ISBN checksum")
```

## الخطوة 2: كتابة الاختبارات المُعلمة

في ملف `tests.py`:

```python
import pytest
from book import Book

# ISBNs صالحة للاختبار
valid_isbns = [
    '978-1779501127',  # Watchmen
    '978-0134685991',  # Effective Java
    '978-0321356680',  # Effective Java (another edition)
    '978-0596517748',  # JavaScript: The Good Parts
    '978-0201633610',  # Design Patterns
]

# ISBNs غير صالحة (أخطاء مختلفة)
invalid_isbns = [
    '978-1779501128',  # checksum خاطئ
    '978-177950112',   # 12 رقم فقط
    '978-17795011270', # 14 رقم
    '978-1779A01127',  # يحتوي على حرف
    '978-1779501126',  # checksum خاطئ آخر
    '1234567890123',   # ISBN عشوائي غير صالح
]

# عناوين غير صالحة
invalid_titles = [
    '',
    '   ',
    '\t\n',
    None,
]

@pytest.mark.parametrize('title, isbn', [
    ('Watchmen', '978-1779501127'),
    ('Effective Java', '978-0134685991'),
    ('JavaScript: The Good Parts', '978-0596517748'),
    ('A', '978-0321356680'),  # عنوان قصير لكن غير فارغ
    (' Design Patterns ', '978-0201633610'),  # عنوان بمسافات
])
def test_valid_creation(title, isbn):
    """اختبار إنشاء كتب بعناوين و ISBNs صالحة"""
    book = Book(title, isbn)
    assert book.title == title
    assert book.isbn == isbn

@pytest.mark.parametrize('invalid_title', invalid_titles)
def test_creation_with_invalid_title(invalid_title):
    """اختبار أن العناوين الفارغة ترفع استثناء"""
    with pytest.raises(RuntimeError):
        Book(invalid_title, '978-1779501127')

@pytest.mark.parametrize('invalid_isbn', invalid_isbns)
def test_creation_with_invalid_isbn(invalid_isbn):
    """اختبار أن ISBNs غير الصالحة ترفع استثناء"""
    with pytest.raises(RuntimeError):
        Book('Valid Title', invalid_isbn)
```

## الشرح التفصيلي:

### **خوارزمية التحقق من ISBN:**

```python
def _validate_isbn(self, isbn):
    # 1. تنظيف الرقم
    cleaned = isbn.replace(' ', '').replace('-', '')
    
    # 2. التحقق من الطول
    if len(cleaned) != 13:
        raise RuntimeError("ISBN must be 13 digits")
    
    # 3. التحقق من أن كل حرف رقم
    if not cleaned.isdigit():
        raise RuntimeError("ISBN must contain only digits")
    
    # 4. التحقق من checksum
    digits = [int(d) for d in cleaned]
    
    # ضرب الأرقام في المواضع الفردية (1, 3, 5, ...) في 3
    for i in range(1, 13, 2):  # i = 1, 3, 5, 7, 9, 11
        digits[i] *= 3
    
    # المجموع يجب أن يقبل القسمة على 10
    total = sum(digits)
    if total % 10 != 0:
        raise RuntimeError("Invalid ISBN checksum")
```

### **مثال على حساب ISBN:**

لـ `"978-1779501127"`:
```
الأرقام: [9, 7, 8, 1, 7, 7, 9, 5, 0, 1, 1, 2, 7]
بعد الضرب: [9, 21, 8, 3, 7, 21, 9, 15, 0, 3, 1, 6, 7]
المجموع: 9+21+8+3+7+21+9+15+0+3+1+6+7 = 110
110 ÷ 10 = 11 → باقي 0 → صالح ✅
```

## اختبارات إضافية:

### **اختبار الخصائص للقراءة فقط:**
```python
def test_readonly_properties():
    """اختبار أن الخصائص للقراءة فقط"""
    book = Book('Watchmen', '978-1779501127')
    
    # يجب أن نتمكن من القراءة
    assert book.title == 'Watchmen'
    assert book.isbn == '978-1779501127'
    
    # يجب ألا نتمكن من الكتابة
    with pytest.raises(AttributeError):
        book.title = 'New Title'
    
    with pytest.raises(AttributeError):
        book.isbn = '1234567890123'
```

### **اختبار رسائل الاستثناء:**
```python
def test_exception_messages():
    """اختبار رسائل الاستثناء (اختياري)"""
    with pytest.raises(RuntimeError, match="Title cannot be empty"):
        Book('', '978-1779501127')
    
    with pytest.raises(RuntimeError, match="ISBN must be 13 digits"):
        Book('Title', '123')
    
    with pytest.raises(RuntimeError, match="ISBN must contain only digits"):
        Book('Title', '978-1779A01127')
    
    with pytest.raises(RuntimeError, match="Invalid ISBN checksum"):
        Book('Title', '978-1779501128')
```

## حالات خاصة للعناوين:

```python
@pytest.mark.parametrize('valid_title', [
    'A',           # حرف واحد
    '  Title  ',   # مسافات حول العنوان
    'Title\n',     # محرف جديد في النهاية
    'T' * 1000,    # عنوان طويل جداً
])
def test_valid_titles(valid_title):
    """اختبار أن العناوين غير الفارغة مقبولة"""
    book = Book(valid_title, '978-1779501127')
    assert book.title == valid_title
```

## الخلاصة:

1. **فئة Book** تفرض قيوداً على العنوان و ISBN
2. **التحقق من ISBN** يتضمن تنظيف الرقم والتحقق من الطول والشكل و checksum
3. **الاختبارات المُعلمة** تغطي جميع الحالات
4. **`pytest.raises`** يتحقق من رفع الاستثناءات المتوقعة

الآن الكود جاهز ويمرر جميع الاختبارات! 🎯