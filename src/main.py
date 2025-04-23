import re
T = open('TALpourTP2.txt',encoding='utf8')
texte = T.read()

#for r in re.finditer(r'.{,75} est un .{,75}',texte,re.S):
#	print(r.group(0))
#	print('*' * 25)

# Prépartation
    # 1. Pré-traitrement pour éviter couper les abréviations
texte = re.sub(r'\(abr. ([A-Z]+)\)', '(abr_ \\1)', texte)

    # 2. Divisier le texte en phrase
phrase = re.findall(r'([A-Z].+?[^.].(\.[ \n]|\n\n))', texte, re.S)

    # 3. Post-traitement pour restaurer les abréviations
for ph in phrase:
    p = ph[0]
    p = re.sub('abr_', 'abr.', p)
# Analyse
    # 4. Sortir les éléments définis et définitoires à l'aide de regex
    print(p.rstrip())
    print('\n')

# Présentation
    # 5. Impression des résultats sur la console avec contexte
