import os

def main():
    input_file = open('input/test.csv', 'r', encoding='utf-8')
    output_file = open('output/test.csv', 'w', encoding='utf-8')
    
    # define o campo que será tratado
    target = 'CPF'

    # a partir da primeira linha do arquivo, cria uma lista com o nome dos campos (atributos)
    first_line = input_file.readline()
    head = first_line.split(';')
    head[-1] = head[-1][0:-1] # elimina a quebra de linha do último item da lista (\n)

    items = list()

    # adiciona cada um dos itens à lista items, de acordo com seu respectivo campo (atributo)
    for line in input_file:
        if line != first_line:
            temp = line.split(';')
            item = list()
            # trata os dados, eliminando espaços ao redor e quebra de linha (\n)
            # em seguida salva o item (tratado) na lista item
            for t in temp:
                item.append(t.strip())

            dictio = {} # cria um dicionário vazio
            for i in range(len(item)):
                dictio[head[i]] = item[i]
            items.append(dictio)
            
            #cpf = temp[2].strip()
            #cpf = cpf[0:3] + ".***.***-" + cpf[-2:]

    input_file.close()

    #    print(repr(items))

    content = ""

    counter = 0

    while counter < len(head):
        content += head[counter]
        if (counter != len(head) - 1):
            content += ";"
        counter += 1

    content += "\n"

    for item in items:
        content += "{:2};{};{}\n".format(item['ID'], item['NOME'], item['CPF'])

    # pega o conteúdo da lista items e salva no arquivo, após serem tratados os dados
    output_file.write(content)

    output_file.close()

    print("Arquivo criado com sucesso em {}".format(output_file.name))

if __name__ == "__main__":
    main() 
