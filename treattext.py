import os
from os.path import split

input_folder = os.path.abspath('input')
output_folder = os.path.abspath('output')

def remove_space_of_namefile(file_name):
    return file_name.replace(" ", "_")


def remove_dash_of_namefile(file_name):
    return file_name.replace("-", "")


def remove_extra_underlines_of_namefile(file_name):
    return file_name.replace("__", "_")


def remove_accents_of_namefile(file_name):
    new_filename = file_name.replace("Á", "A")
    new_filename = new_filename.replace("À", "A")
    new_filename = new_filename.replace("Ã", "A")
    new_filename = new_filename.replace("Â", "A")
    new_filename = new_filename.replace("Ä", "A")
    new_filename = new_filename.replace("É", "E")
    new_filename = new_filename.replace("È", "E")
    new_filename = new_filename.replace("Ê", "E")
    new_filename = new_filename.replace("Ë", "E")
    new_filename = new_filename.replace("Í", "I")
    new_filename = new_filename.replace("Ì", "I")
    new_filename = new_filename.replace("Î", "I")
    new_filename = new_filename.replace("Ï", "I")
    new_filename = new_filename.replace("Ó", "O")
    new_filename = new_filename.replace("Ò", "O")
    new_filename = new_filename.replace("Õ", "O")
    new_filename = new_filename.replace("Ô", "O")
    new_filename = new_filename.replace("Ö", "O")
    new_filename = new_filename.replace("Ú", "U")
    new_filename = new_filename.replace("Ù", "U")
    new_filename = new_filename.replace("Û", "U")
    new_filename = new_filename.replace("Ü", "U")
    return new_filename


def format_filename(file_name):
    newfile_name = remove_space_of_namefile(file_name)
    newfile_name = remove_dash_of_namefile(newfile_name)
    newfile_name = remove_extra_underlines_of_namefile(newfile_name)
    newfile_name = remove_accents_of_namefile(newfile_name)

    input_file_path = os.path.join(input_folder, file_name)
    output_file_path = os.path.join(input_folder, newfile_name)

    try:
        os.rename(input_file_path, output_file_path)
        print(file_name + " has been renamed to " + newfile_name + " successfully.")

    except IsADirectoryError:
        print(file_name + " is a file but " + newfile_name + " is a directory.")

    except NotADirectoryError:
        print(file_name + " is a directory but " + newfile_name + " is a file.")

    except PermissionError:
        print("Operation not permitted.")

    except FileNotFoundError:
        print("File not found.")

    except OSError as error:
        print(error)


def remove_extra_words_in_filename(file_name, extra_word):
    newfile_name = file_name.replace(extra_word, "")

    input_file_path = os.path.join(input_folder, file_name)
    output_file_path = os.path.join(input_folder, newfile_name)

    try:
        os.rename(input_file_path, output_file_path)
        print(file_name + " has been renamed to " + newfile_name + " successfully.")

    except IsADirectoryError:
        print(file_name + " is a file but " + newfile_name + " is a directory.")

    except NotADirectoryError:
        print(file_name + " is a directory but " + newfile_name + " is a file.")

    except PermissionError:
        print("Operation not permitted.")

    except FileNotFoundError:
        print("File not found.")

    except OSError as error:
        print(error)


def replace_part_of_namefile(file_name, part_to_remove, part_to_add):
    newfile_name = file_name.replace(part_to_remove, part_to_add)

    input_file_path = os.path.join(input_folder, file_name)
    output_file_path = os.path.join(input_folder, newfile_name)

    try:
        os.rename(input_file_path, output_file_path)
        print(file_name + " has been renamed to " + newfile_name + " successfully.")

    except IsADirectoryError:
        print(file_name + " is a file but " + newfile_name + " is a directory.")

    except NotADirectoryError:
        print(file_name + " is a directory but " + newfile_name + " is a file.")

    except PermissionError:
        print("Operation not permitted.")

    except FileNotFoundError:
        print("File not found.")

    except OSError as error:
        print(error)


def format_csv(file_name):
    separator = input("Informe o tipo de separador (vírgula, ponto e vírgula, etc): ")
    input_file_path = os.path.join(input_folder, file_name)
    output_file_path = os.path.join(output_folder, file_name)

    input_file = handle_input_file(input_file_path)

    if input_file:
        # a partir da primeira linha do arquivo, cria uma lista com o nome dos campos (atributos)
        first_line = input_file.readline()
        head = first_line.split(separator)

        for line in input_file:
            if line != first_line:
                temp = line.split(';')
                if len(temp) < len(head):
                    temp[-1] = temp[-1][0:-1]

                print(temp)
                print("FALTA TERMINAR DE IMPLEMENTAR...")
                exit()


def hide_cpf(cpf_or_cnpj):
    if len(cpf_or_cnpj) > 0:
        result = cpf_or_cnpj.replace('.','').replace('-','').replace('/','')

        if len(result) == 11:
            cpf_hidded = "{}.***.***-{}".format(result[0:3], result[-2:])
            return cpf_hidded
        elif len(result) == 14:
            return cpf_or_cnpj
        else:
            print(f"\033[1;31mA quantidade de caracteres inserida difere da quantidade de caracteres de um CPF ou CNPJ")
            print(f"Valor informado: {cpf_or_cnpj}.\033[0m")
            exit()
    else:
        return ""


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
    if not os.path.exists('output'):
        os.makedirs('output')
    try:
        with open(path_file, 'w', encoding='utf-8') as output_file:
            output_file.write(content)
            print(f"\033[1;32mO arquivo {path_file} foi criado com sucesso!\033[0m")
    except PermissionError:
        print(f"\033[1;31mO arquivo {path_file} não possui permissão de escrita.\033[0m")
        return
    except Exception as e:
        print(f"\033[1;31mOcorreu um erro inesperado ao tentar ler o arquivo {path_file}: {e}\033[0m")
        return


def treat_sensitive_data(file_name, target):
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


def main():
    file_name = input('Informe o nome de arquivo de entrada: ')
    option = input("SELECT THE OPTION DESIRED:\n1 - FORMAT NAME OF FILE\n2 - REMOVE EXTRA WORDS OF NAME OF FILE\n3 - REPLACE PART OF THE NAME OF FILE TO OTHER TEXT\n4 - FORMAT CSV FILE\n5 - HIDE SENSITIVE DATA\n0 - EXIT\n")

    if (option == '1'):
        format_filename(file_name)
    elif (option == '2'):
        extra_word = input('Insira o texto que deseja remover do nome do arquivo: ')
        remove_extra_words_in_filename(file_name, extra_word)
    elif (option == '3'):
        part_to_remove = input('Insira a parte do texto que deseja remover do nome do arquivo: ')
        part_to_add = input('Insira o texto que deseja adicionar no lugar do texto removido: ')
        replace_part_of_namefile(file_name, part_to_remove, part_to_add)
    elif (option == '4'):
        format_csv(file_name)
    elif (option == '5'):
        target = input('Informe o nome do campo a ser tratado (Exemplo: CPF): ')
        treat_sensitive_data(file_name, target)
    else:
        exit()


if __name__ == "__main__":
    main() 
