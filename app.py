import customtkinter,tkinter

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


def botao_emprego(tipo):
    atualizar_layout()
    database.verificacao = tipo
    botao_login = criar_botao(
        database.card_frame, "Login", lambda: login(database.verificacao))
    botao_cadastro = criar_botao(
        database.card_frame, "Cadastro", lambda: cadastrar(database.verificacao))
    botao_voltar = criar_botao(database.card_frame, "Voltar", voltar)

    botao_login.pack(pady=10)
    botao_cadastro.pack(pady=10)
    botao_voltar.pack(pady=10)


def login(verificacao):
    atualizar_layout()
    email_entry = criar_entry(database.card_frame, "Email")
    senha_entry = criar_entry(database.card_frame, "Senha", show="*")
    email_entry.pack(pady=20, padx=20)
    senha_entry.pack(pady=20, padx=20)

    botao_login = criar_botao(database.card_frame, "Login", lambda: realizar_login(
        verificacao, email_entry.get(), senha_entry.get()))
    botao_voltar = criar_botao(database.card_frame, "Voltar", voltar)

    botao_login.pack(pady=10)
    botao_voltar.pack(pady=10)


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
    global existe
    existe = database.buscar_curriculo(database.email_usuario_logado)
    if database.verificacao == 1:
        if not existe or existe == None:
            nome_entry = criar_entry(database.card_frame, "Nome")
            contato_entry = criar_entry(database.card_frame, "Contato")
            endereco_entry = criar_entry(database.card_frame, "Endereço")

            horarios = customtkinter.CTkComboBox(master=database.card_frame, values=[
                                                "Qualquer", "Integral", "Manhã", "Tarde", "Noite"])
            escolaridade = customtkinter.CTkComboBox(master=database.card_frame, values=[
                                                    "Ensino Fundamental Incompleto", "Ensino Fundamental Completo", "Ensino Médio Incompleto", "Ensino Médio Completo", "Técnico Incompleto", "Técnico Completo", "Graduação Incompleta", "Graduação Completa"])

            botao_voltar_home = criar_botao(database.card_frame, "Voltar", voltar_home)
            botao_criar = criar_botao(database.card_frame, "Criar Currículo",
                lambda: criar_curriculo(nome_entry.get(), contato_entry.get(),endereco_entry.get(), horarios.get(), escolaridade.get(), checagem=0))
        else:
            for dados in existe:
                nome_entry = criar_entry(database.card_frame, f"{dados[1]}")
                contato_entry = criar_entry(database.card_frame, f"{dados[2]}")
                endereco_entry = criar_entry(database.card_frame, f"{dados[3]}")

            horarios = customtkinter.CTkComboBox(master=database.card_frame, values=[
                                                    "Qualquer", "Integral", "Manhã", "Tarde", "Noite"])
            escolaridade = customtkinter.CTkComboBox(master=database.card_frame, values=[
                                                        "Ensino Fundamental Incompleto", "Ensino Fundamental Completo", "Ensino Médio Incompleto", "Ensino Médio Completo", "Técnico Incompleto", "Técnico Completo", "Graduação Incompleta", "Graduação Completa"])

            botao_voltar_home = criar_botao(database.card_frame, "Voltar", voltar_home)
            botao_criar = criar_botao(
                database.card_frame, "Editar Currículo",
                lambda: criar_curriculo(nome_entry.get(), contato_entry.get(),endereco_entry.get(), horarios.get(),escolaridade.get(), checagem=1))

        nome_entry.pack(pady=20, padx=20)
        contato_entry.pack(pady=20, padx=20)
        endereco_entry.pack(pady=20, padx=20)
        horarios.pack(padx=20, pady=20)
        escolaridade.pack(pady=20, padx=20)
        botao_criar.pack(pady=20)
        botao_voltar_home.pack(padx=20)
    else:
        nome_entry = criar_entry(database.card_frame, "Nome")
        requisitos_entry = customtkinter.CTkComboBox(master=database.card_frame, values=[
                                                "Ensino Fundamental Incompleto", "Ensino Fundamental Completo", "Ensino Médio Incompleto", "Ensino Médio Completo", "Técnico Incompleto", "Técnico Completo", "Graduação Incompleta", "Graduação Completa"])
        disponibilidade_entry = customtkinter.CTkComboBox(master=database.card_frame, values=[
                                            "Qualquer", "Integral", "Manhã", "Tarde", "Noite"])
        salario_entry = criar_entry(database.card_frame, "salario")
        
        botao_voltar_home = criar_botao(database.card_frame, "Voltar", voltar_home)
        botao_criar = criar_botao(database.card_frame, "Criar Vaga", lambda: criar_vaga(
            nome_entry.get(), requisitos_entry.get(), disponibilidade_entry.get(), salario_entry.get()))

        nome_entry.pack(pady=20, padx=20)
        requisitos_entry.pack(pady=20, padx=20)
        disponibilidade_entry.pack(pady=20, padx=20)
        salario_entry.pack(padx=20, pady=20)
        botao_criar.pack(pady=20)
        botao_voltar_home.pack(padx=20)


