import customtkinter
import database

customtkinter.set_appearance_mode("dark")  # Modo escuro
customtkinter.set_default_color_theme("green")  # Tema Verde

def voltar():
    atualizar_layout()
    database.card_title.pack(pady=12)
    button.pack(pady=100, padx=20)
    button2.pack(pady=100, padx=20)
    

def botao_pro_em():
    atualizar_layout()
    database.verificacao = 1
    botao_cadastro = customtkinter.CTkButton(
        master=database.card_frame,
        text="Cadastro",
        command=lambda: cadastrar(database.verificacao),
        fg_color="green",
        hover_color="darkgreen",
        text_color="white",
        width=200,
        height=40
    )
    botao_login = customtkinter.CTkButton(
        master=database.card_frame,
        text="Login",
        command=lambda: login(database.verificacao),
        fg_color="green",
        hover_color="darkgreen",
        text_color="white",
        width=200,
        height=40
    )
    
    botao_voltar= customtkinter.CTkButton(
        master=database.card_frame,
        text="Voltar",
        command=voltar,
        fg_color="green",
        hover_color="darkgreen",
        text_color="white",
        width=200,
        height=40
    )
    botao_cadastro.pack(pady=100, padx=10)
    botao_login.pack(pady=10, padx=10)
    botao_voltar.pack(pady=150)

def botao_sou_em():
    atualizar_layout()
    database.verificacao = 2
    botao_cadastro = customtkinter.CTkButton(
        master=database.card_frame,
        text="Cadastro",
        command=lambda: cadastrar(database.verificacao),
        fg_color="green",
        hover_color="darkgreen",
        text_color="white",
        width=200,
        height=40
    )
    botao_login = customtkinter.CTkButton(
        master=database.card_frame,
        text="Login",
        command=lambda: login(database.verificacao),
        fg_color="darkgreen",
        hover_color="green",
        text_color="white",
        width=200,
        height=40
    )
    
    botao_voltar= customtkinter.CTkButton(
        master=database.card_frame,
        text="Voltar",
        command=voltar,
        fg_color="green",
        hover_color="darkgreen",
        text_color="white",
        width=200,
        height=40
    )
    
    botao_cadastro.pack(pady=100, padx=10)
    botao_login.pack(pady=10, padx=10)
    botao_voltar.pack(pady=150)

def login(verificacao):
    atualizar_layout()  # Limpa a interface anterior
    email_entry = customtkinter.CTkEntry(
        master=database.card_frame,
        placeholder_text="Email",
        width=200,
        height=40,
        fg_color="white",
        text_color="black",
        border_color="gray"
    )
    senha_entry = customtkinter.CTkEntry(
        master=database.card_frame,
        placeholder_text="senha",
        width=200,
        height=40,
        fg_color="white",
        text_color="black",
        border_color="gray"
    )
    email_entry.pack(pady=20, padx=20)
    senha_entry.pack(pady=20, padx=20)
    botao_login = customtkinter.CTkButton(
        master=database.card_frame,
        text="Login",
        command=lambda: database.login(verificacao, email_entry.get(), senha_entry.get()),
        fg_color="green",
        hover_color="darkgreen",
        text_color="white",
        width=200,
        height=40
    )
    
    botao_voltar= customtkinter.CTkButton(
        master=database.card_frame,
        text="Voltar",
        command=voltar,
        fg_color="green",
        hover_color="darkgreen",
        text_color="white",
        width=200,
        height=40
    )
    botao_login.pack(pady=100, padx=10)
    botao_voltar.pack(pady=150)

def cadastrar(verificacao):
    atualizar_layout()  # Limpa a interface anterior
    nome_entry = customtkinter.CTkEntry(
        master=database.card_frame,
        placeholder_text="Nome",
        width=200,
        height=40,
        fg_color="white",
        text_color="black",
        border_color="gray"
    )
    email_entry = customtkinter.CTkEntry(
        master=database.card_frame,
        placeholder_text="Email",
        width=200,
        height=40,
        fg_color="white",
        text_color="black",
        border_color="gray"
    )
    senha_entry = customtkinter.CTkEntry(
        master=database.card_frame,
        placeholder_text="senha",
        width=200,
        height=40,
        fg_color="white",
        text_color="black",
        border_color="gray"
    )
    nome_entry.pack(pady=20, padx=20)
    email_entry.pack(pady=20, padx=20)
    senha_entry.pack(pady=20, padx=20)
    botao_cadastro = customtkinter.CTkButton(
        master=database.card_frame,
        text="Cadastro",
        command=lambda: database.criar_conta(verificacao, email_entry.get(), nome_entry.get(), senha_entry.get()),
        fg_color="green",
        hover_color="darkgreen",
        text_color="white",
        width=200,
        height=40
    )
    
    botao_voltar= customtkinter.CTkButton(
        master=database.card_frame,
        text="Voltar",
        command=voltar,
        fg_color="green",
        hover_color="darkgreen",
        text_color="white",
        width=200,
        height=40
    )
    
    botao_cadastro.pack(pady=100, padx=10)
    botao_voltar.pack(pady=150)

def atualizar_layout():
    for widget in database.card_frame.winfo_children():
        widget.pack_forget()

button = customtkinter.CTkButton(database.card_frame, text="Procuro Emprego", command=botao_pro_em, fg_color="green", hover_color="darkgreen")
button2 = customtkinter.CTkButton(database.card_frame, text="Sou Empresa", command=botao_sou_em, fg_color="green", hover_color="darkgreen")

# Define o layout inicial (pack)
button.pack(pady=100, padx=20)
button2.pack(pady=100, padx=20)

database.root.mainloop()
