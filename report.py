import tkinter as tk
from tkinter import filedialog

def salvar_relatorio(dados_sucesso, dados_falha):
    caminho = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if caminho:
        with open(caminho, 'w') as f:
            f.write("Relatório de Envio de Mensagens\n")
            f.write(f"Mensagens enviadas com sucesso: {len(dados_sucesso)}\n")
            for nome, num in dados_sucesso:
                f.write(f"Sucesso: {nome} ({num})\n")
            f.write(f"Mensagens não enviadas: {len(dados_falha)}\n")
            for nome, num, erro in dados_falha:
                f.write(f"Falha: {nome} ({num}) - Erro: {erro}\n")
        messagebox.showinfo("Sucesso", f"Relatório salvo em: {caminho}")

def mostrar_relatorio(dados_sucesso, dados_falha):
    janela_relatorio = tk.Toplevel()
    janela_relatorio.title("Relatório de Envio")
    janela_relatorio.geometry("450x650")  # Aumentando a altura da janela

    lbl_sucesso = tk.Label(janela_relatorio, text=f"Mensagens enviadas com sucesso: {len(dados_sucesso)}")
    lbl_sucesso.pack(pady=10)

    frame_sucesso = tk.Frame(janela_relatorio)
    frame_sucesso.pack(fill=tk.BOTH, expand=True, padx=10, pady=1)
    scrollbar_sucesso = tk.Scrollbar(frame_sucesso)
    scrollbar_sucesso.pack(side=tk.RIGHT, fill=tk.Y)
    lista_sucesso = tk.Listbox(frame_sucesso, height=10, yscrollcommand=scrollbar_sucesso.set)
    lista_sucesso.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar_sucesso.config(command=lista_sucesso.yview)
    for nome, num in dados_sucesso:
        lista_sucesso.insert(tk.END, f"{nome} ({num})")

    lbl_falha = tk.Label(janela_relatorio, text=f"Mensagens não enviadas: {len(dados_falha)}")
    lbl_falha.pack(pady=10)

    frame_falha = tk.Frame(janela_relatorio)
    frame_falha.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
    scrollbar_falha = tk.Scrollbar(frame_falha)
    scrollbar_falha.pack(side=tk.RIGHT, fill=tk.Y)
    lista_falha = tk.Listbox(frame_falha, height=10, yscrollcommand=scrollbar_falha.set)
    lista_falha.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar_falha.config(command=lista_falha.yview)
    for nome, num, erro in dados_falha:
        lista_falha.insert(tk.END, f"{nome} ({num}) - Erro: {erro}")

    frame_botoes_relatorio = tk.Frame(janela_relatorio)
    frame_botoes_relatorio.pack(pady=10)

    btn_salvar = tk.Button(frame_botoes_relatorio, text="Salvar Relatório", command=lambda: salvar_relatorio(dados_sucesso, dados_falha))
    btn_salvar.grid(row=0, column=0, padx=10)

    btn_sair = tk.Button(frame_botoes_relatorio, text="Sair", command=janela_relatorio.destroy)
    btn_sair.grid(row=0, column=1, padx=10)
