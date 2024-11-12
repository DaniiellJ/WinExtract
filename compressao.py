import zipfile
import os
from tkinter import messagebox

def comprimir_arquivos(arquivos_para_compressao, arquivo_zip_destino, modo_compressao):
    if modo_compressao == "unico":
        with zipfile.ZipFile(arquivo_zip_destino, 'w') as zip_ref:
            for arquivo in arquivos_para_compressao:
                zip_ref.write(arquivo, os.path.basename(arquivo))
        messagebox.showinfo("Sucesso", f"Arquivos comprimidos com sucesso em '{arquivo_zip_destino}'.")

    elif modo_compressao == "individual":
        for arquivo in arquivos_para_compressao:
            nome_zip_individual = os.path.join(
                os.path.dirname(arquivo_zip_destino),
                f"{os.path.splitext(os.path.basename(arquivo))[0]}.zip"
            )
            with zipfile.ZipFile(nome_zip_individual, 'w') as zip_ref:
                zip_ref.write(arquivo, os.path.basename(arquivo))
        messagebox.showinfo("Sucesso", "Todos os arquivos foram comprimidos separadamente.")
