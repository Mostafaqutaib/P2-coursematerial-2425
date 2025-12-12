

الحل: بدل ما نطابق “كلمة + نفس الكلمة مرة واحدة”، نطابق “كلمة + (تكرارها واحد أو أكثر)” باستخدام `+` على المجموعة الثانية.

## ✅ regex الصحيح

```regex
(\b\w+\b)(\s+\1)+
```

* `(\b\w+\b)` يمسك الكلمة (group 1)
* `(\s+\1)+` يمسك تكرارها مرة أو أكثر (يعني 2 مرات، 3 مرات، 10 مرات…)

والاستبدال يكون بكلمة واحدة فقط: `\1`

## ✅ الحل النهائي (ستايل الكورس)

```python
import re

def remove_repeated_words(string: str) -> str:
    """Remove consecutive duplicated words from string."""
    return re.sub(r'(\b\w+\b)(\s+\1)+', r'\1', string)
```

### هذا يصلّح حالتك:

* `"a a a a b"` → `"a b"` ✅
* `"yes yes yes"` → `"yes"` ✅
* `"this this is is good"` → `"this is good"` ✅

إذا تبينها تكون **case-insensitive** (مثلاً "Hello hello") قولي وأضيف `flags=re.IGNORECASE`.
