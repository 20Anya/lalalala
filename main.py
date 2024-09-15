import os

files = os.listdir('C:\\Users\\Пользователь\\Desktop\\lalalala\\txt')
rewrite = {}
for file in files:
    with open(f"C:\\Users\\Пользователь\\Desktop\\lalalala\\txt/{file}", encoding='utf-8') as f:
        read_f = f.readlines()
        count = len(read_f)
        rewrite[count] = f"{file}\n{count}\n{"\n".join(read_f)}\n"
with open('new.txt', 'w', encoding='utf-8') as w:
    for key in sorted(rewrite.keys()):
        w.write(rewrite[key])