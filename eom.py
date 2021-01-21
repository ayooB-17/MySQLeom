from tkinter import *

def register_user():
    username_info = username.get()
    password_info = password.get()

    file= open(username_info= "eom", ".txt")
    file.write(username_info)
    file.write(password_info)
    file.close()

    usernameNTR.delete(0, END)
    passwordNTR.delete(0, END)
    
    Label(first_screen, text= "Registration Successful", fg= "#65ff00", font= ("Calibri", 11)).pack()

def register():
    print("Registeration Started")
    global first_screen
    first_screen = Toplevel(screen)
    first_screen.title("Register Here ")
    first_screen.geometry("300x250")

    global username
    global password
    global usernameNTR
    global passwordNTR    
    username = StringVar()
    password = StringVar()

    Label(first_screen, text= "Please Enter Your Details Below: ", bg = "#65ff00", width= "300", height= "2", font = ("Calibri", 13)).pack()
    Label(first_screen, text= "").pack()
    Label(first_screen, text= "Username * ").pack()
    usernameNTR= Entry(first_screen, textvariable=username)
    usernameNTR.pack()
    Label(first_screen, text= "Password * ").pack()
    passwordNTR= Entry(first_screen, textvariable = password)
    passwordNTR.pack()
    Label(first_screen, text= "").pack()
    Button(first_screen, text= "Register", width= 10, height= 1, command= register_user).pack()

def login():
    print("Login Process Started")

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Gateway")
    Label(text= "Gateway To Enter Premises", bg = "#65ff00", width= "300", height= "2", font = ("Calibri", 13)).pack()
    Label(text= "").pack()
    Button(text= "Login Here", height= "2", width= "30", command= login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width= "30", command= register).pack()

    screen.mainloop()

main_screen()