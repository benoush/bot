import tkinter as tk
from tkinter import scrolledtext


def get_bot_response(user_input):
    user_input = user_input.lower()
    if "bonjour" in user_input:
        return "Bonjour à toi aussi ! 😊"
    elif "comment ça va" in user_input:
        return "Je vais très bien, merci ! Et toi ?"
    elif "ton nom" in user_input:
        return "Je suis un petit chatbot sans nom 😄"
    elif "aide" in user_input:
        return "Tu peux me dire bonjour, demander comment je vais, ou juste discuter !"
    elif "quit" in user_input or "sortir" in user_input:
        return "À bientôt !"
    else:
        return "Je ne comprends pas encore ça, mais j'apprends chaque jour."


def send(event=None):  # event=None permet d'appeler aussi bien par bouton que par Entrée
    user_input = entry.get()
    if user_input.strip() == "":
        return
    chat_window.insert(tk.END, f"Toi : {user_input}\n")
    response = get_bot_response(user_input)
    chat_window.insert(tk.END, f"Bot : {response}\n\n")
    entry.delete(0, tk.END)


# Fenêtre principale
window = tk.Tk()
window.title("Mini Chatbot")
window.geometry("400x500")

# Zone de chat
chat_window = scrolledtext.ScrolledText(window, wrap=tk.WORD, state=tk.NORMAL)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Zone de saisie utilisateur
entry = tk.Entry(window, width=40)
entry.pack(padx=10, pady=5, side=tk.LEFT, expand=True)

# Bouton envoyer
send_button = tk.Button(window, text="Envoyer", command=send)
send_button.pack(padx=10, pady=5, side=tk.RIGHT)

# Associer la touche Entrée à l'envoi
window.bind('<Return>', send)

# Lancer l'application
window.mainloop()
