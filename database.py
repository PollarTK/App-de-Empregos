import customtkinter
import tkinter.messagebox
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

customtkinter.set_default_color_theme("blue")

# Configurações do banco de dados
DB_NAME = "Banco.db"
TABLES = {
    "empregados": "CREATE TABLE IF NOT EXISTS empregados (email TEXT PRIMARY KEY, nome TEXT, senha TEXT)",
    "empregadores": "CREATE TABLE IF NOT EXISTS empregadores (email TEXT PRIMARY KEY, nome TEXT, senha TEXT)",
    "curriculo": "CREATE TABLE IF NOT EXISTS Curriculo (id INTEGER PRIMARY KEY, nome TEXT, contato INTEGER, endereco TEXT, horarios TEXT, escolaridade TEXT, email_usuario TEXT, FOREIGN KEY(email_usuario) REFERENCES empregados(email))",
    "vaga": "CREATE TABLE IF NOT EXISTS Vaga (id INTEGER PRIMARY KEY, nome TEXT, requisitos TEXT, disponibilidade INTEGER, salario REAL, email_usuario TEXT, FOREIGN KEY(email_usuario) REFERENCES empregadores(email))",
    "candidatos": "CREATE TABLE IF NOT EXISTS Candidatos (id INTEGER PRIMARY KEY, candidato_nome TEXT, candidato_email TEXT, FOREIGN KEY (candidato_nome) REFERENCES empregados(nome), FOREIGN KEY (candidato_email) REFERENCES empregados(email))"
}

root = customtkinter.CTk()
root.geometry("800x400")
verificacao = 0
email_usuario_logado = None

# Frames e Labels
card_frame = customtkinter.CTkScrollableFrame(
    root, border_width=2, width=600, height=450, border_color="green", corner_radius=20)

card_title = customtkinter.CTkLabel(card_frame, text="📝 Escolha uma Opção", font=(
    "Arial", 16, "bold"), text_color="#4ECB71")

card_home_title = customtkinter.CTkLabel(
    card_frame, text="Buscando Emprego? Crie seu Currículo!", font=("Arial", 16, "bold"), text_color="#4ECB71")

card_vaga = customtkinter.CTkFrame(card_frame, border_width=2, border_color="green",
                                   corner_radius=20)

card_title.pack(pady=(10, 20), anchor="center")
card_frame.pack(pady=(10, 20), anchor="center")


def mensagem(texto):
    tkinter.messagebox.showinfo("Mensagem", texto)


def conectar_banco():
    return sqlite3.connect(DB_NAME)


def executar_sql(sql, params=()):
    with conectar_banco() as conexao:
        cursor = conexao.cursor()
        cursor.execute(sql, params)
        conexao.commit()
        return cursor


def criar_tabelas():
    for table, sql in TABLES.items():
        executar_sql(sql)


def empresas_aleatorias():
    empresas = [
        ("empresa1@gmail.com", "Simas Turbo", "123"),
        ("techjobs@empresa.com", "Tech Jobs", "123"),
        ("vagasrh@empresa.com", "Vagas RH", "123"),
        ("construtora@concreto.com", "Construtora Concreto", "123"),
        ("hospitalvida@saude.com", "Hospital Vida", "123")
    ]
    vagas = [
        ("Assistente de mão", "Ensino Médio Incompleto",
         "Qualquer", 1200, "empresa1@gmail.com"),
        ("Desenvolvedor Júnior", "Técnico",
         "Integral", 3000, "techjobs@empresa.com"),
        ("Auxiliar Administrativo", "Ensino Médio Completo",
         "Manhã", 1800, "vagasrh@empresa.com"),
        ("Pedreiro", "Ensino Médio Completo",
         "Integral", 2500, "construtora@concreto.com"),
        ("Enfermeiro", "Técnico",
         "Integral", 4000, "hospitalvida@saude.com")
    ]

    for email, nome, senha in empresas:
        executar_sql("INSERT INTO empregadores(email, nome, senha) VALUES (?, ?, ?)",
                     (email, nome, generate_password_hash(senha)))

    for nome, requisitos, disponibilidade, salario, email_usuario in vagas:
        executar_sql("INSERT INTO vaga(nome, requisitos, disponibilidade, salario, email_usuario) VALUES (?, ?, ?, ?, ?)",
                     (nome, requisitos, disponibilidade, salario, email_usuario))


def verificar_email(email, tabela):
    cursor = executar_sql(
        f"SELECT COUNT(email) FROM {tabela} WHERE email=?", (email,))
    return cursor.fetchone()[0] > 0


def criar_conta(verificacao, email, nome, senha):
    tabela = "empregados" if verificacao == 1 else "empregadores"
    if verificar_email(email, tabela):
        mensagem("LOG: Email Já Cadastrado.")
        return

    senha_criptografada = generate_password_hash(senha)
    executar_sql(f"INSERT INTO {tabela}(email, nome, senha) VALUES (?, ?, ?)",
                 (email, nome, senha_criptografada))
    mensagem("Usuário Cadastrado Com Sucesso!")


def login(verificacao, email, senha):
    tabela = "empregados" if verificacao == 1 else "empregadores"
    if not verificar_email(email, tabela):
        mensagem("LOG: Email não encontrado.")
        return False

    cursor = executar_sql(
        f"SELECT senha FROM {tabela} WHERE email=?", (email,))
    senha_criptografada = cursor.fetchone()
    if senha_criptografada and check_password_hash(senha_criptografada[0], senha):
        global email_usuario_logado
        email_usuario_logado = email
        mensagem("Usuário Logado Com Sucesso!")
        return True

    mensagem("LOG: Senha incorreta.")
    return False


def criar_curriculo(nome, contato, endereco, horarios, escolaridade, email):
    executar_sql('''INSERT INTO curriculo (nome, contato, endereco, horarios, escolaridade, email_usuario) VALUES (?, ?, ?, ?, ?, ?)''',
                 (nome, contato, endereco, horarios, escolaridade, email))
    mensagem("Currículo Criado Com Sucesso!")


def buscar_vagas():
    cursor = executar_sql('SELECT * FROM vaga')
    return cursor.fetchall()


if __name__ == "__main__":
    criar_tabelas()
    empresas_aleatorias()
