from tkinter import filedialog, messagebox  
from compressao import comprimir_arquivos
from extracao import extrair_arquivos
from interface import criar_janela
import tkinter as tk

def selecionar_arquivos_origem():
    arquivos = filedialog.askopenfilenames(title="Origem dos Arquivos Zip", filetypes=[("Arquivos ZIP", "*.zip")])
    if arquivos:
        entrada_origem.delete(0, tk.END)
        entrada_origem.insert(0, "; ".join(arquivos))

def selecionar_diretorio_destino():
    diretorio = filedialog.askdirectory(title="Selecione o Diretório de Destino")
    if diretorio:
        entrada_destino.delete(0, tk.END)
        entrada_destino.insert(0, diretorio)

def selecionar_arquivos_para_compressao():
    arquivos = filedialog.askopenfilenames(title="Arquivos para Comprimir")
    if arquivos:
        entrada_compressao.delete(0, tk.END)
        entrada_compressao.insert(0, "; ".join(arquivos))

def selecionar_arquivo_zip_destino():
    arquivo = filedialog.asksaveasfilename(title="Diretório de Destino", defaultextension=".zip", filetypes=[("Arquivo ZIP", "*.zip")])
    if arquivo:
        entrada_zip_destino.delete(0, tk.END)
        entrada_zip_destino.insert(0, arquivo)

def iniciar_extracao():
    arquivos_origem = entrada_origem.get().split("; ")
    diretorio_destino = entrada_destino.get()
    modo_extracao = modo_extracao_var.get()

    if not arquivos_origem or not diretorio_destino:
        messagebox.showwarning("Atenção", "Por favor, selecione arquivos ZIP e o diretório de destino.")
    else:
        extrair_arquivos(arquivos_origem, diretorio_destino, modo_extracao)

def iniciar_compressao():
    arquivos_para_compressao = entrada_compressao.get().split("; ")
    arquivo_zip_destino = entrada_zip_destino.get()
    modo_compressao = modo_compressao_var.get()

    if not arquivos_para_compressao or not arquivo_zip_destino:
        messagebox.showwarning("Atenção", "Por favor, selecione arquivos para compressão e o destino do arquivo ZIP.")
    else:
        comprimir_arquivos(arquivos_para_compressao, arquivo_zip_destino, modo_compressao)

# Inicializando a Interface
janela, entrada_origem, entrada_destino, entrada_compressao, entrada_zip_destino, modo_extracao_var, modo_compressao_var = criar_janela(
    selecionar_arquivos_origem,
    selecionar_diretorio_destino,
    selecionar_arquivos_para_compressao,
    selecionar_arquivo_zip_destino,
    iniciar_extracao,
    iniciar_compressao
)

janela.mainloop()
