import tkinter as tk
from tkinter import messagebox
import random

def start_new_game():
    global numero_pc, tentativas, pontuacao
    numero_pc = random.randint(0, 10)
    tentativas = 5
    pontuacao = 0 
    update_tentativas_label()
    update_pontuacao_label()
    entry.delete(0, tk.END)

def check_numero_jog():
    global tentativas, pontuacao
    numero_jog = entry.get()
    entry.delete(0, tk.END)

    try:
        numero_jog = int(numero_jog)
    except ValueError:
        messagebox.showerror("Errou feio", "\nDigite um novo número.")
        return

    if numero_jog < 0 or numero_jog > 10:
        messagebox.showerror("Errou feio", "\nDigite um número entre 0 e 10.")
        return

    if numero_jog == numero_pc:
        pontuacao = 100 - (5 - tentativas) * 20
        if tentativas == 1:
          pontuacao = 10
        messagebox.showinfo("Boaaa!", f"\nVocê acertou!\nO número é {numero_pc}.\nSua pontuação final é {pontuacao} pontos.")
        start_new_game()
    else:
        tentativas -= 1
        if tentativas == 0:
            pontuacao = 0
            messagebox.showinfo("Acabou", f"\nVocê perdeu!\nO número era {numero_pc}.\nSua pontuação final é {pontuacao} pontos.")
            start_new_game()
        else:
            messagebox.showerror("Errou feio", f"\nO número {numero_jog} não é o número sorteado.\nResta apenas {tentativas} tentativas.")
    update_tentativas_label()

# Função para atualizar o rótulo de tentativas
def update_tentativas_label():
    tentativas_label.config(text=f"Restante das tentativas: {tentativas}")

# Função para atualizar o rótulo de pontuação
def update_pontuacao_label():
    pontuacao_label.config(text=f"Pontuação: {pontuacao}")

# Configuração inicial
root = tk.Tk()
root.title("ACERTE O NÚMERO")
root.config(bg='#2B4970')

numero_pc = random.randint(0, 10)
tentativas = 5
pontuacao = 0

# Widgets
tentativas_label = tk.Label(root, text=f"JOGUE E ACERTE: Basea-se na sorte ou na lógica!!!")
tentativas_label.pack(pady=30)

numero_jog_label = tk.Label(root, text="Digite um número de 0 a 10:")
numero_jog_label.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

check_button = tk.Button(root, text="Checar: ", command=check_numero_jog)
check_button.pack(pady=20)

tentativas_label = tk.Label(root, text=f"Restante de tentativas: {tentativas}")
tentativas_label.pack(pady=10)

pontuacao_label = tk.Label(root, text=f"Pontuação: {pontuacao}")
pontuacao_label.pack(pady=20)

new_game_button = tk.Button(root, text="Ir de novo", command=start_new_game)
new_game_button.pack(pady=10)

quit_button = tk.Button(root, text="Sair do jogo", command=root.quit)
quit_button.pack(pady=30)

pontuacao_label = tk.Label(root, text=f"CRIADORES: \n\nFMU: CENTRO UNIVERSITÁRIO DAS FACULDADES METROPOLITANAS UNIDAS\n\nCURSO: ENGENHARIA DA COMPUTAÇÃO - PRESENCIAL - NOTURNO - 3º SEMESTRE - TURMA: 231203A16\n\nGUSTAVO GIL AMARILHO - RA: 1847950\n\nHELLEN CRISTHINE SOUZA ATANASIO - RA: 1821616\n\nLIVIA CAROLINE DOS SANTOS - RA: 1431867\n\nVICTÓRIA DOS SANTOS LUNGOV - RA: 1719971")
pontuacao_label.pack()

# Loop principal
root.mainloop()
