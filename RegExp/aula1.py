# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto
import re

# findall search sub compile
string = 'Este e um teste de expressoes regulares.'
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'ABCD', string))

# Exemplo de compile
regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('DEF', string))