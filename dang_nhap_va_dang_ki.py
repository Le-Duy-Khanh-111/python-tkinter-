import tkinter as tk

window = tk.Tk()

window.title("Đăng nhập và đăng kí")
window.geometry("350x400")
window.configure(background="black")

font_settings = ("Arial", 12, "bold")

def Login():
    usernamedangki = entryUsernamedangki.get()
    passworddangki = entryPassworddangki.get()
    usernamedangnhap = entryUsernamedangnhap.get()
    passworddangnhap = entryPassworddangnhap.get()
    if usernamedangki == usernamedangnhap and passworddangki == passworddangnhap:
        result = "Đăng nhập thành công"
    else:
        result = "Đăng nhập thất bại. Vui lòng đăng nhập lại"
    LabelResultdangnhap.config(text=result)

def show_result():
    passworddangki = entryPassworddangki.get()
    resetPassworddangki = entryResetPassworddangki.get()
    if passworddangki != resetPassworddangki:
        result = "Mật khẩu không khớp. Vui lòng nhập lại"
    else:
        result = "Đăng kí thành công"
    LabelResultdangki.config(text=result)

LabelUsernamedangki = tk.Label(
    window, text="Nhập tên đăng kí: ", font=font_settings, bg="black", 
    fg="green", wraplength=140
)
LabelUsernamedangki.place(x=10, y=10, width=150, height=30)

entryUsernamedangki = tk.Entry(window, font=font_settings)
entryUsernamedangki.place(x=160, y=10, width=150, height=30)

LabelPassworddangki = tk.Label(
    window, text="Nhập mật khẩu đăng kí: ", font=font_settings, bg="black", 
    fg="green", wraplength=140
)
LabelPassworddangki.place(x=10, y=50, width=150, height=30)

entryPassworddangki = tk.Entry(window, font=font_settings, show='*')
entryPassworddangki.place(x=160, y=50, width=150, height=30)

LabelResetPassworddangki = tk.Label(
    window, text="Nhập lại mật khẩu: ", font=font_settings, bg="black", 
    fg="green", wraplength=140
)
LabelResetPassworddangki.place(x=10, y=90, width=150, height=30)

entryResetPassworddangki = tk.Entry(window, show='*', font=font_settings)
entryResetPassworddangki.place(x=160, y=90, width=150, height=30)

buttondangki = tk.Button(
    window, text="Đăng kí", command=show_result, font=font_settings, 
    bg="black", fg="green"
)
buttondangki.place(x=10, y=130, width=300, height=30)

LabelResultdangki = tk.Label(
    window, text="Kết quả: ", font=font_settings, bg="black", fg="green"
)
LabelResultdangki.place(x=10, y=170, width=300, height=30)

LabelUsernamedangnhap = tk.Label(
    window, text="Nhập tên đăng nhập: ", font=font_settings, bg="black", 
    fg="green", wraplength=140
)
LabelUsernamedangnhap.place(x=10, y=210, width=150, height=30)

entryUsernamedangnhap = tk.Entry(window, font=font_settings)
entryUsernamedangnhap.place(x=160, y=210, width=150, height=30)

LabelPassworddangnhap = tk.Label(
    window, text="Nhập mật khẩu: ", font=font_settings, bg="black", 
    fg="green", wraplength=140
)
LabelPassworddangnhap.place(x=10, y=250, width=150, height=30)

entryPassworddangnhap = tk.Entry(window, show='*', font=font_settings)
entryPassworddangnhap.place(x=160, y=250, width=150, height=30)

buttondangnhap = tk.Button(
    window, text="Đăng nhập", command=Login, font=font_settings, 
    bg="black", fg="green", wraplength=140
)
buttondangnhap.place(x=10, y=290, width=300, height=30)

LabelResultdangnhap = tk.Label(
    window, text="Kết quả: ", font=font_settings, bg="black", fg="green"
)
LabelResultdangnhap.place(x=10, y=330, width=300, height=30)

window.mainloop()