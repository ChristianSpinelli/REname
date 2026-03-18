import os
from tkinter import messagebox

class FileController:

   def rename_files(self, folder_path, remove_text, insert_text):
    """
    Renomeia todos os arquivos na pasta adicionando o texto fornecido.
    """
    if(remove_text == "" and insert_text == ""):
       messagebox.showerror("Erro", "Nenhum texto encontrado. Informe pelo menos um dos campos de texto.")
       return

    if not folder_path or not os.path.isdir(folder_path):
        messagebox.showerror("Erro", "Não foi informado um caminho de pasta válido!")
        return

    # Lista todos os arquivos da pasta
    files = os.listdir(folder_path)

    if files.__len__ == 0:
       messagebox.showerror("Erro", "Nenhum arquivo encontrado na pasta informada!")
       return

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)

        # Ignora pastas
        if os.path.isfile(file_path):
            # Extrai extensão
            name, ext = os.path.splitext(file_name)

            if(remove_text != ""):
               name = name.replace(remove_text, "")

            if (insert_text != ""):
               # Novo nome: nome antigo - conteúdo removido(caso houver) + nome novo adicionado + extensão no final 
               new_name = f"{name.rstrip()} {insert_text.rstrip()}{ext}"
            else:
                #Novo nome: nome antigo - conteúdo removido
                new_name = f"{name.rstrip()}{ext}"
            
            new_path = os.path.join(folder_path, new_name)

            try:
                # Renomeia o arquivo
                os.rename(file_path, new_path)
            except:
                messagebox.showerror("Error", "Um ou mais arquivos da pasta informada estão abertos. Feche os arquivos para que possam ser alterados.")
                return
    
    messagebox.showinfo("Sucesso", "Arquivos atualizados com sucesso.")