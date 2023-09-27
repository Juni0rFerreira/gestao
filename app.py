import tkinter as tk
from datetime import datetime, timedelta
from tkinter import *
from tkinter import ttk
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt
import os
import shutil
import locale
import uuid

resultado_simulacao_label = None
nome_locatario_entry = None  # Campo de entrada para o nome do locatário
cpf_entry = None  # Campo de entrada para CPF
rg_entry = None  # Campo de entrada para RG
data_nascimento_entry = None  # Campo de entrada para data de nascimento
logradouro_entry = None  # Campo de entrada para logradouro
numero_entry = None  # Campo de entrada para número
complemento_entry = None  # Campo de entrada para complemento
bairro_entry = None  # Campo de entrada para bairro
estado_entry = None  # Campo de entrada para estado
cidade_entry = None  # Campo de entrada para cidade
data_inicial_entry = None  # Campo de entrada para data inicial
cep_entry = None
email_entry = None  # Corrigido o nome da variável

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')


def fazer_login():
    nome_de_usuario = nome_entry.get()
    senha = senha_entry.get()

    if nome_de_usuario == "admin" and senha == "admin":
        resultado_label.config(text="Login bem-sucedido! Bem-vindo!")
        janela_login.destroy()
        criar_tela_home()
    else:
        resultado_label.config(text="Login falhou. Tente novamente.")

def calcular_data_saida(data_inicial, meses):
    data_formato = "%d/%m/%Y"
    data_inicio = datetime.strptime(data_inicial, data_formato)
    data_saida = data_inicio + timedelta(days=30 * int(meses))
    return data_saida.strftime(data_formato)

def criar_tela_home():
    global resultado_simulacao_label
    global nome_locatario_entry
    global cpf_entry
    global rg_entry
    global data_nascimento_entry
    global logradouro_entry
    global numero_entry
    global complemento_entry
    global bairro_entry
    global estado_entry
    global cidade_entry
    global data_inicial_entry
    global cep_entry
    global email_entry  # Corrigido o nome da variável

    janela_home = tk.Tk()
    janela_home.title("Tela Home")
    janela_home.geometry("1500x900")

    bem_vindo_label = tk.Label(janela_home, text="Bem-vindo à Simulação!")
    bem_vindo_label.grid(row=0, column=0, columnspan=2, pady=10)

    valor_aluguel_label = tk.Label(janela_home, text="Digite o valor do aluguel:")
    valor_aluguel_label.grid(row=1, column=0, padx=10, sticky="e")
    
    valor_aluguel_entry = tk.Entry(janela_home)
    valor_aluguel_entry.grid(row=1, column=1)

    meses_label = tk.Label(janela_home, text="Digite a quantidade de meses:")
    meses_label.grid(row=2, column=0, padx=10, sticky="e")
    
    meses_entry = tk.Entry(janela_home)
    meses_entry.grid(row=2, column=1)

    data_inicial_label = tk.Label(janela_home, text="Data de Entrada (dd/mm/aaaa):")
    data_inicial_label.grid(row=3, column=0, padx=10, sticky="e")
    
    data_inicial_entry = tk.Entry(janela_home)
    data_inicial_entry.grid(row=3, column=1)

    bem_vindo_label = tk.Label(janela_home, text="Dados do Locatário")
    bem_vindo_label.grid(row=4, column=0, columnspan=2, pady=10)

    nome_locatario_label = tk.Label(janela_home, text="Nome do Locatário:")
    nome_locatario_label.grid(row=5, column=0, padx=10, sticky="e")
    
    nome_locatario_entry = tk.Entry(janela_home)
    nome_locatario_entry.grid(row=5, column=1)

    cpf_label = tk.Label(janela_home, text="CPF:")
    cpf_label.grid(row=7, column=0, padx=10, sticky="e")
    
    cpf_entry = tk.Entry(janela_home)
    cpf_entry.grid(row=7, column=1)

    rg_label = tk.Label(janela_home, text="RG:")
    rg_label.grid(row=7, column=2, padx=10, sticky="e")
    
    rg_entry = tk.Entry(janela_home)
    rg_entry.grid(row=7, column=3)

    data_nascimento_label = tk.Label(janela_home, text="Data de Nascimento:")
    data_nascimento_label.grid(row=7, column=4, padx=10, sticky="e")
    
    data_nascimento_entry = tk.Entry(janela_home)
    data_nascimento_entry.grid(row=7, column=5)

    logradouro_label = tk.Label(janela_home, text="Logradouro:")
    logradouro_label.grid(row=9, column=0, padx=10, sticky="e")
    
    logradouro_entry = tk.Entry(janela_home)
    logradouro_entry.grid(row=9, column=1)

    numero_label = tk.Label(janela_home, text="Número:")
    numero_label.grid(row=9, column=2, padx=10, sticky="e")
    
    numero_entry = tk.Entry(janela_home)
    numero_entry.grid(row=9, column=3)

    complemento_label = tk.Label(janela_home, text="Complemento:")
    complemento_label.grid(row=9, column=4, padx=10, sticky="e")

    complemento_entry = tk.Entry(janela_home)
    complemento_entry.grid(row=9, column=5)

    cep_label = tk.Label(janela_home, text="CEP:")
    cep_label.grid(row=9, column=6, padx=10, sticky="e")

    cep_entry = tk.Entry(janela_home)
    cep_entry.grid(row=9, column=7)

    bairro_label = tk.Label(janela_home, text="Bairro:")
    bairro_label.grid(row=10, column=0, padx=10, sticky="e")

    bairro_entry = tk.Entry(janela_home)
    bairro_entry.grid(row=10, column=1)

    # Lista Estado
    listEstados = ["RJ", "SP", "ES", "MG", "PR", "SC", "RS", "MS", "GO", "AC", "AL", "AP", "AM", "BA", "CE", "DF", "MA", "MT", "PA", "PB", "PE", "PI", "RN", "RO", "RR", "SE", "TO"]

    estado_label = tk.Label(janela_home, text="Estado:")
    estado_label.grid(row=10, column=2, padx=10, sticky="e")

    estado_entry = ttk.Combobox(janela_home, value=listEstados)
    estado_entry.grid(row=10, column=3) 

    # Lista Cidade
    listCidades = []

    cidade_label = tk.Label(janela_home, text="Cidade:")
    cidade_label.grid(row=10, column=4, padx=10, sticky="e")
    
    cidade_entry = tk.Entry(janela_home)
    cidade_entry.grid(row=10, column=5)

    email_label = tk.Label(janela_home, text="E-mail:")
    email_label.grid(row=11, column=0, padx=10, sticky="e")
    
    email_entry = tk.Entry(janela_home)  # Corrigido o nome da variável
    email_entry.grid(row=11, column=1)

    simular_button = tk.Button(janela_home, text="Simular", command=lambda: simular_aluguel(valor_aluguel_entry.get(), meses_entry.get(), data_inicial_entry.get()))
    simular_button.grid(row=12, column=5, padx=10)

    gerar_contrato_button = tk.Button(janela_home, text="Gerar Contrato", command=lambda: gerar_contrato(valor_aluguel_entry.get(), meses_entry.get(), data_inicial_entry.get()))
    gerar_contrato_button.grid(row=13, column=5, padx=10)

    resultado_simulacao_label = tk.Label(janela_home, text="Venda não Simulada!")
    resultado_simulacao_label.grid(row=14, column=5, padx=10)

    janela_home.mainloop()

