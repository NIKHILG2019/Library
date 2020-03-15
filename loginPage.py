import tkinter as tk
m = tk.Tk()
m.title("Login Page")
text1 = tk.Text(m, width="10", height="2")
text1.pack()
button1 = tk.Button(m, text="Login", command=m.destroy, width="10", height="1")
button1.pack()
m.mainloop()