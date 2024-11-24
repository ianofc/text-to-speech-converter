import tkinter as tk
from tkinter import messagebox, ttk
from gtts import gTTS
import os
import playsound

def botao():
    texto = texto_entry.get("1.0", tk.END).strip()
    linguagem = linguagem_combobox.get()
    sotaque = sotaque_combobox.get()
    
    if not texto:
        messagebox.showwarning("Aviso", "Por favor, insira algum texto.")
        return
    
    try:
        # Cria o objeto gTTS
        tts = gTTS(text=texto, lang=linguagem, slow=False)
        arquivo_audio = "output.mp3"
        # Salva o arquivo de áudio
        tts.save(arquivo_audio)
        # Reproduz o áudio
        playsound.playsound(arquivo_audio)
        messagebox.showinfo("Sucesso", "Conversão de texto para fala concluída e salva como output.mp3")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

def inicia():
    botao()

def resetar():
    texto_entry.delete("1.0", tk.END)
    linguagem_combobox.set("pt")
    sotaque_combobox.set("br")

# Criação da janela principal
root = tk.Tk()
root.title("Conversor de Texto para Fala")
root.geometry("400x300")

# Texto de entrada
texto_label = tk.Label(root, text="Digite o texto:")
texto_label.pack(pady=10)

texto_entry = tk.Text(root, height=5, width=40)
texto_entry.pack(pady=10)

# Seleção de linguagem
linguagem_label = tk.Label(root, text="Selecione a linguagem:")
linguagem_label.pack(pady=10)

linguagem_combobox = ttk.Combobox(root, values=["pt", "en", "es", "fr", "de"])
linguagem_combobox.set("pt")  # Define o padrão como Português
linguagem_combobox.pack(pady=10)

# Seleção de sotaque
sotaque_label = tk.Label(root, text="Selecione o sotaque:")
sotaque_label.pack(pady=10)

sotaque_combobox = ttk.Combobox(root, values=["br", "pt", "co.uk", "com.au", "com", "fr", "de"])
sotaque_combobox.set("br")  # Define o padrão como Brasileiro
sotaque_combobox.pack(pady=10)

# Botões
botao_iniciar = tk.Button(root, text="Iniciar", command=inicia)
botao_iniciar.pack(pady=5)

botao_resetar = tk.Button(root, text="Resetar", command=resetar)
botao_resetar.pack(pady=5)

# Executa a aplicação
root.mainloop()