def simular_aluguel(valor, meses, data_inicial):
    global resultado_simulacao_label

    try:
        valor = float(valor)
        meses = int(meses)
        data_saida = calcular_data_saida(data_inicial, meses)
        resultado = f"Simulação de aluguel realizada com sucesso!\nValor do aluguel: R${valor:.2f}\n Data de Entrada: {data_inicial}\nData de Saída: {data_saida}"
        resultado_simulacao_label.config(text=resultado)
    except ValueError:
        resultado_simulacao_label.config(text="Por favor, insira valores válidos.")

def gerar_contrato(valor, meses, data_inicial):
    global resultado_simulacao_label

    try:
        valor = float(valor)
        meses = int(meses)
        data_saida = calcular_data_saida(data_inicial, meses)

        # Carregue o modelo do contrato
        modelo_contrato = Document("contratomodelopf.docx")  # Substitua pelo caminho do seu modelo

        # Dicionário de tags e valores a serem substituídos
        tags_e_valores = {
            "<NOME_LOCATARIO>": nome_locatario_entry.get(),
            "<CPF>": cpf_entry.get(),
            "<RG>": rg_entry.get(),
            "<VALOR_ALUGUEL>": f'R${valor:.2f} por mês',
            "<DATA_INICIAL>": data_inicial,
            "<DATA_SAIDA>": data_saida,
            "<LOGRADOURO>": logradouro_entry.get(),
            "<NUMERO>": numero_entry.get(),
            "<COMPLEMENTO>": complemento_entry.get(),
            "<BAIRRO>": bairro_entry.get(),
            "<ESTADO>": estado_entry.get(),
            "<CIDADE>": cidade_entry.get(),
            "<CEP>": cep_entry.get(),
            "<EMAIL>": email_entry.get(),  # Corrigido o nome da variável
            # Adicione mais tags e valores conforme necessário
        }

        # Substitua as tags pelo valor correspondente no modelo
        for paragrafo in modelo_contrato.paragraphs:
            for tag, valor in tags_e_valores.items():
                if tag in paragrafo.text:
                    paragrafo.text = paragrafo.text.replace(tag, valor)

        # Gerar um nome de arquivo único e aleatório usando UUID
        nome_arquivo = str(uuid.uuid4())[:8] + '_contrato_aluguel.docx'

        # Salvar o contrato gerado em um arquivo
        modelo_contrato.save(nome_arquivo)

        # Obter o diretório de downloads do usuário
        pasta_downloads = os.path.expanduser("~\\Downloads")

        # Mover o arquivo para a pasta de downloads
        shutil.move(nome_arquivo, os.path.join(pasta_downloads, nome_arquivo))

        resultado_simulacao_label.config(text="Contrato gerado com sucesso. Verifique a pasta de downloads.")

    except ValueError:
        resultado_simulacao_label.config(text="Por favor, insira valores válidos.")

janela_login = tk.Tk()
janela_login.title("Tela de Login")
janela_login.geometry("1500x900")

titulo_label = tk.Label(janela_login, text="Bem-vindo ao Sistema de Login")
titulo_label.pack(pady=10)

nome_label = tk.Label(janela_login, text="Nome de Usuário:")
nome_label.pack()
nome_entry = tk.Entry(janela_login)
nome_entry.pack()

senha_label = tk.Label(janela_login, text="Senha:")
senha_label.pack()
senha_entry = tk.Entry(janela_login, show="*")
senha_entry.pack()

botao_login = tk.Button(janela_login, text="Login", command=fazer_login)
botao_login.pack(pady=10)

resultado_label = tk.Label(janela_login, text="")
resultado_label.pack()

janela_login.mainloop()
