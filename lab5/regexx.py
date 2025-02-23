import re
txt = """
abbbb
a
abb
amkmdb
DUPLICATE
Branch of EUROPHARMA LLP Astana
BIN 080841000761
...
WEBKASSA.KZ
abs_abc
hello_world
hello word
helloWord
"""

pt1 = r"a[b]*"
mt1 = re.search(pt1, txt)
print(mt1.group())

pt2 = r"a[b]{2,3}"
mt2 = re.search(pt2, txt)
if pt2:
    print(mt2.group())

pt3 = r"\b[a-z]+_[a-z]+\b"
mt3 = re.findall(pt3,txt)
print(mt3)

pt4 = r"[A-Z][a-z]+"
mt4 = re.findall(pt4,txt)
print(mt4)

pt5 = r"a.*b"
mt5 = re.search(pt5, txt)
if pt5:
 print(mt5.group())

pt6 = r"[ ,.]"
replaced= re.sub(pt6, ":", txt)
print(replaced)

def snaketocamel(match):
    return match.group(2).upper()

pt7 = r"(_)([a-z])"
camelcase = re.sub(pt7, snaketocamel, txt)
print(camelcase)

pt8 = r"([A-Z])"
split = re.split(pt8, txt)
print(split)

pt9 = r"([a-z])([A-Z])"
formatted = re.sub(pt9, r"\1 \2", txt)
print(formatted)

pt10 = r"([a-z])([A-Z])"
sn = re.sub(pt10, r"\1_\2", txt).lower()
print(sn)