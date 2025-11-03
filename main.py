import customtkinter as ctk
from tkinter import filedialog
import os
from src.converter import convert_file
import sys

def resource_path(relative_path):
    try:
        # O PyInstaller cria uma pasta temporária e guarda o caminho nela
        base_path = sys._MEIPASS
    except Exception:
        # Se sys._MEIPASS não estiver definido, estamos rodando no ambiente normal
        base_path = os.path.abspath(".")
        
    return os.path.join(base_path, relative_path)
# 1. Cria a instância principal da aplicação (a janela)
app = ctk.CTk()
app.title("Conversor para JSON")
icon_path = resource_path("json_app.ico")
app.iconbitmap(icon_path)
app.geometry("500x400")
ctk.set_appearance_mode("Dark")
# --- FUNÇÕES ---
def selecionar_arquivo():
    caminho_do_arquivo = filedialog.askopenfilename()
    if caminho_do_arquivo:
        label_selecionar_arquivo.full_path = caminho_do_arquivo
        nome_do_arquivo = os.path.basename(caminho_do_arquivo)
        label_selecionar_arquivo.configure(text= nome_do_arquivo)
        update_status("Arquivo selecionado com sucesso!")
def iniciar_conversao():
    try:
        caminho_para_converter = label_selecionar_arquivo.full_path
        resultado_json = convert_file(caminho_para_converter)
        update_status("Conversão concluída e arquivo salvo!")

        # --- LÓGICA DE SALVAR CORRIGIDA ---
        
        # CORREÇÃO 1: Chamando 'filedialog' diretamente.
        # CORREÇÃO 2: Usando 'asksaveasfilename' para obter a string do caminho.
        caminho_para_salvar = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )

        # Este 'if' e 'with open' agora funcionarão perfeitamente
        if caminho_para_salvar:
            with open(caminho_para_salvar, "w", encoding="utf-8") as arquivo_de_saida:
                arquivo_de_saida.write(resultado_json)
        
        # --- O resto do seu código estava perfeito! ---
        textbox_resultado.configure(state="normal")
        textbox_resultado.delete("1.0", "end")
        textbox_resultado.insert("1.0", resultado_json)
        textbox_resultado.configure(state="disabled")

    except Exception as e:
        print(f"Ocorreu um erro: {e}") 
        mensagem_de_erro = f"Ocorreu um erro:\n\n{e}"
        textbox_resultado.configure(state="normal")
        textbox_resultado.delete("1.0", "end")
        textbox_resultado.insert("1.0", mensagem_de_erro) 
        textbox_resultado.configure(state="disabled")
def copiar_json():
    texto_para_copiar = textbox_resultado.get("1.0", "end")
    app.clipboard_clear()
    app.clipboard_append(texto_para_copiar)
    update_status("JSON copiado para a área de transferênica!")
def update_status(message):
    status_bar.configure(text=message)
# --- WIDGETS ---
# main_frame para conter todos os outros widgets
main_frame = ctk.CTkFrame(master=app)
main_frame.pack(pady=20, padx=20, fill="both", expand=True)
# frame para os botões de conversão
button_frame = ctk.CTkFrame(master=main_frame)
button_frame.pack(pady=10)
# Label selecionar arquivo
label_selecionar_arquivo = ctk.CTkLabel(master=main_frame, text="Nenhum arquivo selecionado" )
label_selecionar_arquivo.pack(pady=10)
# Botão converter para JSON
botao_converter = ctk.CTkButton(
    master=button_frame,
    text="Converter",
    fg_color="#1f6aa5",      
    hover_color="#144870",   
    text_color="#FFFFFF",     
    command=iniciar_conversao
    )
botao_converter.pack(side="right", padx=10)
# Caixa de texto
textbox_resultado = ctk.CTkTextbox(master=main_frame)
textbox_resultado.pack(pady=10)
# Botão selecionar arquivo
botao_selecionar_arquivo = ctk.CTkButton(
    master=button_frame, 
    text="Selecionar Arquivo",
    fg_color="#1f6aa5",      
    hover_color="#144870",   
    text_color="#FFFFFF",     
    command=selecionar_arquivo
    )
botao_selecionar_arquivo.pack(side="left", padx=10)
# Copiar para área de transferência
botao_copiar_json = ctk.CTkButton(
    master=main_frame,
    text="Copiar JSON",
    fg_color="#1f6aa5",      
    hover_color="#144870",   
    text_color="#FFFFFF",    
    command=copiar_json)
botao_copiar_json.pack(pady=10)
# Barra de status
status_bar = ctk.CTkLabel(master=app, text="Pronto")
status_bar.pack(side="bottom", fill="x")
# 2. Inicia o loop principal que mantém a janela aberta
app.mainloop()

