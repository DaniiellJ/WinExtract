import zipfile 
import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def extrair_arquivos(arquivos_zip, diretorio_destino, janela, modo_extracao):

    os.makedirs(diretorio_destino, exist_ok=True)
    total_arquivos = len(arquivos_zip)
    
    if total_arquivos == 0:
        messagebox.showwarning("Atenção", "Nenhum arquivo .zip selecionado.")
        return

    for i, caminho_arquivo in enumerate(arquivos_zip, start=1):
        try:
            if not zipfile.is_zipfile(caminho_arquivo):
                messagebox.showerror("Erro", f"O arquivo '{caminho_arquivo}' não é um arquivo ZIP válido.")
                continue

            if modo_extracao == "unica":
                with zipfile.ZipFile(caminho_arquivo, 'r') as zip_ref:
                    zip_ref.extractall(diretorio_destino)
                    print(f"Arquivo '{caminho_arquivo}' extraído com sucesso para '{diretorio_destino}'.")
            elif modo_extracao == "individual":
                nome_subpasta = os.path.join(diretorio_destino, os.path.splitext(os.path.basename(caminho_arquivo))[0])
                os.makedirs(nome_subpasta, exist_ok=True)
                with zipfile.ZipFile(caminho_arquivo, 'r') as zip_ref:
                    zip_ref.extractall(nome_subpasta)
                    print(f"Arquivo '{caminho_arquivo}' extraído com sucesso para '{nome_subpasta}'.")

        except zipfile.BadZipFile:
            print(f"Erro: O arquivo '{caminho_arquivo}' não é um arquivo ZIP válido.")
            messagebox.showerror("Erro", f"O arquivo '{caminho_arquivo}' não é um arquivo ZIP válido.")
            continue
        except Exception as e:
            print(f"Erro ao extrair o arquivo '{caminho_arquivo}': {e}")
            messagebox.showerror("Erro", f"Ocorreu um erro ao extrair o arquivo '{caminho_arquivo}': {e}")

    messagebox.showinfo("Sucesso", "Todos os arquivos .zip foram extraídos com sucesso!")

def comprimir_arquivos(arquivos_para_compressao, arquivo_zip_destino, modo_compressao):

    if modo_compressao == "unico":
        with zipfile.ZipFile(arquivo_zip_destino, 'w') as zip_ref:
            for arquivo in arquivos_para_compressao:
                zip_ref.write(arquivo, os.path.basename(arquivo))
                print(f"Arquivo '{arquivo}' adicionado ao ZIP '{arquivo_zip_destino}'.")
        messagebox.showinfo("Sucesso", f"Arquivos comprimidos com sucesso em '{arquivo_zip_destino}'.")

    elif modo_compressao == "individual":
        for arquivo in arquivos_para_compressao:
            nome_zip_individual = os.path.join(
                os.path.dirname(arquivo_zip_destino),
                f"{os.path.splitext(os.path.basename(arquivo))[0]}.zip"
            )
            with zipfile.ZipFile(nome_zip_individual, 'w') as zip_ref:
                zip_ref.write(arquivo, os.path.basename(arquivo))
                print(f"Arquivo '{arquivo}' comprimido em '{nome_zip_individual}'.")
        messagebox.showinfo("Sucesso", "Todos os arquivos foram comprimidos separadamente.")

def selecionar_arquivos_origem():
    arquivos = filedialog.askopenfilenames(
        title="Origem dos Arquivos Zip",
        filetypes=[("Arquivos ZIP", "*.zip")]
    )
    if arquivos:
        entrada_origem.delete(0, tk.END)
        entrada_origem.insert(0, "; ".join(arquivos))
        print(f"Arquivos ZIP selecionados: {arquivos}")

def selecionar_arquivos_para_compressao():
    arquivos = filedialog.askopenfilenames(
        title="Arquivos para Comprimir",
    )
    if arquivos:
        entrada_compressao.delete(0, tk.END)
        entrada_compressao.insert(0, "; ".join(arquivos))
        print(f"Arquivos para compressão selecionados: {arquivos}")

def selecionar_diretorio_destino():
    diretorio = filedialog.askdirectory(title="Selecione o Diretório de Destino")
    if diretorio:
        entrada_destino.delete(0, tk.END)
        entrada_destino.insert(0, diretorio)

