from tkinter import *
root = Tk()

# 기본설정
root.title('InstaPy')
root.geometry("640x400+100+100")

#username, password
Label(root, text="username").grid(row=0)
user_name = Entry(root).grid(row=0, column=1)
Label(root, text="password").grid(row=1)
password = Entry(root).grid(row=1, column=1)

Label(root, text="target Hashtag").grid(row=3)
hashtag = Entry(root).grid(row=3, column=1, pady=10)


root.mainloop()

# import tkinter as tk

# master = tk.Tk()
# tk.Label(master, text="First Name").grid(row=0)
# tk.Label(master, text="Last Name").grid(row=1)

# e1 = tk.Entry(master)
# e2 = tk.Entry(master)

# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)

# master.mainloop()