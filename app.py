import tkinter as tk
from datetime import datetime, timedelta
from docx import Document
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

    janela_home = tk.Tk()
    janela_home.title("Tela Home")
    janela_home.geometry("400x600")  # Aumentamos a altura da janela para acomodar os novos campos

    bem_vindo_label = tk.Label(janela_home, text="Bem-vindo à Tela Home!")
    bem_vindo_label.pack(pady=10)

    valor_aluguel_label = tk.Label(janela_home, text="Digite o valor do aluguel:")
    valor_aluguel_label.pack()
    
    valor_aluguel_entry = tk.Entry(janela_home)
    valor_aluguel_entry.pack()

    meses_label = tk.Label(janela_home, text="Digite a quantidade de meses:")
    meses_label.pack()
    
    meses_entry = tk.Entry(janela_home)
    meses_entry.pack()

    data_inicial_label = tk.Label(janela_home, text="Data de Entrada (dd/mm/aaaa):")
    data_inicial_label.pack()
    
    data_inicial_entry = tk.Entry(janela_home)
    data_inicial_entry.pack()

    nome_locatario_label = tk.Label(janela_home, text="Nome do Locatário:")
    nome_locatario_label.pack()
    
    nome_locatario_entry = tk.Entry(janela_home)
    nome_locatario_entry.pack()

    cpf_label = tk.Label(janela_home, text="CPF:")
    cpf_label.pack()
    
    cpf_entry = tk.Entry(janela_home)
    cpf_entry.pack()

    rg_label = tk.Label(janela_home, text="RG:")
    rg_label.pack()
    
    rg_entry = tk.Entry(janela_home)
    rg_entry.pack()

    data_nascimento_label = tk.Label(janela_home, text="Data de Nascimento (dd/mm/aaaa):")
    data_nascimento_label.pack()
    
    data_nascimento_entry = tk.Entry(janela_home)
    data_nascimento_entry.pack()

    logradouro_label = tk.Label(janela_home, text="Logradouro:")
    logradouro_label.pack()
    
    logradouro_entry = tk.Entry(janela_home)
    logradouro_entry.pack()

    numero_label = tk.Label(janela_home, text="Número:")
    numero_label.pack()
    
    numero_entry = tk.Entry(janela_home)
    numero_entry.pack()

    complemento_label = tk.Label(janela_home, text="Complemento:")
    complemento_label.pack()
    
    complemento_entry = tk.Entry(janela_home)
    complemento_entry.pack()

    bairro_label = tk.Label(janela_home, text="Bairro:")
    bairro_label.pack()
    
    bairro_entry = tk.Entry(janela_home)
    bairro_entry.pack()

    estado_label = tk.Label(janela_home, text="Estado:")
    estado_label.pack()
    
    estado_entry = tk.Entry(janela_home)
    estado_entry.pack()

    cidade_label = tk.Label(janela_home, text="Cidade:")
    cidade_label.pack()
    
    cidade_entry = tk.Entry(janela_home)
    cidade_entry.pack()

    simular_button = tk.Button(janela_home, text="Simular", command=lambda: simular_aluguel(valor_aluguel_entry.get(), meses_entry.get(), data_inicial_entry.get()))
    simular_button.pack(pady=10)

    resultado_simulacao_label = tk.Label(janela_home, text="")
    resultado_simulacao_label.pack()

    gerar_contrato_button = tk.Button(janela_home, text="Gerar Contrato", command=lambda: gerar_contrato(valor_aluguel_entry.get(), meses_entry.get(), data_inicial_entry.get()))
    gerar_contrato_button.pack(pady=10)

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

        # Criar um novo documento Word (DOCX)
        doc = Document()

        # Adicionar título ao contrato
        doc.add_heading('Contrato de Aluguel', 0)

        # Adicionar informações ao contratom
        doc.add_paragraph(f"Locador: [Nome do Locador]")
        doc.add_paragraph(f"Locatário: {nome_locatario_entry.get()}")
        doc.add_paragraph(f"CPF: {cpf_entry.get()}")
        doc.add_paragraph(f"RG: {rg_entry.get()}")
        doc.add_paragraph(f"Data de Nascimento: {data_nascimento_entry.get()}")
        doc.add_paragraph(f"Logradouro: {logradouro_entry.get()}")
        doc.add_paragraph(f"Número: {numero_entry.get()}")
        doc.add_paragraph(f"Complemento: {complemento_entry.get()}")
        doc.add_paragraph(f"Bairro: {bairro_entry.get()}")
        doc.add_paragraph(f"Estado: {estado_entry.get()}")
        doc.add_paragraph(f"Cidade: {cidade_entry.get()}")
        doc.add_paragraph(f"Valor do Aluguel: R${valor:.2f} por mês")
        doc.add_paragraph(f"Data de Início: {data_inicial}")
        doc.add_paragraph(f"Data de Saída: {data_saida}")

        # Adicionar a data de hoje formatada como "dia de mês de ano" em pt-BR
        hoje = datetime.now().strftime("%d de %B de %Y")
        doc.add_paragraph(f"São José do Rio Preto, {hoje}").alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

        # Adicionar espaço em branco para a assinatura do cliente
        doc.add_paragraph("\n\n\n\n")
        doc.add_paragraph("_________________________________________________").alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        doc.add_paragraph("LOCADOR").alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        doc.add_paragraph("\n\n")
        doc.add_paragraph("_________________________________________________").alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        doc.add_paragraph(f"{nome_locatario_entry.get()}").alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

        # Gerar um nome de arquivo único e aleatório usando UUID
        nome_arquivo = str(uuid.uuid4())[:8] + '_contrato_aluguel.docx'

        # Salvar o contrato em um arquivo
        doc.save(nome_arquivo)

        # Obter o diretório de downloads do usuário
        pasta_downloads = os.path.expanduser("~\\Downloads")

        # Mover o arquivo para a pasta de downloads
        shutil.move(nome_arquivo, os.path.join(pasta_downloads, nome_arquivo))

        resultado_simulacao_label.config(text="Contrato gerado com sucesso. Verifique a pasta de downloads.")

    except ValueError:
        resultado_simulacao_label.config(text="Por favor, insira valores válidos.")

janela_login = tk.Tk()
janela_login.title("Tela de Login")
janela_login.geometry("300x250")

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
