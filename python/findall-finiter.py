
import re

pattern=r"(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])"

txt = raw_input()

result = map(lambda x: x.group(),re.finditer(pattern,txt))

if not result:
    print -1
else:
    for x in result:
        print x


