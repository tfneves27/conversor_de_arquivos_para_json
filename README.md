# Conversor Universal de Arquivos

Este é um aplicativo de desktop simples para Windows que converte arquivos .csv, .xlsx e .docx para o formato JSON.

## Funcionalidades

* Converte arquivos CSV para JSON.
* Converte arquivos Excel (.xlsx) para JSON.
* Extrai o texto de arquivos Word (.docx) para um JSON.
* Salva o JSON resultante em um novo arquivo.
* Exibe uma prévia do JSON na tela.
* Permite copiar o JSON para a área de transferência.

## Como Usar

1.  Baixe o arquivo `Conversor.zip` da seção "Releases".
2.  Descompacte o arquivo.
3.  Execute o arquivo `main.exe` (ou o nome que você der).
4.  Clique em "Selecionar Arquivo" e escolha um arquivo compatível.
5.  Clique em "Converter".
6.  Escolha um nome e local para salvar seu novo arquivo .json.

## Como Executar o Projeto (para Desenvolvedores)

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/tfneves27/conversor-de-arquivos-para-json.git](https://github.com/tfneves27/conversor-de-arquivos-para-json.git)
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd conversor_de_arquivos_para_json
    ```

3.  **Crie um ambiente virtual:**
    ```bash
    python -m venv venv
    ```

4.  **Ative o ambiente virtual:**
    * No Windows:
        ```bash
        .\venv\Scripts\activate
        ```

5.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

6.  **Execute a aplicação:**
    ```bash
    python main.py
    ```

7.  **(Opcional) Execute os testes:**
    ```bash
    pytest
    ```
## Tecnologias Utilizadas

* Python 3.10+
* CustomTkinter (para a interface gráfica)
* pandas (para manipulação de CSV e EXCEL)
* python-docx (para manipalação de DOCX)
* openpyxl
* pytest (para realizar testes)
* PyInstaller (para empacotamento do projeto)
