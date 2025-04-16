import re
T = open('TALpourTP2.txt',encoding='utf8')
texte = T.read()
for r in re.finditer(r'.{,75} est un .{,75}',texte,re.S):
	print(r.group(0))
	print('*' * 25)
