import re


def baseN(num,b):
  return ((num == 0) and  "0" ) or ( baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])

def get(lst, n):
    return n < len(lst) and lst[n]

def decode(p, a, c, k):
    d = {}
    def e(c):
        if c < a:
            q = ""
        else:
            q = e(int(c/a))
        c = c % a
        if c > 35:
            return q + chr(c + 29)
        else:
            return q + baseN(c, 36)
    for i in range(c-1, -1, -1):
        d[e(i)] = get(k, i) or e(i)
    return re.sub(r"\b\w+\b", lambda _: d[_.string[_.start():_.end()]], p)

pattern = re.compile(r"\w=\w=.*?(\[\".*?\"\]).*?(\d+).*?(\d+).*?('.*?'\.split\('\|'\))")

def parse(s):
    s = s.replace("\\", "")
    p, a, c, k = pattern.search(s).groups()
    k = eval(k)
    result =  decode(p, int(a), int(c), k)
    result = eval(result)
    return result
