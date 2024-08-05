from tkinter import filedialog, messagebox
import pandas as pd

def definir_icone(janela):
    try:
        janela.iconbitmap("img/favicon.ico")  # Substitua "caminho/do/icone.ico" pelo caminho do seu ícone
    except Exception as e:
        print(f"Erro ao definir ícone: {e}")

def carregar_planilha():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    return file_path

def carregar_arquivo_adicional():
    arquivo_adicional = filedialog.askopenfilename(
        filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.gif"), ("Todos os arquivos", "*.*")])
    return arquivo_adicional

def gerar_planilha_exemplo():
    dados = {
        "Nome": ["Eduardo", "Julio"],
        "Numero": ["+5548988593816", "+55482222222222"]
    }
    df = pd.DataFrame(dados)
    caminho = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if caminho:
        df.to_csv(caminho, index=False)
        messagebox.showinfo("Sucesso", f"Planilha de exemplo salva em: {caminho}")

def converter_xlsx_para_csv():
    caminho_xlsx = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if not caminho_xlsx:
        return

    df = pd.read_excel(caminho_xlsx, dtype={'Numero': str})  # Tratar a coluna 'Numero' como texto
    caminho_csv = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if caminho_csv:
        df.to_csv(caminho_csv, index=False)
        messagebox.showinfo("Sucesso", f"Arquivo convertido e salvo em: {caminho_csv}")
