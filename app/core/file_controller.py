import os
from tkinter import messagebox

class FileController:
   
   def none_text_found_error(self, remove_text:str, insert_text:str) -> bool:
      return remove_text == "" and insert_text == ""
   
   def folder_path_invalid(self, folder_path:str) -> bool:
      return not folder_path or not os.path.isdir(folder_path)
   
   def none_file_found(self, files:list[str]) -> bool:
     return files.__len__ == 0
   
   def initial_validations(self, remove_text:str, insert_text:str, folder_path:str, files:list[str]) -> bool:
        if(self.none_text_found_error(remove_text, insert_text)):
           messagebox.showerror("Erro", "Nenhum texto encontrado. Informe pelo menos um dos campos de texto.")
           return False
        elif(self.folder_path_invalid(folder_path)):
           messagebox.showerror("Erro", "Não foi informado um caminho de pasta válido!")
           return False
        elif(self.none_file_found(files)):
           messagebox.showerror("Erro", "Nenhum arquivo encontrado na pasta informada!")
           return False
        return True
           
   def rename_files(self, folder_path:str, remove_text:str, insert_text:str, all_instances_checked:bool):
    """
    Renomeia todos os arquivos na pasta adicionando o texto fornecido.
    """

    # Lista todos os arquivos da pasta
    files = os.listdir(folder_path)
    self.initial_validations(remove_text, insert_text, folder_path, files)
    
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)

        # Ignora pastas
        if os.path.isfile(file_path):
            # Extrai extensão
            name, ext = os.path.splitext(file_name)

            if(remove_text != ""):
               if all_instances_checked:
                  name = name.replace(remove_text, insert_text)
               else:
                  name = name.replace(remove_text, insert_text, 1)

            if (insert_text != "" and remove_text == ""):
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
                return False
    
    messagebox.showinfo("Sucesso", "Arquivos atualizados com sucesso.")
    return True