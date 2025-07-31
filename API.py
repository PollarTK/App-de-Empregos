import customtkinter as ctk
import requests

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def buscar_cotacao():
    moeda = combo_moeda.get()
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    resposta = requests.get(url)
    dados = resposta.json()

    par = moeda + "BRL"
    cotacao = float(dados[par]["bid"])

    resultado.configure(text=f"1 {moeda} = R$ {cotacao:.2f}")
    
app = ctk.CTk()
app.title("Cotação de Moedas")
app.geometry("300x200")

label_titulo = ctk.CTkLabel(app, text="Cotação de Moedas", font=("Arial", 18))
label_titulo.pack(pady=10)

combo_moeda = ctk.CTkComboBox(app, values=["USD", "EUR", "BTC"])
combo_moeda.set("USD")
combo_moeda.pack(side="top")

resultado = ctk.CTkLabel(app, text="", font=("Arial", 16))
resultado.pack(pady=20)

botao = ctk.CTkButton(app, text="Ver Cotação", command=buscar_cotacao)
botao.pack(pady=10)


app.mainloop()
