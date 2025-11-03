# laboratorio.py
from src.converter import convert_docx_to_json
import os

# 1. Definimos o caminho para o nosso arquivo de amostra.
caminho_do_docx = os.path.join('tests', 'data', 'sample3.docx')

# 2. Executamos a nossa função com esse arquivo.
resultado_json = convert_docx_to_json(caminho_do_docx)

# 3. Imprimimos o resultado na tela para podermos ver!
print("--- O JSON gerado pela função é: ---")
print(resultado_json)
print("------------------------------------")