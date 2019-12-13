import re

# ^开头字符必须以后面字符开头
# .代表任意字符
# *代表可以重复任意多次
# $结尾字符必须以后面字符结尾
# ?非贪婪匹配
# +出现至少一次-
# {2}{2,}{2,5}前面字符出现次数
# |或
# []里面字符只要满足一个都可以 可以使区间 [^1]{9} 不等于1,9次
# \s空格(一个) \S不是空格(一个) \w [a-zA-Z0-9-] \W
# [\u4e00-\u9FA5]   汉子
# \d 数字
line = "xxx出生于2019年06月01日"
line = "xxx出生于2019/06/01"
line = "xxx出生于2019.06.01"
line = "xxx出生于2019-06-01"
regex_str = ".*出生于(\d{4})[年/\-\/\.](\d{1,2})[月/\-\/\.](\d{1,2})"
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))
    print(match_obj.group(2))
    print(match_obj.group(3))
