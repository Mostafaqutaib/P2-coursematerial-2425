def indices_of(xs, condition):
    lst = []
    for i, x in enumerate(xs):
        if condition(x):
            lst.append(i)
    return lst

def is_palindrome(string):
    return string == string[::-1]

def get_palindrome_indices(strings):
    return indices_of(strings, is_palindrome)

# اختبار المثال المطلوب
words = ["kayak", "never", "rotator", "palindrome"]
result = indices_of(words, is_palindrome)
print(result)  # [0, 2]

# أو باستخدام الدالة الأصلية
result2 = get_palindrome_indices(words)
print(result2)  # [0, 2]