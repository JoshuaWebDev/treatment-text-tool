import os

def hide_cpf(cpf):
    cpf_hidded = "{}.***.***-{}".format(cpf[0:3], cpf[-2:])
    return cpf_hidded


def main():
    file_name = input('Informe o nome de arquivo de entrada: ')
    target    = input('Informe o nome do campo a ser tratado (Exemplo: CPF): ')
    input_folder = os.path.abspath('input')
    output_folder = os.path.abspath('output')
    input_file = open(input_folder + '/' + file_name, 'r', encoding='utf-8')
    output_file = open(output_folder + '/' + file_name, 'w', encoding='utf-8')
    
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

            # adiciona o contéudo de item ao dicionário dictio
            for i in range(len(item)):
                dictio[head[i]] = item[i]

            # adiciona o contéudo do dicionário dictio à lista items
            items.append(dictio)
            
            #cpf = temp[2].strip()
            #cpf = cpf[0:3] + ".***.***-" + cpf[-2:]

    input_file.close()

    # organiza o conteúdo que será salvo no arquivo de saída
    # na pasta output dentro da variável content
    content = ""

    # formata o cabeçalho (1ª linha do arquivo)
    for h in head:
        if h == head[-1]:
            content += "{}\n".format(h)
        else:
            content += "{};".format(h)

    # formata o contéudo após o cabeçalho (2ª linha em diante)
    for item in items:
        for h in head:
            # se o cabeçalho for igual ao target informado
            # é realizado o tratamento deste campo
            if h == target:
                content += hide_cpf(item[h])
            else:
                content += item[h]

            # se for o último item, adiciona uma quebra de linha
            # senão, adiciona o separador (',', ';', etc)
            if h == head[-1]:
                content += "\n"
            else:
                content += ";"

    # pega o conteúdo da variável content e salva no arquivo, após serem tratados os dados
    output_file.write(content)

    output_file.close()

    print("Arquivo criado com sucesso em {}".format(output_file.name))

if __name__ == "__main__":
    main() 
