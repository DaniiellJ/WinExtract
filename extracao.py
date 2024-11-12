import zipfile
import os
from tkinter import messagebox

def extrair_arquivos(arquivos_zip, diretorio_destino, modo_extracao):
    os.makedirs(diretorio_destino, exist_ok=True)
    total_arquivos = len(arquivos_zip)
    
    if total_arquivos == 0:
        messagebox.showwarning("Atenção", "Nenhum arquivo .zip selecionado.")
        return

    for caminho_arquivo in arquivos_zip:
        try:
            if not zipfile.is_zipfile(caminho_arquivo):
                messagebox.showerror("Erro", f"O arquivo '{caminho_arquivo}' não é um arquivo ZIP válido.")
                continue

            if modo_extracao == "unica":
                with zipfile.ZipFile(caminho_arquivo, 'r') as zip_ref:
                    zip_ref.extractall(diretorio_destino)
            elif modo_extracao == "individual":
                nome_subpasta = os.path.join(diretorio_destino, os.path.splitext(os.path.basename(caminho_arquivo))[0])
                os.makedirs(nome_subpasta, exist_ok=True)
                with zipfile.ZipFile(caminho_arquivo, 'r') as zip_ref:
                    zip_ref.extractall(nome_subpasta)

        except zipfile.BadZipFile:
            messagebox.showerror("Erro", f"O arquivo '{caminho_arquivo}' não é um arquivo ZIP válido.")
            continue
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao extrair o arquivo '{caminho_arquivo}': {e}")

    messagebox.showinfo("Sucesso", "Todos os arquivos .zip foram extraídos com sucesso!")
