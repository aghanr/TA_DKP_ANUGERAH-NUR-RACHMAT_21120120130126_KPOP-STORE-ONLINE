from tkinter import *
import os
from tkinter import ttk
from tkinter import messagebox 


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Silahkan Masukan User dan Password").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, command = register_user).pack()
 

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Silahkan Login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 

def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=ok).pack()

def ok():
    global kpop_store
    global stringnama
    global stringalamat
    global radio
    kpop_store = Toplevel(login_success_screen)
    kpop_store.title("K-Pop Online Store - Data Diri")
    kpop_store.geometry("300x200")
    Label(kpop_store, text="SILAHKAN MASUKAN DATA DIRI ANDA").pack()
    lbnama = Label(kpop_store, text = "Nama\t:").place(x = 30, y = 30)    
    lbalamat = Label(kpop_store, text = "Alamat\t:").place(x = 30, y = 80)
    stringnama = StringVar()
    stringalamat = StringVar()
    inama = Entry(kpop_store, width = 20, textvariable=stringnama).place(x = 110, y = 30) 
    ialamat = Entry(kpop_store, width = 20, textvariable=stringalamat).place(x = 110, y = 80) 
    radio = IntVar()
    btn1 = Button(kpop_store, command = submit, text="SUBMIT").place(x=120,y=170)

def submit():
    global kpop_store_item
    global radio_item
    kpop_store_item = Toplevel(kpop_store)
    kpop_store_item.geometry("350x950")
    kpop_store_item.title("K-Pop Online Store - Item")
    Label(kpop_store_item, text="Silahkan pilih barang yang ingin anda beli").pack()
    radio_item = IntVar()
    R1 = Radiobutton(kpop_store_item, text="BTS - Map Of The Soul : Persona", variable=radio_item, value=1).place(x=75, y=50) 
    lb1 = Label(kpop_store_item, text = "Rp.280.000,00").place(x = 75,y = 80)  
    R2 = Radiobutton(kpop_store_item, text="LOONA - 12:00", variable=radio_item, value=2).place(x=75, y=150) 
    lb1 = Label(kpop_store_item, text = "Rp.250.000,00").place(x = 75,y = 180) 
    R3 = Radiobutton(kpop_store_item, text="TWICE - twicetagram", variable=radio_item, value=3).place(x=75, y=250) 
    lb1 = Label(kpop_store_item, text = "Rp.250.000,00").place(x = 75,y = 280)
    R4 = Radiobutton(kpop_store_item, text="ITZY - It'z Me", variable=radio_item, value=4).place(x=75, y=350)
    lb1 = Label(kpop_store_item, text = "Rp.280.000,00").place(x = 75,y = 380)
    R5 = Radiobutton(kpop_store_item, text="Stray Kids - GO LIVE", variable=radio_item, value=5).place(x=75, y=450)
    lb1 = Label(kpop_store_item, text = "Rp.300.000,00").place(x = 75,y = 480)
    R6 = Radiobutton(kpop_store_item, text="NCT - Resonance Pt.1", variable=radio_item, value=6).place(x=75, y=550) 
    lb1 = Label(kpop_store_item, text = "Rp.300.000,00").place(x = 75,y = 580)
    R6 = Radiobutton(kpop_store_item, text="DAY6 - The Book Of Us : Negentropy", variable=radio_item, value=7).place(x=75, y=650)
    lb1 = Label(kpop_store_item, text = "Rp.300.000,00").place(x = 75,y = 680)
    R6 = Radiobutton(kpop_store_item, text="IZONE - One-reeler/Act IV", variable=radio_item, value=8).place(x=75, y=750)
    lb1 = Label(kpop_store_item, text = "Rp.280.000,00").place(x = 75,y = 780)
    btn2 = Button(kpop_store_item, command = struk, text="SUBMIT").place(x=150,y=855)

def struk():
    global strukanda
    strukanda = Toplevel(kpop_store_item)
    strukanda.geometry("700x450")
    strukanda.title("Struk Pembayaran")
    Label(strukanda, text="Struk Anda").pack()

    struk_stringnama = stringnama.get()
    struk_stringalamat = stringalamat.get()
    radio_radio      = radio.get()
    r_item      = radio_item.get()

    if len(struk_stringnama) == 0:
        messagebox.showerror("Error","Anda belum mengisi nama")
        return
    if len(struk_stringalamat) == 0:
        messagebox.showerror("Error","Anda belum mengisi alamat tujuan")
        return
    if radio_item.get() == 1:
         des1 ="BTS - Map Of The Soul : Persona"
         des2 ="Anda memilih album ini dengan harga Rp.280.000,00" 
         des3 ="Biaya ongkir Rp.20.000,00"
         des4 ="Rp.300.000,00"
    if radio_item.get() == 2:
         des1 ="LOONA - 12:00"
         des2 ="Anda memilih album ini dengan harga Rp.250.000,00"
         des3 ="Biaya ongkir Rp.20.000,00"
         des4 ="Rp.270.000,00"
    if radio_item.get() == 3:
         des1 ="TWICE - twicetagram"
         des2 ="Anda memilih album ini dengan harga 250.000,00"
         des3 ="Biaya ongkir Rp.20.000,00"
         des4 ="Rp.270.000,00"
    if radio_item.get() == 4: 
         des1 ="ITZY - It'z Me"
         des2 ="Anda memilih album ini dengan harga Rp.280.000,00" 
         des3 ="Biaya ongkir Rp.20.000,00"
         des4 ="Rp.300.000,00"
    if radio_item.get() == 5:
         des1 ="Stray Kids - GO LIVE"
         des2 ="Anda memilih album ini dengan harga Rp.300.000,00"
         des3 ="Biaya ongkir Rp.20.000,00"
         des4 ="Rp.320.000,00"
    if radio_item.get() == 6:
         des1 ="NCT - Resonance Pt.1"
         des2 ="Anda memilih album ini dengan harga Rp.300.000,00"
         des3 ="Biaya ongkir Rp.20.000,00"
         des4 ="Rp.320.000,00"
    if radio_item.get() == 7:
         des1 ="DAY6 - The Book of Us : Negentropy"
         des2 ="Anda memilih album ini dengan harga Rp.300.000,00"
         des3 ="Biaya ongkir Rp.20.000,00"
         des4 ="Rp.320.000,00"
    if radio_item.get() == 8:
         des1 ="IZONE - One-reeler/Act IV"
         des2 ="Anda memilih album ini dengan harga Rp.280.000,00" 
         des3 ="Biaya ongkir Rp.20.000,00"
         des4 ="Rp.300.000,00"


 
    Label(strukanda, text="Data Pemesan").place(x=30,y=50)
    Label(strukanda, text="Nama      :  " + struk_stringnama).place(x=30,y=70)
    Label(strukanda, text="Alamat     :  " + struk_stringalamat).place(x=30,y=90)

    Label(strukanda, text="Item yang dipesan").place(x=30,y=150)
    Label(strukanda, text=des1).place(x=30,y=170)
    Label(strukanda, text=des2).place(x=30,y=190)
    Label(strukanda, text=des3).place(x=30,y=210)

    Label(strukanda, text="TOTAL BIAYA = "+ des4).place(x=30,y=250)
    Label(strukanda, text="Silahkan transfer ke Bank ACB dengan nomor rekening 123456 a.n Anugerah Nur Rachmat").place(x=30,y=280)




def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 

def del_login_screen():
    login_screen.destroy()
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login and Register Kpop Online Store")
    Label(text="K-Pop Online Store", bg="cyan", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()
