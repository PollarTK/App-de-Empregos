import customtkinter
import database

customtkinter.set_appearance_mode("dark")  # Modo escuro
customtkinter.set_default_color_theme("green")  # Tema Verde


def criar_botao(master, texto, comando, largura=200, altura=40):
    return customtkinter.CTkButton(
        master=master,
        text=texto,
        command=comando,
        fg_color="green",
        hover_color="darkgreen",
        text_color="white",
        width=largura,
        height=altura,
    )


def criar_entry(master, placeholder, show=None):
    return customtkinter.CTkEntry(
        master=master,
        placeholder_text=placeholder,
        width=200,
        height=40,
        fg_color="white",
        text_color="black",
        border_color="gray",
        show=show
    )


def voltar():
    atualizar_layout()
    database.email_usuario_logado = None
    database.card_title.pack(pady=(10, 20), anchor="center")
    button.pack(pady=(10, 20), anchor="center", padx=20)
    button2.pack(pady=(10, 20), anchor="center", padx=20)


def voltar_home():
    atualizar_layout()
    database.card_home_title.pack(pady=(10, 20), anchor="center")
    botao_curriculo()


def botao_emprego(tipo):
    atualizar_layout()
    database.verificacao = tipo
    botao_cadastro = criar_botao(
        database.card_frame, "Cadastro", lambda: cadastrar(database.verificacao))
    botao_login = criar_botao(
        database.card_frame, "Login", lambda: login(database.verificacao))
    botao_voltar = criar_botao(database.card_frame, "Voltar", voltar)

    botao_cadastro.pack(pady=100, padx=10)
    botao_login.pack(pady=10, padx=10)
    botao_voltar.pack(pady=150)


def login(verificacao):
    atualizar_layout()
    email_entry = criar_entry(database.card_frame, "Email")
    senha_entry = criar_entry(database.card_frame, "Senha", show="*")
    email_entry.pack(pady=20, padx=20)
    senha_entry.pack(pady=20, padx=20)

    botao_login = criar_botao(database.card_frame, "Login", lambda: realizar_login(
        verificacao, email_entry.get(), senha_entry.get()))
    botao_voltar = criar_botao(database.card_frame, "Voltar", voltar)

    botao_login.pack(pady=100, padx=10)
    botao_voltar.pack(pady=150)


def realizar_login(verificacao, email, senha):
    database.resultado_verificacao = database.login(verificacao, email, senha)
    if database.resultado_verificacao:
        atualizar_layout()
        database.card_home_title.pack(pady=12)
        botao_curriculo()
    else:
        print("Login falhou. Verifique suas credenciais.")


def inputs_curriculo():
    atualizar_layout()
    nome_entry = criar_entry(database.card_frame, "Nome")
    contato_entry = criar_entry(database.card_frame, "Contato")
    endereco_entry = criar_entry(database.card_frame, "Endereço")

    horarios = customtkinter.CTkComboBox(master=database.card_frame, values=[
                                         "Qualquer", "Integral", "Manhã", "Tarde", "Noite"])
    escolaridade = customtkinter.CTkComboBox(master=database.card_frame, values=[
                                             "Fundamental Incompleto", "Fundamental Completo", "Médio Incompleto", "Médio Completo", "Superior Incompleto", "Superior Completo"])

    botao_voltar_home = criar_botao(database.card_frame, "Voltar", voltar_home)
    botao_criar = criar_botao(database.card_frame, "Criar Currículo", lambda: criar_curriculo(
        nome_entry.get(), contato_entry.get(), endereco_entry.get(), horarios.get(), escolaridade.get()))

    nome_entry.pack(pady=20, padx=20)
    contato_entry.pack(pady=20, padx=20)
    endereco_entry.pack(pady=20, padx=20)
    horarios.pack(padx=20, pady=20)
    escolaridade.pack(pady=20, padx=20)
    botao_criar.pack(pady=20)
    botao_voltar_home.pack(padx=20)


def botao_curriculo():
    botao_criar = criar_botao(
        database.card_frame, "Criar Currículo", inputs_curriculo)
    criar_buscar = criar_botao(
        database.card_frame, "Buscar Vagas", inputs_curriculo)
    botao_logout = criar_botao(database.card_frame, "Logout", voltar)

    botao_criar.pack(pady=20)
    criar_buscar.pack(pady=20)
    busca = database.buscar_vagas()
    for vaga in busca:
        database.card_vaga.pack(pady=5)
        print(vaga)
    botao_logout.pack(pady=100, padx=40)


def criar_curriculo(nome, contato, endereco, horarios, escolaridade):
    email_usuario = database.email_usuario_logado
    if not all([nome, contato, endereco, horarios, escolaridade]):
        print("Por favor, preencha todos os campos.")
        return
    database.criar_curriculo(nome, contato, endereco,
                             horarios, escolaridade, email_usuario)


def cadastrar(verificacao):
    atualizar_layout()
    nome_entry = criar_entry(database.card_frame, "Nome")
    email_entry = criar_entry(database.card_frame, "Email")
    senha_entry = criar_entry(database.card_frame, "Senha", show="*")

    nome_entry.pack(pady=20, padx=20)
    email_entry.pack(pady=20, padx=20)
    senha_entry.pack(pady=20, padx=20)

    botao_cadastro = criar_botao(database.card_frame, "Cadastro", lambda: database.criar_conta(
        verificacao, email_entry.get(), nome_entry.get(), senha_entry.get()))
    botao_voltar = criar_botao(database.card_frame, "Voltar", voltar)

    botao_cadastro.pack(pady=100, padx=10)
    botao_voltar.pack(pady=150)


def atualizar_layout():
    for widget in database.card_frame.winfo_children():
        widget.pack_forget()


# Define o layout inicial (pack)
button = criar_botao(database.card_frame, "Procuro Emprego",
                     lambda: botao_emprego(1))
button2 = criar_botao(database.card_frame, "Sou Empresa",
                      lambda: botao_emprego(2))
button.pack(padx=20)
button2.pack(padx=20)

database.root.mainloop()