def filtro_busca():
    atualizar_layout()
    filtro = criar_entry(database.card_frame, "O que está buscando?")
    buscar = criar_botao(database.card_frame, "Buscar", lambda: mostrar_resultados_filtro(filtro.get()))
    filtro.pack(pady=20)
    buscar.pack(pady=20)

def mostrar_resultados_filtro(termo):
    vagas = database.filtrar_vagas_por_termo(termo)
    ids = [vaga[0] for vaga in vagas]
    ids_filtrados = ids

    atualizar_layout()
    botao_voltar = criar_botao(database.card_frame, "Voltar", voltar_home)
    database.card_busca_title.pack(pady=20, side="top")
    if not vagas or vagas == None:
        frame_vagas = customtkinter.CTkFrame(database.card_frame)
        frame_vagas.pack(pady=10)
        requisitos = customtkinter.CTkLabel(
                frame_vagas, text="Nenhuma Vaga Encontrada, Verifique se foi digitado corretamente.")
        requisitos.pack(side="top", pady=5)
        botao_voltar.pack(pady=10)
    else:
        for vaga in vagas:
            # crie cards como no botao_curriculo
            frame_vagas = customtkinter.CTkFrame(database.card_frame)
            frame_vagas.pack(pady=10)
            card_vaga = customtkinter.CTkScrollableFrame(frame_vagas, border_width=2, width=500, height=200, border_color="green",
                                                corner_radius=10)
            card_vaga.pack(pady=5)
            nome_vaga = customtkinter.CTkLabel(
                card_vaga, text=f"Vaga: {vaga[1]}")
            nome_vaga.pack(side="top", pady=5)
            requisitos = customtkinter.CTkLabel(
                    card_vaga, text=f"Requisitos: {vaga[2]}")
            requisitos.pack(side="top", pady=5)
                
            disponibilidade = customtkinter.CTkLabel(
                    card_vaga, text=f"Disponibilidade: {vaga[3]}")
            disponibilidade.pack(side="top", pady=5)
                
            salario = customtkinter.CTkLabel(
                    card_vaga, text=f"Salário: {vaga[4]}")
            salario.pack(side="top", pady=5)
                
                # Passa o ID da vaga para a função candidatar
            botao_candidatar = criar_botao(card_vaga, "Candidatar-se", lambda vaga=vaga: database.candidatar(vaga))
            botao_candidatar.pack(side="top")
                
        botao_voltar.pack(pady=10)
        botao_cand_todas = criar_botao(database.card_frame, "Candidatar Todas", lambda: database.candidatar_vagas_por_ids(ids_filtrados))
        botao_cand_todas.pack(pady=20,side="top")

