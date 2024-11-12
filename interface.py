import tkinter as tk
from tkinter import filedialog

def criar_janela(selecionar_arquivos_origem, selecionar_diretorio_destino, selecionar_arquivos_para_compressao,
                 selecionar_arquivo_zip_destino, iniciar_extracao, iniciar_compressao):
    
    janela = tk.Tk()
    janela.title("Extrator e Compressor de Arquivos ZIP")

    tk.Label(janela, text="Origem dos Arquivos Zip:").grid(row=0, column=0, padx=10, pady=10)
    entrada_origem = tk.Entry(janela, width=50)
    entrada_origem.grid(row=0, column=1, padx=10, pady=10)
    tk.Button(janela, text="Procurar", command=selecionar_arquivos_origem).grid(row=0, column=2, padx=10, pady=10)

    tk.Label(janela, text="Diretório de Destino:").grid(row=1, column=0, padx=10, pady=10)
    entrada_destino = tk.Entry(janela, width=50)
    entrada_destino.grid(row=1, column=1, padx=10, pady=10)
    tk.Button(janela, text="Procurar", command=selecionar_diretorio_destino).grid(row=1, column=2, padx=10, pady=10)

    modo_extracao_var = tk.StringVar(value="unica")
    tk.Label(janela, text="Modo de Extração:").grid(row=2, column=0, padx=10, pady=10)
    tk.Radiobutton(janela, text="Extração Separada", variable=modo_extracao_var, value="unica").grid(row=2, column=1, sticky="w")
    tk.Radiobutton(janela, text="Extração Única", variable=modo_extracao_var, value="individual").grid(row=3, column=1, sticky="w")

    tk.Label(janela, text="Arquivos para Comprimir:").grid(row=4, column=0, padx=10, pady=10)
    entrada_compressao = tk.Entry(janela, width=50)
    entrada_compressao.grid(row=4, column=1, padx=10, pady=10)
    tk.Button(janela, text="Procurar", command=selecionar_arquivos_para_compressao).grid(row=4, column=2, padx=10, pady=10)

    tk.Label(janela, text="Diretório de Destino:").grid(row=5, column=0, padx=10, pady=10)
    entrada_zip_destino = tk.Entry(janela, width=50)
    entrada_zip_destino.grid(row=5, column=1, padx=10, pady=10)
    tk.Button(janela, text="Procurar", command=selecionar_arquivo_zip_destino).grid(row=5, column=2, padx=10, pady=10)

    modo_compressao_var = tk.StringVar(value="unico")
    tk.Label(janela, text="Modo de Compressão:").grid(row=6, column=0, padx=10, pady=10)
    tk.Radiobutton(janela, text="Compressão Única", variable=modo_compressao_var, value="unico").grid(row=6, column=1, sticky="w")
    tk.Radiobutton(janela, text="Compressão Separada", variable=modo_compressao_var, value="individual").grid(row=7, column=1, sticky="w")

    tk.Button(janela, text="Iniciar Extração", command=iniciar_extracao).grid(row=8, column=1, padx=10, pady=10)
    tk.Button(janela, text="Iniciar Compressão", command=iniciar_compressao).grid(row=9, column=1, padx=10, pady=10)

    return janela, entrada_origem, entrada_destino, entrada_compressao, entrada_zip_destino, modo_extracao_var, modo_compressao_var
