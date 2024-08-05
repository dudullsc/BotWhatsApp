import tkinter as tk
from tkinter import ttk, messagebox  # Certifique-se de incluir ttk aqui
import pywhatkit as kit
import pandas as pd
import time
import re
import threading
from report import mostrar_relatorio


# Variável de controle para parar o envio
enviar = False
dados_sucesso = []
dados_falha = []

def formatar_numero(numero):
    numero = re.sub(r"[ \-\(\)]", "", numero)
    if numero.startswith("+"):
        numero = numero[1:]
    if not numero.startswith("55"):  # Substitua "55" pelo código do país aprop




        numero = "55" + numero
    return numero

def enviar_mensagens(file_path, mensagem_base, arquivo_adicional, root, barra_progresso, lbl_progresso):
    global enviar, dados_sucesso, dados_falha
    dados_sucesso = []
    dados_falha = []
    enviar = True
    mensagem_base = mensagem_base.get("1.0", tk.END).strip()
    if not mensagem_base:
        messagebox.showerror("Erro", "A mensagem não pode estar vazia.")
        return

    try:
        df = pd.read_csv(file_path)
        total = len(df)
        for index, row in df.iterrows():
            if not enviar:
                break
            nome = row['Nome']
            numero = str(row['Numero']).strip()
            numero = formatar_numero(numero)
            if not re.match(r"^\d+$", numero):
                print(f"Formato de número inválido: {numero}")
                dados_falha.append((nome, numero, "Formato de número inválido"))
                continue

            mensagem = mensagem_base.replace("{nome}", f"*{nome}*")
            try:
                if arquivo_adicional:
                    # Envia mensagem com arquivo
                    kit.sendwhats_image(
                        receiver=f"+{numero}",
                        img_path=arquivo_adicional,
                        caption=mensagem,
                        tab_close=True
                    )
                else:
                    # Envia mensagem de texto
                    kit.sendwhatmsg_instantly(f"+{numero}", mensagem, wait_time=10, tab_close=True, close_time=3)

                print(f"Mensagem enviada para {nome} ({numero})")
                time.sleep(15)  # Intervalo para evitar bloqueio do WhatsApp

                # Adiciona aos dados de sucesso
                dados_sucesso.append((nome, numero))

            except Exception as e:
                print(f"Erro ao enviar mensagem para {nome} ({numero}): {e}")
                dados_falha.append((nome, numero, str(e)))

            # Atualiza a barra de progresso
            progresso = int((index + 1) / total * 100)
            barra_progresso['value'] = progresso
            lbl_progresso.config(text=f"{progresso}% completo")

        if enviar:
            lbl_progresso.config(text="100% completo")
            messagebox.showinfo("Sucesso", "Mensagens enviadas com sucesso!")
        else:
            messagebox.showinfo("Parado", "Envio de mensagens interrompido.")

        # Mostra o relatório
        mostrar_relatorio(dados_sucesso, dados_falha)

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao enviar mensagens: {e}")
    finally:
        root.destroy()

def iniciar_envio(file_path, arquivo_adicional, mensagem, root):
    if file_path is None:
        messagebox.showerror("Erro", "Por favor, carregue uma planilha antes de iniciar o envio.")
        return

    # Cria a janela de progresso
    janela_progresso = tk.Toplevel(root)
    janela_progresso.title("Enviando Mensagens")
    janela_progresso.geometry("300x100")
    lbl_progresso = tk.Label(janela_progresso, text="0% completo")
    lbl_progresso.pack(pady=10)
    barra_progresso = ttk.Progressbar(janela_progresso, length=200, mode='determinate')
    barra_progresso.pack(pady=10)

    # Inicia o envio em uma thread separada
    threading.Thread(target=enviar_mensagens, args=(file_path, mensagem, arquivo_adicional, janela_progresso, barra_progresso, lbl_progresso)).start()

def parar_envio():
    global enviar
    enviar = False
