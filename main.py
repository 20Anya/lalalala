line1 = 0
content1 = ''
with open('1.txt', encoding='utf-8') as f1:
    for lines in f1:
        line1 += 1
        content1 += lines

line2 = 0
content2 = ''
with open('2.txt', encoding='utf-8') as f2:
    for lines in f2:
        line2 += 1
        content2 += lines

line3 = 0
content3 = ''
with open('3.txt', encoding='utf-8') as f3:
    for lines in f3:
        line3 += 1
        content3 += lines

max_ = max(line3, line2, line1)
min_ = min(line3, line2, line1)
l1 = str(line1)
l2 = str(line2)
l3 = str(line3)

if min_ == line1:
    with open('new.txt', 'w', encoding= 'utf-8') as f:
        f.write('1.txt\n' + l1 + '\n' + content1 + '\n')
elif min_ == line2:
    with open('new.txt', 'w', encoding= 'utf-8') as f:
        f.write('2.txt\n' + l2 + '\n' + content2 + '\n')
elif min_ == line3:
    with open('new.txt', 'w', encoding= 'utf-8') as f:
        f.write('3.txt\n' + l3 + '\n' + content3 + '\n')

if max_ != line1 and min_ != line1:
    with open('new.txt', 'a', encoding= 'utf-8') as f:
        f.write('1.txt\n' + l1 + '\n' + content1 + '\n')
elif max_ != line2 and min_ != line2:
    with open('new.txt', 'a', encoding= 'utf-8') as f:
        f.write('2.txt\n' + l2 + '\n' + content2 + '\n')
elif max_ != line3 and min_ != line3:
    with open('new.txt', 'a', encoding= 'utf-8') as f:
        f.write('3.txt\n' + l3 + '\n' + content3 + '\n')

if max_ == line1:
    with open('new.txt', 'a', encoding= 'utf-8') as f:
        f.write('1.txt\n' + l1 + '\n' + content1 + '\n')
elif max_ == line2:
    with open('new.txt', 'a', encoding= 'utf-8') as f:
        f.write('2.txt\n' + l2 + '\n' + content2 + '\n')
elif max_ == line3:
    with open('new.txt', 'a', encoding= 'utf-8') as f:
        f.write('3.txt\n' + l3 + '\n' + content3 + '\n')




