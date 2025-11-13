def find(collection, condition):
    """
    دالة عامة للبحث عن أول عنصر في القائمة يحقق شرط معين
    
    collection: القائمة المطلوب البحث فيها
    condition: دالة تأخذ عنصر وترجع True إذا حقق الشرط
    """
    for element in collection:
        if condition(element):
            return element
    return None

def has_consecutive_characters(string):
    """
    تتحقق إذا كانت السلسلة تحتوي على حرفين متتاليين متماثلين
    """
    for index in range(len(string) - 1):
        if string[index] == string[index + 1]:
            return True
    return False

def find_string_with_consecutive_characters(strings):
    """
    الدالة الأصلية معاد تنفيذها باستخدام الدالة العامة
    """
    return find(strings, has_consecutive_characters)