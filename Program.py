import customtkinter

customtkinter.set_appearance_mode("Dark")  # Режим теми: System, Dark, Light
customtkinter.set_default_color_theme("green")  # Колірна схема: blue, green, dark-blue

app = customtkinter.CTk()
app.geometry("400x200")  # Розміри вікна
app.title("Hello, World! з CustomTkinter")

def button_callback():
    label.configure(text="Кнопку натиснуто!")

# Створення напису (Label)
label = customtkinter.CTkLabel(app, text="Hello, World!", font=customtkinter.CTkFont(size=20, weight="bold"))
label.pack(pady=(20, 0))  # Верхній відступ 20, нижній 0

# Створення кнопки
button = customtkinter.CTkButton(app, text="Натисни мене!", command=button_callback)
button.pack(pady=(20, 20))  # Верхній та нижній відступи по 20

app.mainloop()