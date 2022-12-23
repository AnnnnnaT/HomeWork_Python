
with open('file1.txt', 'r', encoding='UTF-8') as data, open('file.txt', 'w', encoding='UTF-8') as new_data:
    for line in data:
        new_data.writelines(line)

with open('file2.txt', 'r', encoding='UTF-8') as data, open('file.txt', 'a', encoding='UTF-8') as new_data:
    for line in data:
        new_data.writelines(line)