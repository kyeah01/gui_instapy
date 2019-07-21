import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        
        # self.test = tk.Entry(self)
        # self.test
        string = tk.StringVar()
        self.textbox = tk.Entry(self, width=20, textvariable=string)
        self.textbox.pack()
        self.action = tk.Button(self, text="click Me", command=self.clickMe)
        self.action.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
    
    def clickMe(self):
        self.messagebox.showinfo("Button Clicked", str.get())



root = tk.Tk()
app = Application(master=root)
app.mainloop()