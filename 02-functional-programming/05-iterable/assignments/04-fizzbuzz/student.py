def fizz_buzz():
    n = 1
    while True:
        if n % 15 == 0:      # قابل للقسمة على 3 و 5
            yield 'fizzbuzz'
        elif n % 3 == 0:     # قابل للقسمة على 3 فقط
            yield 'fizz'
        elif n % 5 == 0:     # قابل للقسمة على 5 فقط
            yield 'buzz'
        else:                # غير قابل للقسمة على 3 أو 5
            yield str(n)
        n += 1