def botao_curriculo():
    botao_logout = criar_botao(database.card_frame, "Logout", voltar)
    if database.verificacao == 1:
        existe = database.buscar_curriculo(database.email_usuario_logado)
        if not existe or existe == None:
            botao_criar = criar_botao(
                database.card_frame, "Criar Currículo", inputs_curriculo)
        else:
            botao_criar = criar_botao(
                database.card_frame, "Editar Currículo", inputs_curriculo)
            
        criar_buscar = criar_botao(
            database.card_frame, "Buscar Vagas", filtro_busca)
        botao_criar.pack(pady=20)
        criar_buscar.pack(pady=20)
        # Frame para conter os cards de vagas
        frame_vagas = customtkinter.CTkFrame(database.card_frame)
        frame_vagas.pack(pady=10)
        busca = database.buscar_vagas(database.email_usuario_logado)
        for vaga in busca:
            # Cria um novo card para cada vaga
            card_vaga = customtkinter.CTkScrollableFrame(frame_vagas, border_width=2, width=500, height=200, border_color="green",
                                            corner_radius=10)
            card_vaga.pack(pady=5)
            nome_vaga = customtkinter.CTkLabel(
                card_vaga, text=f"Vaga: {vaga[1]}")
            nome_vaga.pack(side="top", pady=5)
            requisitos = customtkinter.CTkLabel(
                card_vaga, text=f"Requisitos: {vaga[2]}")
            requisitos.pack(side="top", pady=5)
            
            disponibilidade = customtkinter.CTkLabel(
                card_vaga, text=f"Disponibilidade: {vaga[3]}")
            disponibilidade.pack(side="top", pady=5)
            
            salario = customtkinter.CTkLabel(
                card_vaga, text=f"Salário: {vaga[4]}")
            salario.pack(side="top", pady=5)
            
            # Passa o ID da vaga para a função candidatar
            botao_candidatar = criar_botao(card_vaga, "Candidatar-se", lambda vaga=vaga: database.candidatar(vaga))
            botao_candidatar.pack(side="top")
            
        botao_logout.pack(pady=10)
    else:
        botao_criar = criar_botao(
            database.card_frame, "Criar Vaga", inputs_curriculo)
        botao_criar.pack(side="top",pady=20)
        botao_logout.pack(side="top",pady=10)
        # Frame para conter os cards de vagas
        frame_vagas = customtkinter.CTkFrame(database.card_frame)
        frame_vagas.pack(pady=10)
        busca = database.buscar_vagas(database.email_usuario_logado)
        for vaga in busca:
            # Cria um novo card para cada vaga
            card_vaga = customtkinter.CTkScrollableFrame(frame_vagas, border_width=2, width=500, height=200, border_color="green",
                                            corner_radius=10)
            card_vaga.pack(pady=5)
            nome_vaga = customtkinter.CTkLabel(
                card_vaga, text=f"Vaga: {vaga[1]}")
            nome_vaga.pack(side="top", pady=5)
            requisitos = customtkinter.CTkLabel(
                card_vaga, text=f"Requisitos: {vaga[2]}")
            requisitos.pack(side="top", pady=5)
            
            disponibilidade = customtkinter.CTkLabel(
                card_vaga, text=f"Disponibilidade: {vaga[3]}")
            disponibilidade.pack(side="top", pady=5)
            
            salario = customtkinter.CTkLabel(
                card_vaga, text=f"Salário: {vaga[4]}")
            salario.pack(side="top", pady=5)
            
            botao_candidados = criar_botao(card_vaga, "Ver Candidatos", lambda: database.buscar_candidatos(database.email_usuario_logado))
            botao_candidados.pack(side="top")
            


def criar_curriculo(nome, contato, endereco, horarios, escolaridade, checagem):
    email_usuario = database.email_usuario_logado
    if not all([nome, contato, endereco, horarios, escolaridade]):
        database.mensagem("Por favor, preencha todos os campos.")
        return
    
    if checagem == 0:
        database.criar_curriculo(nome, contato, endereco,
                                horarios, escolaridade, email_usuario)
    else:
        database.editar_curriculo(nome, contato, endereco,
                                horarios, escolaridade, email_usuario)
        
    
def criar_vaga(nome, requisitos, disponibilidade, salario):
    email_usuario = database.email_usuario_logado
    if not all([nome, requisitos, disponibilidade, salario]):
        database.mensagem("Por favor, preencha todos os campos.")        
        return
    database.criar_vaga(nome, requisitos, disponibilidade, salario, email_usuario)

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

    botao_cadastro.pack(pady=10)
    botao_voltar.pack(pady=10)


def atualizar_layout():
    for widget in database.card_frame.winfo_children():
        widget.pack_forget()

def voltar():
    atualizar_layout()
    database.email_usuario_logado = None
    card_frame = database.card_frame
    card_frame._parent_canvas.yview_moveto(0.0)
    database.card_title.pack(pady=20, side="top")
    button.pack(pady=10,padx=20)
    button2.pack(pady=10,padx=20)


def voltar_home():
    atualizar_layout()
    card_frame = database.card_frame
    card_frame._parent_canvas.yview_moveto(0.0)
    database.card_home_title.pack(pady=10, anchor="center")
    botao_curriculo()


# Define o layout inicial (pack)
button = criar_botao(database.card_frame, "Procuro Emprego",
                     lambda: botao_emprego(1))
button2 = criar_botao(database.card_frame, "Sou Empresa",
                      lambda: botao_emprego(2))
button.pack(pady=10,padx=20)
button2.pack(pady=10,padx=20)

database.root.mainloop()
