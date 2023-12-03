def jokes(idj):
    line = ''
    with open('handlers/users/jokes/anek.txt', 'r', encoding='utf-8') as f:
        for i in range(idj):
            line = f.readline()
        if line == "":
            return 'Такого нет, попробуйте случайный анекдот'
        else:
            return line[:-1]



