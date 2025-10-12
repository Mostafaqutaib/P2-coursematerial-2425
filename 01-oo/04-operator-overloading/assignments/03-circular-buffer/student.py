# student.py

class CircularBuffer:
    """مخزن دائري ثابت الحجم يقوم بالكتابة فوق العناصر الأقدم عند الامتلاء."""
    def __init__(self, capacity):
        """تهيئة المخزن الدائري بسعة محددة."""
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        self.capacity = capacity            # السعة القصوى للمخزن
        self.buffer = [None] * capacity     # قائمة ثابتة الحجم لتخزين العناصر
        self.start = 0                      # مؤشر العنصر الأقدم (بداية المخزن)
        self.count = 0                      # عدد العناصر الحالية في المخزن

    def __len__(self):
        """إرجاع عدد العناصر المخزنة حالياً."""
        return self.count

    def add(self, value):
        """إضافة قيمة جديدة إلى المخزن الدائري.
        إذا كان المخزن ممتلئاً، سيتم الكتابة فوق أقدم عنصر."""
        if self.count < self.capacity:
            # لم يمتلئ المخزن بعد: أضف القيمة في نهاية الجزء المستخدم من القائمة
            index = (self.start + self.count) % self.capacity
            self.buffer[index] = value
            self.count += 1
        else:
            # المخزن ممتلئ: اكتب فوق أقدم عنصر ثم حرّك مؤشر البداية للأمام
            self.buffer[self.start] = value
            # تحديث مؤشر البداية (التخلص من أقدم عنصر)
            self.start = (self.start + 1) % self.capacity
            # يظل self.count ثابتاً عند السعة القصوى

    def __getitem__(self, index):
        """قراءة عنصر حسب الفهرس، بحيث يشير الفهرس 0 إلى أقدم عنصر."""
        # دعم الشرائح Slice (اختياري): يعيد قائمة من العناصر المطلوبة
        if isinstance(index, slice):
            start_idx, stop_idx, step = index.indices(self.count)
            return [self[i] for i in range(start_idx, stop_idx, step)]
        # التعامل مع الفهارس السالبة (مثل بايثون القائمة العادية)
        if index < 0:
            index = self.count + index
        # التحقق من النطاق المسموح
        if index < 0 or index >= self.count:
            raise IndexError("CircularBuffer index out of range")
        # حساب الفهرس الفعلي في القائمة الداخلية وإرجاع القيمة
        actual_index = (self.start + index) % self.capacity
        return self.buffer[actual_index]

    def __iter__(self):
        """إتاحة التكرار على العناصر من الأقدم إلى الأحدث."""
        for i in range(self.count):
            yield self.buffer[(self.start + i) % self.capacity]

    def __repr__(self):
        """تمثيل نصي لمحتويات المخزن الدائري."""
        if self.count == 0:
            return "CircularBuffer([])"
        elements = [self.buffer[(self.start + i) % self.capacity] for i in range(self.count)]
        return f"CircularBuffer({elements})"
