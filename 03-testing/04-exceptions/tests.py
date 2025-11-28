import pytest
from book import Book

def test_title_setter():
    """يختتب إمكانية تعديل العنوان"""
    book = Book('Original Title', '9783088668645')
    
    # تعديل العنوان
    book.title = 'New Title'
    assert book.title == 'New Title'
    
    # التحقق من أن العنوان الجديد مضبوط
    assert book.title == 'New Title'

def test_title_setter_validation():
    """يختتب أن setter العنوان يتحقق من الصحة"""
    book = Book('Valid Title', '9783088668645')
    
    # محاولة تعيين عنوان فارغ (يجب أن يرفع خطأ)
    with pytest.raises(RuntimeError, match="Title must not be empty"):
        book.title = ''
    
    with pytest.raises(RuntimeError, match="Title must not be empty"):
        book.title = '   '
    
    # التأكد من أن العنوان الأصلي لم يتغير
    assert book.title == 'Valid Title'

def test_isbn_setter():
    """يختتب إمكانية تعديل ISBN"""
    book = Book('Test Book', '9783088668645')
    
    # تعديل ISBN
    book.isbn = '9786736371492'
    assert book.isbn == '9786736371492'
    
    # التأكد من أن ISBN الجديد مضبوط
    assert book.isbn == '9786736371492'

def test_isbn_setter_validation():
    """يختتب أن setter الـ ISBN يتحقق من الصحة"""
    book = Book('Test Book', '9783088668645')
    
    # محاولة تعيين ISBN غير صالح (يجب أن يرفع خطأ)
    with pytest.raises(RuntimeError, match="ISBN must contain exactly 13 digits"):
        book.isbn = '978308866864'  # 12 رقم فقط
    
    with pytest.raises(RuntimeError, match="Invalid ISBN checksum"):
        book.isbn = '9783088668646'  # checksum خاطئ
    
    with pytest.raises(RuntimeError, match="ISBN must contain only digits, spaces, or dashes"):
        book.isbn = '97830886686A5'  # يحتوي على حرف
    
    # التأكد من أن ISBN الأصلي لم يتغير
    assert book.isbn == '9783088668645'

def test_isbn_setter_with_formatting():
    """يختتب أن setter الـ ISBN ينظف التنسيق"""
    book = Book('Test Book', '9783088668645')
    
    # تعيين ISBN بتنسيق مختلف
    book.isbn = '978-3088-6686-45'
    assert book.isbn == '9783088668645'  # يجب أن يكون منظفاً
    
    book.isbn = '978 3088 6686 45'
    assert book.isbn == '9783088668645'  # يجب أن يكون منظفاً

def test_multiple_changes():
    """يختتب تعديل multiple properties"""
    book = Book('Initial Title', '9783088668645')
    
    # تغيير العنوان
    book.title = 'Updated Title'
    assert book.title == 'Updated Title'
    assert book.isbn == '9783088668645'  # لم يتغير
    
    # تغيير ISBN
    book.isbn = '9786736371492'
    assert book.title == 'Updated Title'  # لم يتغير
    assert book.isbn == '9786736371492'

def test_property_consistency():
    """يختتب أن الخصائص تبقى متسقة بعد التعديلات"""
    book = Book('Book One', '9783088668645')
    
    original_title = book.title
    original_isbn = book.isbn
    
    # تغيير وإعادة
    book.title = 'Temporary Title'
    book.isbn = '9786736371492'
    
    book.title = original_title
    book.isbn = original_isbn
    
    assert book.title == 'Book One'
    assert book.isbn == '9783088668645'