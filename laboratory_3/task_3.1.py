# создайте произвольный текстовый файл с несколькими строками произвольного текста

with open("text.txt", "w") as file:
    file.write(" A \n")
    file.write("    B  A  B    \n")
    file.write(" B    AAA    B \n")
    file.write("  B  AAAAA B   \n")
    file.write("    AAAAAAA    \n")
    file.write("   AAAAAAAAA   \n")
    file.write(" AAAAAAAAAAAAA \n")
    file.write("abc\n")

# Выведите в консоль строки файла, удалив лишние пробелы в начале и конце строк, если они есть

with open('text.txt', 'r') as file:
    for line in file:
        start=0
        while line[start]==' ':
            start+=1
        finish=len(line[start::])-2+start
        if finish-start>0:
            while line[finish] == ' ':
                finish -= 1
        print(line[start:finish+1])