import sys
import tkinter
import tkinter.ttk
from instapy import InstaPy
from instapy import smart_run

class SimpleApp(tkinter.Tk):

    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)

        self.parent = parent
        self.user_information = {'username':'', 'password':''}
        self.registered_comments = []
        self.registered_hashtags = []

        self.initialize()

    def initialize(self):
        # self.grid()
        self.tab = tkinter.ttk.Notebook(self, width=400, height=300)
        self.tab.place(x=250, y=0)

        sys.stdin = open('./commentList.txt','r')
        self.registered_comments = input().split()

        self.user_information_register()
        self.hashtag_tab_initialize()
        self.user_tab_initialize()
        # self.comment_register()
        # self.registered_comments_list()

        self.geometry('660x340+200+100')




    def user_information_register(self):
        self.user_info = tkinter.Label(self)
        self.user_info['text'] = 'User Information'
        self.user_info.grid(column=1, row=0)

        self.account_info = tkinter.Label(self)
        self.account_info['text'] = 'username'
        self.account_info.grid(column=0, row=1)
        self.account_value = tkinter.StringVar()
        self.account_entry = tkinter.Entry(self, textvariable=self.account_value)
        self.account_entry.grid(column=1, row=1, sticky='WE')

        self.password_info = tkinter.Label(self)
        self.password_info['text'] = 'password'
        self.password_info.grid(column=0, row=2)
        self.password_value = tkinter.StringVar()
        self.password_entry = tkinter.Entry(self, show="*", textvariable=self.password_value)
        self.password_entry.grid(column=1, row=2, sticky='WE')
        
        self.account_entry.bind('<Return>', self.user_enter_press)

        self.button = tkinter.Button(self, text='click', command=self.user_click_press)
        self.button.grid(column=2, row=2)

        self.user_label_value = tkinter.StringVar()
        self.user_label = tkinter.Label(self, fg='red', textvariable=self.user_label_value)
        self.user_label.grid(column=0, row=3, columnspan=2, sticky='EW')

        # self.entry.focus_set()
        # self.entry.select_range(0, tkinter.END)
    







    def hashtag_tab_initialize(self):
        sys.stdin = open('./hashtagList.txt','r')
        self.registered_hashtags = input().split()

        self.tab1 = tkinter.Frame(self)
        self.tab.add(self.tab1, text="Target HashTag")
        # self.registered_hashtag_list()
        self.hashtag_register(self.tab1)
        self.registered_hashtags_list(self.tab1)
        # self.registered_comments_list(self.tab1)
        self.hash_button = tkinter.Button(self.tab1, text="좋아요와 댓글달기", command=self.hashTag_Target_LikeNComment)
        self.hash_button.grid(row=4, column=4)

    def hashtag_register(self, target_tab):
        self.hashtagTitle = tkinter.Label(target_tab)
        self.hashtagTitle['text'] = 'Target HashTag'
        self.hashtagTitle.grid(row=0,column=1)

        self.hashtag = tkinter.Label(target_tab)
        self.hashtag['text'] = 'hashtag'
        self.hashtag.grid(row=1,column=0)
        self.hashtag_value = tkinter.StringVar()
        self.hashtag_entry = tkinter.Entry(target_tab, textvariable=self.hashtag_value)
        self.hashtag_entry.grid(row=1,column=1)
    
        # command 수정 필요
        hashtag_register_button = tkinter.Button(target_tab, text='등록', command=self.user_click_press)
        hashtag_register_button.grid(row=1,column=2)

    def registered_hashtags_list(self, target_tab):
        self.registered_hashtags_title = tkinter.Label(target_tab)
        self.registered_hashtags_title['text'] = 'registered hashtags'
        self.registered_hashtags_title.grid(row=3,column=1)

        self.hashtag_listbox = tkinter.Listbox(target_tab, selectmode='extended', height=0)
        self.hashtag_listbox.grid(row=4,column=1)
        for i, comment in enumerate(self.registered_hashtags):
            self.hashtag_listbox.insert(i, comment)
    





    def user_tab_initialize(self):
        self.tab2 = tkinter.Frame(self)
        self.tab.add(self.tab2, text="Target User")
        self.target_userId_register(self.tab2)
        # self.registered_comments_list(self.tab2)
    
    def target_userId_register(self, target_tab):
        self.userIdTitle = tkinter.Label(target_tab)
        self.userIdTitle['text'] = 'Target UserId'
        self.userIdTitle.grid(column=1, row=0)

        self.userId = tkinter.Label(target_tab)
        self.userId['text'] = 'UserId'
        self.userId.grid(column=0, row=1)
        self.userId_value = tkinter.StringVar()
        self.userId_entry = tkinter.Entry(target_tab, textvariable=self.userId_value)
        self.userId_entry.grid(column=1, row=1, sticky='WE')
        userId_register = tkinter.Button(target_tab, text='등록', command=self.comment_click)
        userId_register.grid(column=2, row=1)





    def comment_register(self):
        self.commentTitle = tkinter.Label(self)
        self.commentTitle['text'] = 'comment register'
        self.commentTitle.place(x=260, y=50)

        self.comments = tkinter.Label(self)
        self.comments['text'] = 'comment'
        self.comments.place(x=260, y=50)
        self.comment_value = tkinter.StringVar()
        self.comment_entry = tkinter.Entry(self, textvariable=self.comment_value)
        self.comment_entry.grid(column=4, row=2, sticky='WE')

        self.comment_entry.bind('<Return>', self.comment_enter)

    def registered_comments_list(self, target_tab):
        self.registered_comments_title = tkinter.Label(target_tab)
        self.registered_comments_title['text'] = 'registered comments'
        self.registered_comments_title.grid(column=4, row=0)

        self.comment_string = tkinter.StringVar()
        self.comment_combo = tkinter.ttk.Combobox(target_tab, textvariable=self.comment_string)
        self.comment_combo['values'] = self.registered_comments
        self.comment_combo.grid(column=4, row=1, padx=5)



    def user_click_press(self):
        if not self.account_value.get() or not self.password_value.get():
            self.user_label['fg'] = 'red'
            self.user_label_value.set("값을 입력하세요")
        else:
            self.user_label_value.set("")
            self.user_information['username'] = self.account_value.get()
            self.user_information['password'] = self.password_value.get()
            self.password_value.set('')
            self.user_label_value.set("저장되었습니다.")
            self.session = InstaPy(username=self.user_information['username'], 
                                    password=self.user_information['password'], headless_browser=True)

    def user_enter_press(self, event):
        self.user_click_press()

    def comment_click(self):
        if self.comment_value.get():
            with open('./commentList.txt', 'a') as CL:
                CL.write(self.comment_value.get()+' ')
            self.listbox.insert(len(self.registered_comments), self.comment_value.get())
            self.registered_comments + [self.comment_value.get()]
            self.comment_value.set('')
    
    def comment_enter(self, event):
        self.comment_click()

    
    def hashTag_Target_LikeNComment(self):
        with smart_run(self.session):
            self.session.set_do_follow(True, percentage=100, times=1)
            self.session.set_comments(self.registered_comments)
            self.session.set_do_comment(enabled=True, percentage=100)
            self.session.set_user_interact(amount=3, randomize=True, percentage=100)

            self.session.like_by_tags(self.hashtag_listbox.curselection(), amount=1)



app = SimpleApp(None)
app.title = 'Grapic User Interface'
app.mainloop()
