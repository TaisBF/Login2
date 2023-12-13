from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkmacosx import Button

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

def signin ():
    username=user.get()
    password=code.get()

    if username=='admin' and password=='12345':
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        Label(screen, text='Hello Everyone!', bg='white', fg='black', font=('Calibri(Body)', 50, 'bold')).pack(expand=True, fill='both')

        screen.mainloop()

    elif username!='admin' and password!='12345':
        messagebox.showerror("Invalid", "ivalid username and password")
    elif password!="1234":
        messagebox.showerror("Invalid", "ivalid password")
    elif username!='admin':
        messagebox.showerror("Invalid", "ivalid username")

# Caminho para a imagem original
caminho_da_imagem_original = '/Users/taisfigueiredo/Downloads/Imagem.JPEG'

# Carregar e converter a imagem usando o Pillow
try:
    imagem_pillow = Image.open(caminho_da_imagem_original)
    resize_image = imagem_pillow.resize((450, 450))
    imagem_convertida = ImageTk.PhotoImage(resize_image)

    # Exibir a imagem convertida em um rótulo
    label = Label(root, image=imagem_convertida, bg='white')
    label.place(x=5, y=5)
except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")

# Caixa vermelha
frame = Label(root, width=350, height=350, bg="white")
frame.place(x=500, y=50)

heading=Label (frame, text='Sign in',  fg='#57a1f8',  bg='white', font=('Microsoft YaHei UI Light', 23, 'bold' ))
heading.place(x=100, y=5)

#####------------------------------------------------
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get
    if name=='':
        user.insert(0, 'Username')

user = Entry(frame, width=45, fg='black', border= 0, bg="white", highlightbackground='white', highlightcolor='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)
#####------------------------------------------------

def on_enter_password(e):
    code.delete(0, 'end')
    code.config(show='*')

def on_leave_password(e):
    password = code.get()
    if not password:
        code.insert(0, 'Password')
        code.config(show='')

code = Entry(frame, width=45, fg='black', bd=0, bg="white", highlightbackground='white', highlightcolor='white', font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter_password)
code.bind('<FocusOut>', on_leave_password)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

##################################################

Button(frame, width=300, pady=7, text='Sign in', bg='blue', fg='white', border=0, command=signin, highlightbackground='white').place(x=25, y=204)
label=Label(frame, text="Don´t have an account?", fg='black', bg='white', highlightbackground='white', font=('Microsoft YaHei UI Light', 9 ))
label.place(x=50, y=270)

sign_up = Button(frame, width=70, text='Sign up', border=0, bg='white', highlightbackground='white', highlightcolor='white', cursor='hand', fg='#57a1f8')
sign_up.place(x=180,y=264)

root.mainloop()