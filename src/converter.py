import pandas as pd
import docx
import json
import os

def convert_csv_to_json(file_path):

# Função que irá ler o arquivo CSV
    dataframe = pd.read_csv(file_path)

# Função que irá converter o arquivo para JSON
    string_json = dataframe.to_json()
    return string_json

def convert_excel_to_json(file_path):

    dataframe = pd.read_excel(file_path)

    string_json = dataframe.to_json()
    return string_json

def convert_docx_to_json(file_path):
    lista_de_textos = []
    documento = docx.Document(file_path)
    for paragrafo in documento.paragraphs:
        lista_de_textos.append(paragrafo.text)
    string_json = json.dumps(lista_de_textos)
    return string_json

# Substitua sua função convert_file por esta
def convert_file(file_path):
    # Todo este código está indentado, ou seja, DENTRO da função.
    
    _ , extension = os.path.splitext(file_path)

    # Etapa 1: Decidir qual função "trabalhadora" usar
    if extension == '.csv':
        # Aqui não executamos, apenas guardamos a FUNÇÃO em si na variável
        funcao_a_executar = convert_csv_to_json
    elif extension == '.xlsx':
        funcao_a_executar = convert_excel_to_json
    elif extension == '.docx':
        funcao_a_executar = convert_docx_to_json
    else:
        # Se não encontrarmos uma função, lançamos o erro imediatamente
        raise ValueError(f"Formato de arquivo não suportado: {extension}")

    # Etapa 2: Tentar executar a função que foi escolhida na Etapa 1
    try:
        # Agora sim, chamamos a função que foi guardada na variável
        return funcao_a_executar(file_path)
    except Exception as e:
        # Se a execução falhar (ex: arquivo corrompido), capturamos o erro
        raise Exception(f"Erro ao processar o arquivo: {file_path}")