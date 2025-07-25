import customtkinter
import database

customtkinter.set_appearance_mode("dark")  # Modo escuro
customtkinter.set_default_color_theme("green")  # Tema Verde

def voltar():
    atualizar_layout()
    database.email_usuario_logado = None
    database.card_title.pack(pady=12)
    button.pack(pady=100, padx=20)
    button2.pack(pady=100, padx=20)

def voltar_home():
    atualizar_layout()
    database.card_home_title.pack(pady=12)
    botao_curriculo()

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
        command=lambda: realizar_login(verificacao, email_entry.get(), senha_entry.get()),
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

def realizar_login(verificacao, email, senha):
    # Chama a função de login e armazena o resultado
    database.resultado_verificacao = database.login(verificacao, email, senha)
    
    if database.resultado_verificacao:  # Verifica se o login foi bem-sucedido
        atualizar_layout()
        database.card_home_title.pack(pady=12)
        botao_curriculo()
    else:
        # Aqui você pode adicionar uma mensagem de erro se o login falhar
        print("Login falhou. Verifique suas credenciais.")

def inputs_vaga():
    atualizar_layout()
    nome_vaga = customtkinter.CTkEntry(
        master=database.card_frame,
        placeholder_text="Ex: Enfermeiro, Pedreiro...",
        width=200,
        height=40,
        fg_color="white",
        text_color="black",
        border_color="gray"
    )

def inputs_curriculo():
    horarios = customtkinter.CTkComboBox(master=database.card_frame,
        values=["Qualquer", "Integral", "Manhã", "Tarde", "Noite"])
    
    nome_entry = customtkinter.CTkEntry(
        master=database.card_frame,
        placeholder_text="Nome",
        width=200,
        height=40,
        fg_color="white",
        text_color="black",
        border_color="gray"
    )
    contato_entry = customtkinter.CTkEntry(
        master=database.card_frame,
        placeholder_text="Contato",
        width=200,
        height=40,
        fg_color="white",
        text_color="black",
        border_color="gray"
    )
    endereco_entry = customtkinter.CTkEntry(
        master=database.card_frame,
        placeholder_text="Endereço",
        width=200,
        height=40,
        fg_color="white",
        text_color="black",
        border_color="gray"
    )
    
    escolaridade = customtkinter.CTkComboBox(master=database.card_frame,
        values=["Fundamental Incompleto", "Fundamental Completo", "Médio Incompleto", "Médio Completo", "Superior Incompleto", "Superior Completo"])
    
    botao_voltar_home = customtkinter.CTkButton(
        master=database.card_frame,
        text="Voltar",
        command=voltar_home,
        fg_color="green",
        hover_color="darkgreen",
        text_color="white",
        width=200,
        height=40
    )
    
    botao_criar = customtkinter.CTkButton(
        master=database.card_frame,
        text="Criar Currículo",
        command=lambda: criar_curriculo(nome_entry.get(), contato_entry.get(), endereco_entry.get(), horarios.get(), escolaridade.get()),
        fg_color="green",
        hover_color="darkgreen",
        text_color="white",
        width=200,
        height=40
    )

    atualizar_layout()
    nome_entry.pack(pady=20, padx=20)
    contato_entry.pack(pady=20, padx=20)
    endereco_entry.pack(pady=20, padx=20)
    horarios.pack(padx=20, pady=20)
    escolaridade.pack(pady=20, padx=20)
    botao_criar.pack(pady=20)
    botao_voltar_home.pack(pady=100, padx=20)

def botao_curriculo():
    botao_criar = customtkinter.CTkButton(
        master=database.card_frame,
        text="Criar Currículo",
        command=inputs_curriculo,
        fg_color="green",
        hover_color="darkgreen",
        text_color="white",
        width=200,
        height=40
    )

    botao_logout = customtkinter.CTkButton(
        master=database.card_frame,
        text="Logout",
        command=voltar,
        fg_color="green",
        hover_color="darkgreen",
        text_color="white",
        width=100,
        height=20
    )

    criar_buscar = customtkinter.CTkButton(
        master=database.card_frame,
        text="Buscar Vagas",
        command=inputs_vaga,
        fg_color="green",
        hover_color="darkgreen",
        text_color="white",
        width=200,
        height=40
    )

    botao_criar.pack(pady=20)
    criar_buscar.pack(pady=20)
    busca = database.buscar_vagas()
    for vaga in busca:
        database.card_vaga.pack(pady=5)
        print(vaga)

    botao_logout.pack(pady=100, padx=40)




def criar_curriculo(nome, contato, endereco, horarios, escolaridade):
    # Aqui você deve garantir que o email do usuário logado esteja acessível  
    email_usuario = database.email_usuario_logado  # Supondo que você tenha armazenado o email do usuário logado
    if not all([nome, contato, endereco, horarios, escolaridade]):
        print("Por favor, preencha todos os campos.")
        return
    # Chame a função de criação de currículo no banco de dados
    database.criar_curriculo(nome, contato, endereco, horarios, escolaridade, email_usuario)

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

# Define o layout inicial (pack)
button = customtkinter.CTkButton(database.card_frame, text="Procuro Emprego", command=botao_pro_em, fg_color="green", hover_color="darkgreen")
button2 = customtkinter.CTkButton(database.card_frame, text="Sou Empresa", command=botao_sou_em, fg_color="green", hover_color="darkgreen")
button.pack(pady=100, padx=20)
button2.pack(pady=100, padx=20)

database.root.mainloop()
database.buscar_vagas()
