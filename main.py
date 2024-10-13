from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    generated_password = "".join(password_list)
    password_entry.insert(0,generated_password)
    pyperclip.copy(generated_password)
#password_p = ""
#for char in password_list:
#  password_p += char


    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    mail = mail_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": mail,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty")
    else:
        try:
            with open('data.json', 'r') as file:
                # Dosyayı yüklemeye çalış
                data = json.load(file)
        except FileNotFoundError:
            # Dosya bulunamazsa, yeni veri yapısını oluştur
            data = new_data
        except json.JSONDecodeError:
            # JSON formatı geçersiz veya dosya boşsa yeni bir veri oluştur
            data = new_data
        else:
            # Eğer dosya geçerli ise yeni veriyi mevcut veri ile güncelle
            data.update(new_data)
        
        # Dosyaya veriyi yaz
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
        
        # Giriş alanlarını temizle
        website_entry.delete(0, END)
        password_entry.delete(0, END)

 #-------------------------FIND PASSWORD-------------------#
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data file found")
    else:
        if website in data:
            mail = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {mail}\n Password:{password}")
        else:
            messagebox.showinfo(title="Error",message=f"Böyle bir hocadan önce insan bulunamadı")
        
            
        
    
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels and Entries
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="W")

search_frame = Frame(window)
search_frame.grid(row=1, column=1, columnspan=2, sticky="W")

website_entry = Entry(search_frame,width=35)
website_entry.grid(row=0, column=0)

search_button = Button(search_frame, text="Search", width=15,command=find_password)
search_button.grid(row=0, column=1)

mail_label = Label(text="Email/Username:")
mail_label.grid(row=2, column=0, sticky="W")

mail_entry = Entry(width=35)
mail_entry.grid(row=2, column=1, columnspan=2, sticky="W")
mail_entry.insert(0, "ela@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="W")

# Frame for password entry and button
password_frame = Frame(window)
password_frame.grid(row=3, column=1, columnspan=2, sticky="W")

password_entry = Entry(password_frame, width=35)
password_entry.grid(row=0, column=0)

password_button = Button(password_frame, text="Generate Password", width=20,command=generate_password)
password_button.grid(row=0, column=1)





# Add button (spanning two columns)
add_button = Button(text="Add", width=36,command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")


window.mainloop()
