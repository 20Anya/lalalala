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




def process_files(directory, output_file):
    files = os.listdir(directory)
    rewrite = {}
    for file in files:
        with open(os.path.join(directory, file), encoding='utf-8') as f:
            read_f = f.readlines()
            count = len(read_f)
            rewrite[count] = f"{file}\n{count}\n{'\\n'.join(read_f)}\n"
    with open(output_file, 'w', encoding='utf-8') as w:
        for key in sorted(rewrite.keys()):
            w.write(rewrite[key])

process_files('C:\\Users\\Пользователь\\Desktop\\lalalala\\txt', 'new.txt')
