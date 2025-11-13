def merge_dictionaries(d1, d2, merge_function):
    result = {}
    
    # ننسخ كل عناصر d1
    for key, value in d1.items():
        result[key] = value
    
    # ندمج مع d2
    for key, value in d2.items():
        if key in result:
            # إذا كان المفتاح موجود في كلا القاموسين، نستخدم دالة الدمج
            result[key] = merge_function(result[key], value)
        else:
            # إذا كان المفتاح موجود فقط في d2، نضيفه
            result[key] = value
    
    return result