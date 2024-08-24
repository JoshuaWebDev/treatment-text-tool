import os

def main():
    input_file = open('input/test.csv', 'r', encoding='utf-8')
    output_file = open('output/test.csv', 'w', encoding='utf-8')

    first_line = input_file.readline()
    head = first_line.split(';')
    first_line = head[0] + ";" + head[1] + ";" + head[2].strip()

    items = list()
    items.append(first_line)

    for line in input_file:
        if line != first_line:
            temp = line.split(';')
            cpf = temp[2].strip()
            cpf = cpf[0:3] + ".***.***-" + cpf[-2:]
            item = temp[0] + ";" + temp[1] + ";" +  cpf
            items.append(item)

    input_file.close()

    for item in items:
        output_file.write(item + "\n")

    print("Arquivo criado com sucesso em", output_file.name)

if __name__ == "__main__":
    main() 
