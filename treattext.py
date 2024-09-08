import os

def hide_cpf(cpf_or_cnpj):
    result = cpf_or_cnpj.replace('.','').replace('-','').replace('/','')

    if len(result) == 11:
        cpf_hidded = "{}.***.***-{}".format(result[0:3], result[-2:])
        return cpf_hidded
    else:
        return cpf_or_cnpj


def handle_input_file(path_file):
    result = False

    try:
        result = open(path_file, 'r', encoding='utf-8')
    except FileNotFoundError:
        print(f"\033[1;31mNão foi possível encontar o arquivo {path_file}.\033[0m")
        print(f"\033[1;31mCertifique-se de que o arquivo existe e está localizado dentro do diretório input\033[0m")
        return
    except PermissionError:
        print(f"\033[1;31mO arquivo {path_file} não possui permissão de escrita.\033[0m")
        return
    except Exception as e:
        print(f"\033[1;31mOcorreu um erro inesperado ao tentar ler o arquivo {path_file}: {e}\033[0m")
        return
    
    return result


def handle_output_file(path_file, content):
    try:
        with open(path_file, 'w', encoding='utf-8') as output_file:
            output_file.write(content)
            print(f"\033[1;32mO arquivo {path_file} foi criado com sucesso\!\033[0m")
    except PermissionError:
        print(f"\033[1;31mO arquivo {path_file} não possui permissão de escrita.\033[0m")
        return
    except Exception as e:
        print(f"\033[1;31mOcorreu um erro inesperado ao tentar ler o arquivo {path_file}: {e}\033[0m")
        return
    

def main():
    file_name = input('Informe o nome de arquivo de entrada: ')
    target    = input('Informe o nome do campo a ser tratado (Exemplo: CPF): ')
    input_folder = os.path.abspath('input')
    output_folder = os.path.abspath('output')
    input_file_path = os.path.join(input_folder, file_name)
    output_file_path = os.path.join(output_folder, file_name)

    input_file = handle_input_file(input_file_path)

    if input_file:
        # a partir da primeira linha do arquivo, cria uma lista com o nome dos campos (atributos)
        first_line = input_file.readline()
        head = first_line.split(';')
        # elimina a quebra de linha do último item da lista
        head[-1] = head[-1][0:-1]

        items = list()

        # variável onde será armazenado temporariamente o conteúdo que será salvo no arquivo de saída
        content = ""

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

        input_file.close()
            
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
        handle_output_file(output_file_path, content)


if __name__ == "__main__":
    main() 
