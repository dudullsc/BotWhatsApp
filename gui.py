import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from whatsapp_sender import iniciar_envio, parar_envio
from utils import definir_icone, carregar_planilha, carregar_arquivo_adicional, gerar_planilha_exemplo, converter_xlsx_para_csv
from report import mostrar_relatorio

class JanelaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Envio de Mensagens no WhatsApp")
        definir_icone(self.root)
        self.file_path = None
        self.arquivo_adicional = None
        self.enviar = False

        # Componentes da interface
        self.setup_gui()

    def setup_gui(self):
        # Menu principal
        menu_principal = tk.Menu(self.root)
        self.root.config(menu=menu_principal)

        # Menu Ajuda
        menu_ajuda = tk.Menu(menu_principal, tearoff=0)
        menu_principal.add_cascade(label="Ajuda", menu=menu_ajuda)
        menu_ajuda.add_command(label="Gerar Planilha de Exemplo", command=gerar_planilha_exemplo)

        lbl_instrucoes = tk.Label(self.root, text="Importe uma planilha com as colunas: Nome e Numero.")
        lbl_instrucoes.pack(pady=10)

        frame_botoes = tk.Frame(self.root)
        frame_botoes.pack(pady=5)

        btn_carregar = tk.Button(frame_botoes, text="Carregar Planilha", command=self.carregar_planilha)
        btn_carregar.grid(row=0, column=0, padx=5)

        btn_arquivo = tk.Button(frame_botoes, text="Carregar Arquivo Adicional", command=self.carregar_arquivo_adicional)
        btn_arquivo.grid(row=0, column=1, padx=5)

        btn_converter = tk.Button(frame_botoes, text="Converter .xlsx para .csv", command=converter_xlsx_para_csv)
        btn_converter.grid(row=0, column=2, padx=5)

        self.lbl_planilha = tk.Label(self.root, text="Nenhuma planilha carregada")
        self.lbl_planilha.pack(pady=5)

        self.lbl_arquivo = tk.Label(self.root, text="Nenhum arquivo adicional carregado")
        self.lbl_arquivo.pack(pady=5)

        lbl_mensagem = tk.Label(self.root, text="Digite a mensagem. Use {nome} para inserir o nome da pessoa:")
        lbl_mensagem.pack(pady=10)

        self.txt_mensagem = tk.Text(self.root, height=10, width=50)
        self.txt_mensagem.pack(pady=5)

        frame_envio = tk.Frame(self.root)
        frame_envio.pack(pady=5)

        btn_iniciar = tk.Button(frame_envio, text="Iniciar Envio", command=self.iniciar_envio)
        btn_iniciar.grid(row=0, column=0, padx=5)

        btn_parar = tk.Button(frame_envio, text="Parar Envio", command=self.parar_envio)
        btn_parar.grid(row=0, column=1, padx=5)

        btn_fechar = tk.Button(self.root, text="Fechar Programa", command=self.fechar_programa)
        btn_fechar.pack(pady=20)

        lbl_versao = tk.Label(self.root, text="Versão: v1.1")
        lbl_versao.pack(pady=5)

    def carregar_planilha(self):
        self.file_path = carregar_planilha()
        if self.file_path:
            self.lbl_planilha.config(text=f"Planilha carregada: {self.file_path}")
        else:
            self.lbl_planilha.config(text="Nenhuma planilha carregada")

    def carregar_arquivo_adicional(self):
        self.arquivo_adicional = carregar_arquivo_adicional()
        if self.arquivo_adicional:
            self.lbl_arquivo.config(text=f"Arquivo carregado: {self.arquivo_adicional}")
        else:
            self.lbl_arquivo.config(text="Nenhum arquivo adicional carregado")

    def iniciar_envio(self):
        if self.file_path:
            iniciar_envio(self.file_path, self.arquivo_adicional, self.txt_mensagem, self.root)
        else:
            messagebox.showerror("Erro", "Por favor, carregue uma planilha antes de iniciar o envio.")

    def parar_envio(self):
        parar_envio()

    def fechar_programa(self):
        self.root.destroy()
