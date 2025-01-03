import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("600x400")
app.title("Аналізатор тексту")

def analyze_text():
    text = textbox.get("1.0", "end-1c") # Отримуємо текст з textbox
    # Тут ваш код аналізу тексту (поки що просто виводимо текст)
    result_label.configure(text=f"Введено текст: {text}")

# Текстове поле
textbox = customtkinter.CTkTextbox(app)
textbox.pack(padx=20, pady=(20, 10))

# Кнопка аналізу
analyze_button = customtkinter.CTkButton(app, text="Аналізувати", command=analyze_text)
analyze_button.pack(pady=(0, 10))

# Мітка для результатів
result_label = customtkinter.CTkLabel(app, text="")
result_label.pack()

app.mainloop()