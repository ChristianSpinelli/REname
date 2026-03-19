import customtkinter as ctk
from tkinter import filedialog
from app.core.file_controller import FileController

# Configurações de tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

fileController = FileController()

def init_home():

     # Função para abrir o explorador de pastas
    def choose_folder(event=None):
        folder_path = filedialog.askdirectory()
        if folder_path:
            # Temporariamente habilita o campo para atualizar o valor
            folder_entry.configure(state="normal")
            folder_entry.delete(0, "end")
            folder_entry.insert(0, folder_path)
            folder_entry.configure(state="readonly")
    
       # Função do botão Confirm
    def confirm_action():
        insert_text = text_entry.get()
        remove_text = text_remove_entry.get()
        folder_path = folder_entry.get()
        all_instances_checked = check_all_instances.get()
        files_renamed = fileController.rename_files(folder_path, remove_text, insert_text, all_instances_checked)
        if(files_renamed):
            text_entry.delete(0, len(insert_text))
            text_remove_entry.delete(0, len(remove_text))
            check_all_instances.deselect()
        

    # Criação da janela principal
    app = ctk.CTk()
    app.title("REname")
    app.geometry("500x500")
    app.resizable(False, False)

    # Container principal
    main_frame = ctk.CTkFrame(app, corner_radius=15)
    main_frame.pack(padx=20, pady=20, fill="both", expand=True)

    # Título do app
    title_label = ctk.CTkLabel(
        main_frame,
        text="REname",
        font=ctk.CTkFont(size=28, weight="bold")
    )
    title_label.pack(pady=(20, 10))

    #campo de remoção de texto
    text_remove_label = ctk.CTkLabel(main_frame, text="Infome o texto que deseja remover:")
    text_remove_label.pack(anchor="w", padx=20)

    text_remove_entry = ctk.CTkEntry(main_frame, width=400, height=35)
    text_remove_entry.pack(pady=5, padx=20)

    check_all_instances = ctk.CTkCheckBox(main_frame, text="Substituir TODAS as ocorrências.", checkbox_height=20, checkbox_width=20, corner_radius=5)
    check_all_instances.pack(anchor="w", padx=30, pady=10)

    # Campo de texto
    text_label = ctk.CTkLabel(main_frame, text="Informe o texto que deseja adicionar:")
    text_label.pack(anchor="w", padx=20)    

    text_entry = ctk.CTkEntry(main_frame, width=400, height=35)
    text_entry.pack(pady=5, padx=20)

    # Campo de pasta
    folder_label = ctk.CTkLabel(main_frame, text="Informe a pasta:")
    folder_label.pack(anchor="w", padx=20, pady=(15, 0))

    folder_entry = ctk.CTkEntry(main_frame, width=400, height=35, state="readonly")
    folder_entry.pack(pady=5, padx=20)

    # Vincula clique no campo à função
    folder_entry.bind("<Button-1>", choose_folder)

    confirm_button = ctk.CTkButton(
        main_frame,
        text="Confirmar",
        height=40,
        command=confirm_action
    )
    confirm_button.pack(pady=25)

    app.mainloop()