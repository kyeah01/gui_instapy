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
        self.registered_userids = []

        self.initialize()

    def initialize(self):
        # self.grid()
        self.tab = tkinter.ttk.Notebook(self, width=400, height=300)
        self.tab.place(x=280, y=0)


        self.user_information_register()
        self.setting_the_limit()
        self.hashtag_tab_initialize()
        self.user_tab_initialize()
        self.comment_tab_initialize()

        # self.registered_comments_list()

        self.geometry('690x330+200+100')




    def user_information_register(self):
        self.user_info = tkinter.Label(self, text='User Information')
        self.user_info.grid(column=1, row=0)

        self.account_info = tkinter.Label(self, text='username')
        self.account_info.grid(column=0, row=1)
        self.account_value = tkinter.StringVar()
        self.account_entry = tkinter.Entry(self, textvariable=self.account_value)
        self.account_entry.grid(column=1, row=1, sticky='WE')

        self.password_info = tkinter.Label(self, text='password')
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
    
    def setting_the_limit(self):
        watingLimit = tkinter.Label(self, text="대기시간 설정")
        watingLimit.grid(row=4,column=1)

        likeLimit = tkinter.Label(self, text="좋아요")
        likeLimit.grid(row=5, column=0)
        likeLimitSpinbox = tkinter.Spinbox(self, from_ = 0, to = 100)
        likeLimitSpinbox.grid(row=5, column=1)

        followLimit = tkinter.Label(self, text="팔로우")
        followLimit.grid(row=6, column=0)
        followLimitSpinbox = tkinter.Spinbox(self, from_ = 0, to = 100)
        followLimitSpinbox.grid(row=6, column=1)

        todayLimit = tkinter.Label(self, text="하루 제한량 설정")
        todayLimit.grid(row=7,column=1)

        unfollowLimit = tkinter.Label(self, text="언팔")
        unfollowLimit.grid(row=8, column=0)
        unfollowLimitSpinbox = tkinter.Spinbox(self, from_ = 0, to = 100)
        unfollowLimitSpinbox.grid(row=8, column=1)
        
        nextLimit = tkinter.Label(self, text="언팔 후 대기")
        nextLimit.grid(row=9, column=0)
        nextLimitSpinbox = tkinter.Spinbox(self, from_ = 0, to = 100)
        nextLimitSpinbox.grid(row=9, column=1)
        











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
        self.hash_button.grid(row=1, column=4, padx=5)

    def hashtag_register(self, target_tab):
        hashtagTitle = tkinter.Label(target_tab, text='Target HashTag')
        hashtagTitle.grid(row=0,column=1)

        hashtag = tkinter.Label(target_tab, text='hashtag')
        hashtag.grid(row=1,column=0)
        self.hashtag_value = tkinter.StringVar()
        self.hashtag_entry = tkinter.Entry(target_tab, textvariable=self.hashtag_value)
        self.hashtag_entry.grid(row=1,column=1)
    
        self.hashtag_register_button = tkinter.Button(target_tab, text='등록', command=self.hashtag_click)
        self.hashtag_register_button.grid(row=1,column=2)

        self.hashtag_delete_button = tkinter.Button(target_tab, text='삭제', command=self.hashtag_delete)
        self.hashtag_delete_button.grid(row=4,column=2)

    def registered_hashtags_list(self, target_tab):
        registered_hashtags_title = tkinter.Label(target_tab, text='registered hashtags')
        registered_hashtags_title.grid(row=3,column=1)
        self.hashtag_listbox = tkinter.Listbox(target_tab, selectmode='extended', height=0)
        self.hashtag_listbox.grid(row=4,column=1)
        for i, ht in enumerate(self.registered_hashtags):
            self.hashtag_listbox.insert(i, ht)
    





    def user_tab_initialize(self):
        sys.stdin = open('./userIdList.txt','r')
        self.registered_userids = input().split()

        self.tab2 = tkinter.Frame(self)
        self.tab.add(self.tab2, text="Target User")
        self.target_userId_register(self.tab2)
        self.registered_userids_list(self.tab2)
    
    def target_userId_register(self, target_tab):
        userIdTitle = tkinter.Label(target_tab, text='Target UserId')
        userIdTitle.grid(column=1, row=0)

        userId = tkinter.Label(target_tab,text='UserId')
        userId.grid(column=0, row=1)
        self.userId_value = tkinter.StringVar()
        self.userId_entry = tkinter.Entry(target_tab, textvariable=self.userId_value)
        self.userId_entry.grid(column=1, row=1, sticky='WE')

        userId_register = tkinter.Button(target_tab, text='등록', command=self.userid_click)
        userId_register.grid(column=2, row=1)
        
        userId_delete = tkinter.Button(target_tab, text='삭제', command=self.userid_delete)
        userId_delete.grid(column=2, row=4)

    def registered_userids_list(self, target_tab):
        registered_userids_title = tkinter.Label(target_tab,text='registered userids')
        registered_userids_title.grid(row=3,column=1)
        self.userid_listbox = tkinter.Listbox(target_tab, selectmode='extended', height=0)
        self.userid_listbox.grid(row=4,column=1)
        for i, ud in enumerate(self.registered_userids):
            self.userid_listbox.insert(i, ud)








    def comment_tab_initialize(self):
        sys.stdin = open('./commentList.txt','r')
        self.registered_comments = input().split()

        self.tab3 = tkinter.Frame(self)
        self.tab.add(self.tab3, text="Registered Comments")
        self.registered_comments_list(self.tab3)
        self.comment_register(self.tab3)


    def comment_register(self, target_tab):
        commentTitle = tkinter.Label(target_tab, text='comment register')
        commentTitle.grid(row=0, column=1)

        comments = tkinter.Label(target_tab, text='comment')
        comments.grid(row=1, column=0)
        self.comment_value = tkinter.StringVar()
        self.comment_entry = tkinter.Entry(target_tab, textvariable=self.comment_value)
        self.comment_entry.grid(column=1, row=1)

        comment_register = tkinter.Button(target_tab, text='등록', command=self.comment_click)
        comment_register.grid(column=2, row=1)

        comment_delete_button = tkinter.Button(target_tab, text='삭제', command=self.comment_delete)
        comment_delete_button.grid(column=2, row=3)

    def registered_comments_list(self, target_tab):
        registered_comments_title = tkinter.Label(target_tab, text='registered comments')
        registered_comments_title.grid(column=1, row=2, pady=5)
        self.comment_listbox = tkinter.Listbox(target_tab, selectmode='extended', height=0)
        self.comment_listbox.grid(column=1, row=3)
        for i, comment in enumerate(self.registered_comments):
            self.comment_listbox.insert(i, comment)








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





    def hashtag_click(self):
        if self.hashtag_value.get():
            with open('./hashtagList.txt', 'a') as HL:
                HL.write(self.hashtag_value.get()+' ')
            self.hashtag_listbox.insert(len(self.registered_hashtags), self.hashtag_value.get())
            self.registered_hashtags += [self.hashtag_value.get()]
            self.hashtag_value.set('')
    
    def hashtag_delete(self):
        choice = self.hashtag_listbox.curselection()
        self.hashtag_listbox.delete(choice[0], choice[-1])
        for _ in choice:
            self.registered_hashtags.pop(choice[0])
        
        with open('./hashtagList.txt', 'w') as HL:
            HL.write(' '.join(self.registered_hashtags)+' ')








    
    def userid_click(self):
        if self.userId_value.get():
            with open('./userIdList.txt', 'a') as UL:
                UL.write(self.userId_value.get()+' ')
            self.userid_listbox.insert(len(self.registered_userids), self.userId_value.get())
            self.registered_userids += [self.userId_value.get()]
            self.userId_value.set('')

    def userid_delete(self):
        choice = self.userid_listbox.curselection()
        self.userid_listbox.delete(choice[0], choice[-1])
        for _ in choice:
            self.registered_userids.pop(choice[0])
        
        with open('./userIdList.txt', 'w') as UL:
            UL.write(' '.join(self.registered_userids)+' ')







    def comment_click(self):
        if self.comment_value.get():
            with open('./commentList.txt', 'a') as CL:
                CL.write(self.comment_value.get()+' ')
            self.comment_listbox.insert(len(self.registered_comments), self.comment_value.get())
            self.registered_comments += [self.comment_value.get()]
            self.comment_value.set('')

    def comment_delete(self):
        choice = self.comment_listbox.curselection()
        self.comment_listbox.delete(choice[0], choice[-1])
        for _ in choice:
            self.registered_comments.pop(choice[0])
        
        with open('./commentList.txt', 'w') as CL:
            CL.write(' '.join(self.registered_comments)+' ')
    







    def hashTag_Target_LikeNComment(self):
        with smart_run(self.session):
            # follow 설정
            self.session.set_do_follow(True, percentage=100, times=1)
            # 설정된 comment내에서 무작위로 comment 달기
            self.session.set_comments(self.registered_comments)
            self.session.set_do_comment(enabled=True, percentage=100)
            self.session.set_user_interact(amount=3, randomize=True, percentage=100)

            self.session.like_by_tags(self.hashtag_listbox.curselection(), amount=1)



app = SimpleApp(None)
app.title = 'Grapic User Interface'
app.mainloop()
