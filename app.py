import customtkinter as ctk
from googletrans import Translator

# Initialize the translator
translator = Translator()

def translate_to_pashto():
    word = entry_word.get()
    if word:
        translated_text = translator.translate(word, src='en', dest='ps').text
        label_translation.configure(text=f"Pashto: {translated_text}")
    else:
        label_translation.configure(text="Please enter a word.")

def translate_to_english():
    word = entry_word.get()
    if word:
        translated_text = translator.translate(word, src='ps', dest='en').text
        label_translation.configure(text=f"English: {translated_text}")
    else:
        label_translation.configure(text="Please enter a word.")

def clear_input():
    entry_word.delete(0, ctk.END)
    label_translation.configure(text="Translation will appear here.")

def exit_app():
    root.quit()

# Set up the main window
root = ctk.CTk()

# Set window title and size
root.title("Abbas Hilal Dictionary")
root.geometry("600x450")  # Increased window size to fit extra buttons

# Create widgets
label_title = ctk.CTkLabel(root, text="Abbas Hilal Dictionary", font=("Arial", 30))
label_title.pack(pady=20)

entry_word = ctk.CTkEntry(root, placeholder_text="Enter a word", width=350, height=40, font=("Arial", 16))
entry_word.pack(pady=20)

button_english_to_pashto = ctk.CTkButton(root, text="Translate to Pashto", command=translate_to_pashto, width=350, height=40, font=("Arial", 16))
button_english_to_pashto.pack(pady=10)

button_pashto_to_english = ctk.CTkButton(root, text="Translate to English", command=translate_to_english, width=350, height=40, font=("Arial", 16))
button_pashto_to_english.pack(pady=10)

label_translation = ctk.CTkLabel(root, text="Translation will appear here.", font=("Arial", 20))
label_translation.pack(pady=30)

# Clear and Exit buttons
button_clear = ctk.CTkButton(root, text="Clear", command=clear_input, width=170, height=40, font=("Arial", 16))
button_clear.pack(side="left", padx=20, pady=20)

button_exit = ctk.CTkButton(root, text="Exit", command=exit_app, width=170, height=40, font=("Arial", 16))
button_exit.pack(side="right", padx=20, pady=20)

# Run the app
root.mainloop()
