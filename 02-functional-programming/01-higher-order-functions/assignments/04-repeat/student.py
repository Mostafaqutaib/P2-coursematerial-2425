def repeat(function, n):
    for i in range(n):
        function()

# مثال الاستخدام
def say_hello():
    print("Hello!")

# اختبار الدالة
repeat(say_hello, 5)