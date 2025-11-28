def matching_parentheses(string):
    count = 0
    for char in string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            # إذا أصبح العدد سالب، يعني هناك أقواس إغلاق بدون فتح
            if count < 0:
                return False
    # في النهاية، يجب أن يكون العدد صفر
    return count == 0