def selecionar_arquivo_zip_destino():
    arquivo = filedialog.asksaveasfilename(
        title="Diretório de Destino",
        defaultextension=".zip",
        filetypes=[("Arquivo ZIP", "*.zip")]
    )
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
        extrair_arquivos(arquivos_origem, diretorio_destino, janela, modo_extracao)

def iniciar_compressao():
    arquivos_para_compressao = entrada_compressao.get().split("; ")
    arquivo_zip_destino = entrada_zip_destino.get()
    modo_compressao = modo_compressao_var.get()
    
    if not arquivos_para_compressao or not arquivo_zip_destino:
        messagebox.showwarning("Atenção", "Por favor, selecione arquivos para compressão e o destino do arquivo ZIP.")
    else:
        comprimir_arquivos(arquivos_para_compressao, arquivo_zip_destino, modo_compressao)

# Interface
janela = tk.Tk()
janela.title("Extrator e Compressor de Arquivos ZIP")

# Campo de origem para extração
tk.Label(janela, text="Origem dos Arquivos Zip:").grid(row=0, column=0, padx=10, pady=10)
entrada_origem = tk.Entry(janela, width=50)
entrada_origem.grid(row=0, column=1, padx=10, pady=10)
botao_origem = tk.Button(janela, text="Procurar", command=selecionar_arquivos_origem)
botao_origem.grid(row=0, column=2, padx=10, pady=10)

# Campo de destino para extração
tk.Label(janela, text="Diretório de Destino:").grid(row=1, column=0, padx=10, pady=10)
entrada_destino = tk.Entry(janela, width=50)
entrada_destino.grid(row=1, column=1, padx=10, pady=10)
botao_destino = tk.Button(janela, text="Procurar", command=selecionar_diretorio_destino)
botao_destino.grid(row=1, column=2, padx=10, pady=10)

# Opção de extração
modo_extracao_var = tk.StringVar(value="unica")
tk.Label(janela, text="Modo de Extração:").grid(row=2, column=0, padx=10, pady=10)
radio_unica = tk.Radiobutton(janela, text="Extração Separada", variable=modo_extracao_var, value="unica")
radio_individual_extracao = tk.Radiobutton(janela, text="Extração Única", variable=modo_extracao_var, value="individual")
radio_unica.grid(row=2, column=1, sticky="w")
radio_individual_extracao.grid(row=3, column=1, sticky="w")

# Campo de origem para compressão
tk.Label(janela, text="Arquivos para Comprimir:").grid(row=4, column=0, padx=10, pady=10)
entrada_compressao = tk.Entry(janela, width=50)
entrada_compressao.grid(row=4, column=1, padx=10, pady=10)
botao_compressao = tk.Button(janela, text="Procurar", command=selecionar_arquivos_para_compressao)
botao_compressao.grid(row=4, column=2, padx=10, pady=10)

# Campo de destino para compressão
tk.Label(janela, text="Diretório de Destino:").grid(row=5, column=0, padx=10, pady=10)
entrada_zip_destino = tk.Entry(janela, width=50)
entrada_zip_destino.grid(row=5, column=1, padx=10, pady=10)
botao_zip_destino = tk.Button(janela, text="Procurar", command=selecionar_arquivo_zip_destino)
botao_zip_destino.grid(row=5, column=2, padx=10, pady=10)

# Opção de compressão
modo_compressao_var = tk.StringVar(value="unico")
tk.Label(janela, text="Modo de Compressão:").grid(row=6, column=0, padx=10, pady=10)
radio_unica_compressao = tk.Radiobutton(janela, text="Compressão Única", variable=modo_compressao_var, value="unico")
radio_individual_compressao = tk.Radiobutton(janela, text="Compresão Separada", variable=modo_compressao_var, value="individual")
radio_unica_compressao.grid(row=6, column=1, sticky="w")
radio_individual_compressao.grid(row=7, column=1, sticky="w")

# Botões de Ação
botao_extrair = tk.Button(janela, text="Extrair", command=iniciar_extracao)
botao_extrair.grid(row=2, column=2, padx=10, pady=10)

botao_comprimir = tk.Button(janela, text="Comprimir", command=iniciar_compressao)
botao_comprimir.grid(row=6, column=2, padx=10, pady=10)

janela.mainloop()
