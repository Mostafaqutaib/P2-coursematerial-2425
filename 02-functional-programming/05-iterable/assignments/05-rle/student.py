def rle_encode(data):
    """تشفر البيانات باستخدام خوارزمية RLE"""
    if not data:
        return
    
    iterator = iter(data)
    current_char = next(iterator)
    count = 1
    
    for char in iterator:
        if char == current_char:
            count += 1
        else:
            yield (current_char, count)
            current_char = char
            count = 1
    
    yield (current_char, count)

def rle_decode(data):
    """تفك تشفير البيانات المشفرة بـ RLE"""
    for char, count in data:
        for _ in range(count):
            yield char