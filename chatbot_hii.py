import tkinter as tk

def send_message():
    user_text = entry.get()

    if user_text.strip() == "":
        return

    chat_box.insert(tk.END, "you: " + user_text + "\n")

    if user_text.lower() == "hi":
        chat_box.insert(tk.END, "suzu : Hello!\n")
    elif user_text.lower() == "bye":
        chat_box.insert(tk.END, "suzu: Bye!\n")
    else:
        chat_box.insert(tk.END, "suzu: I am a bot🤖\n")

    entry.delete(0, tk.END)

window = tk.Tk()
window.title("My Chatbot")
window.geometry("800x900")

chat_box = tk.Text(window, font=("Arial", 16))
chat_box.pack()

entry = tk.Entry(window, font=("Arial", 16))
entry.pack()

button = tk.Button(window, text="Send", command=send_message, font=("Arial", 16))
button.pack()

window.mainloop()