# coding=<utf-8>

import sys
import tkinter
import tkinter.ttk
import tkinter.messagebox
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
        self.registered_words = []
        self.followers = []
        self.isSessionRun = False

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
        self.ignoreTabInitialize()

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
        watingLimit = tkinter.Label(self, text="Maximum limit")
        watingLimit.grid(row=4,column=0)

        timeLimit = tkinter.Label(self, text="per hour")
        timeLimit.grid(row=5,column=1)

        dayLimit = tkinter.Label(self, text="per day")
        dayLimit.grid(row=5,column=2)

        likeLimit = tkinter.Label(self, text="Like")
        likeLimit.grid(row=6, column=0)

        self.likeHourLimitSpinbox = tkinter.Spinbox(self, from_ = 0, to = 1000, width=5)
        self.likeHourLimitSpinbox.grid(row=6, column=1)

        self.likeDayLimitSpinbox = tkinter.Spinbox(self, from_ = 0, to = 1000, width=5)
        self.likeDayLimitSpinbox.grid(row=6, column=2)

        followLimit = tkinter.Label(self, text="Follow")
        followLimit.grid(row=7, column=0)

        self.followHourLimitSpinbox = tkinter.Spinbox(self, from_ = 0, to = 1000, width=5)
        self.followHourLimitSpinbox.grid(row=7, column=2)

        self.followDayLimitSpinbox = tkinter.Spinbox(self, from_ = 0, to = 1000, width=5)
        self.followDayLimitSpinbox.grid(row=7, column=1)

        br = tkinter.Label(self)
        br.grid(row=8, column=0)

        countLimit = tkinter.Label(self, text="Maximum limit")
        countLimit.grid(row=9,column=0)

        hourLimit = tkinter.Label(self, text="per hour")
        hourLimit.grid(row=10,column=1)

        todayLimit = tkinter.Label(self, text="per day")
        todayLimit.grid(row=10,column=2)

        unfollowLimit = tkinter.Label(self, text="unfollow")
        unfollowLimit.grid(row=11, column=0)

        self.unfollowHourLimitSpinbox = tkinter.Spinbox(self, from_ = 0, to = 1000, width=5)
        self.unfollowHourLimitSpinbox.grid(row=11, column=1)

        self.unfollowDayLimitSpinbox = tkinter.Spinbox(self, from_ = 0, to = 1000, width=5)
        self.unfollowDayLimitSpinbox.grid(row=11, column=2)
        
        nextLimit = tkinter.Label(self, text="server call")
        nextLimit.grid(row=12, column=0)

        self.serverHourLimitSpinbox = tkinter.Spinbox(self, from_ = 0, to = 1000, width=5)
        self.serverHourLimitSpinbox.grid(row=12, column=1)

        self.serverDayLimitSpinbox = tkinter.Spinbox(self, from_ = 0, to = 1000, width=5)
        self.serverDayLimitSpinbox.grid(row=12, column=2)

        applyButton = tkinter.Button(self, text="apply", command=self.applyTheLimit)
        applyButton.grid(row=13, column=2)
        











    def hashtag_tab_initialize(self):
        sys.stdin = open('./hashtagList.txt','r')
        self.registered_hashtags = input().split()

        self.tab1 = tkinter.Frame(self)
        self.tab.add(self.tab1, text="Target HashTag")
        # self.registered_hashtag_list()
        self.hashtag_register(self.tab1)
        self.registered_hashtags_list(self.tab1)
        # self.registered_comments_list(self.tab1)
        self.hash_button = tkinter.Button(self.tab1, text="Like & comment", command=self.hashTag_Target_LikeNComment)
        self.hash_button.grid(row=1, column=4, padx=5)

    def hashtag_register(self, target_tab):
        hashtagTitle = tkinter.Label(target_tab, text='Target HashTag')
        hashtagTitle.grid(row=0,column=1)

        hashtag = tkinter.Label(target_tab, text='hashtag')
        hashtag.grid(row=1,column=0)
        self.hashtag_value = tkinter.StringVar()
        self.hashtag_entry = tkinter.Entry(target_tab, textvariable=self.hashtag_value)
        self.hashtag_entry.grid(row=1,column=1)
    
        self.hashtag_register_button = tkinter.Button(target_tab, text='register', command=self.hashtag_click)
        self.hashtag_register_button.grid(row=1,column=2)

        self.hashtag_delete_button = tkinter.Button(target_tab, text='delete', command=self.hashtag_delete)
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

        userId_register = tkinter.Button(target_tab, text='register', command=self.userid_click)
        userId_register.grid(column=2, row=1)
        
        userId_delete = tkinter.Button(target_tab, text='delete', command=self.userid_delete)
        userId_delete.grid(column=2, row=4)

        userId_likeNComment = tkinter.Button(target_tab, text='Like & Comment', command=self.UserId_Target_LikeNComment)
        userId_likeNComment.grid(column=3, row=1)

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

        comment_register = tkinter.Button(target_tab, text='register', command=self.comment_click)
        comment_register.grid(column=2, row=1)

        comment_delete_button = tkinter.Button(target_tab, text='delete', command=self.comment_delete)
        comment_delete_button.grid(column=2, row=3)

    def registered_comments_list(self, target_tab):
        registered_comments_title = tkinter.Label(target_tab, text='registered comments')
        registered_comments_title.grid(column=1, row=2, pady=5)
        self.comment_listbox = tkinter.Listbox(target_tab, selectmode='extended', height=0)
        self.comment_listbox.grid(column=1, row=3)
        for i, comment in enumerate(self.registered_comments):
            self.comment_listbox.insert(i, comment)





    def ignoreTabInitialize(self):
        sys.stdin = open('./ignoreList.txt','r')
        self.registered_words = input().split()

        self.tab4 = tkinter.Frame(self)
        self.tab.add(self.tab4, text="ignore text list")
        self.words_register(self.tab4)
        self.registered_words_list(self.tab4)

    def words_register(self, target_tab):
        wordsTitle = tkinter.Label(target_tab, text='words register')
        wordsTitle.grid(row=0, column=1)

        wordss = tkinter.Label(target_tab, text='words')
        wordss.grid(row=1, column=0)
        self.words_value = tkinter.StringVar()
        self.words_entry = tkinter.Entry(target_tab, textvariable=self.words_value)
        self.words_entry.grid(column=1, row=1)

        words_register = tkinter.Button(target_tab, text='register', command=self.words_click)
        words_register.grid(column=2, row=1)

        words_delete_button = tkinter.Button(target_tab, text='delete', command=self.words_delete)
        words_delete_button.grid(column=2, row=3)

    def registered_words_list(self, target_tab):
        registered_words_title = tkinter.Label(target_tab, text='registered_word_list')
        registered_words_title.grid(column=1, row=2, pady=5)

        self.words_listbox = tkinter.Listbox(target_tab, selectmode='extended', height=0)
        self.words_listbox.grid(column=1, row=3)
        for i, word in enumerate(self.registered_words):
            self.words_listbox.insert(i, word)







    def user_click_press(self):
        try:
            if not self.account_value.get() or not self.password_value.get():
                self.user_label['fg'] = 'red'
                self.user_label_value.set("enter the value")
            else:
                self.user_label_value.set("")
                self.user_information['username'] = self.account_value.get()
                self.user_information['password'] = self.password_value.get()
                self.password_value.set('')
                self.user_label_value.set("saved")
                self.session = InstaPy(username=self.user_information['username'], 
                                        password=self.user_information['password'], headless_browser=True)            
                self.session.set_blacklist ( enabled = True , campaign = ' soccer_campaign ' )

        except Exception as error:
            tkinter.messagebox.showinfo("warning", error)


    def user_enter_press(self, event):
        self.user_click_press()





    def hashtag_click(self):
        try:
            if self.hashtag_value.get():
                with open('./hashtagList.txt', 'a') as HL:
                    HL.write(self.hashtag_value.get()+' ')
                self.hashtag_listbox.insert(len(self.registered_hashtags), self.hashtag_value.get())
                self.registered_hashtags += [self.hashtag_value.get()]
                self.hashtag_value.set('')
        except Exception as error:
            tkinter.messagebox.showinfo("warning", error)
    
    def hashtag_delete(self):
        try:
            choice = self.hashtag_listbox.curselection()
            self.hashtag_listbox.delete(choice[0], choice[-1])
            for _ in choice:
                self.registered_hashtags.pop(choice[0])
            
            with open('./hashtagList.txt', 'w') as HL:
                HL.write(' '.join(self.registered_hashtags)+' ')
        except Exception as error:
            tkinter.messagebox.showinfo("warning", error)








    
    def userid_click(self):
        try:
            if self.userId_value.get():
                with open('./userIdList.txt', 'a') as UL:
                    UL.write(self.userId_value.get()+' ')
                self.userid_listbox.insert(len(self.registered_userids), self.userId_value.get())
                self.registered_userids += [self.userId_value.get()]
                self.userId_value.set('')
        except Exception as error:
            tkinter.messagebox.showinfo("warning", error)


    def userid_delete(self):
        try:
            choice = self.userid_listbox.curselection()
            self.userid_listbox.delete(choice[0], choice[-1])
            for _ in choice:
                self.registered_userids.pop(choice[0])
            
            with open('./userIdList.txt', 'w') as UL:
                UL.write(' '.join(self.registered_userids)+' ')
        except Exception as error:
            tkinter.messagebox.showinfo("warning", error)








    def comment_click(self):
        try:
            if self.comment_value.get():
                with open('./commentList.txt', 'a') as CL:
                    CL.write(self.comment_value.get()+' ')
                self.comment_listbox.insert(len(self.registered_comments), self.comment_value.get())
                self.registered_comments += [self.comment_value.get()]
                self.comment_value.set('')
        except Exception as error:
            tkinter.messagebox.showinfo("warning", error)

    def comment_delete(self):
        try:
            choice = self.comment_listbox.curselection()
            self.comment_listbox.delete(choice[0], choice[-1])
            for _ in choice:
                self.registered_comments.pop(choice[0])
            
            with open('./commentList.txt', 'w') as CL:
                CL.write(' '.join(self.registered_comments)+' ')
        except Exception as error:
            tkinter.messagebox.showinfo("warning", error)










    def words_click(self):
        try:
            if self.words_value.get():
                with open('./ignoreList.txt', 'a') as IL:
                    IL.write(self.words_value.get()+' ')
                self.words_listbox.insert(len(self.registered_words), self.words_value.get())
                self.registered_words += [self.words_value.get()]
                self.words_value.set('')
        except Exception as error:
            tkinter.messagebox.showinfo("warning", error)

    def words_delete(self):
        try:
            choice = self.words_listbox.curselection()
            self.words_listbox.delete(choice[0], choice[-1])
            for _ in choice:
                self.registered_words.pop(choice[0])
            
            with open('./ignoreList.txt', 'w') as IL:
                IL.write(' '.join(self.registered_words)+' ')
        except Exception as error:
            tkinter.messagebox.showinfo("warning", error)
    


    def applyTheLimit(self):
        try:
            print(1)
            self.session.set_quota_supervisor(enabled=True, sleepyhead=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], stochastic_flow=True, notify_me=True,
                peak_likes=(int(self.likeHourLimitSpinbox.get()), int(self.likeDayLimitSpinbox.get())),
                peak_follows=(int(self.followHourLimitSpinbox.get()), int(self.followDayLimitSpinbox.get())),
                peak_unfollows=(int(self.unfollowHourLimitSpinbox.get()), int(self.unfollowDayLimitSpinbox.get())),
                peak_server_calls=(int(self.serverHourLimitSpinbox.get()), int(self.serverDayLimitSpinbox.get())))
        except AttributeError:
            tkinter.messagebox.showinfo("warning", 'Please Enter UserInformation')
        except Exception as error:
            tkinter.messagebox.showinfo("warning", error)




    def hashTag_Target_LikeNComment(self):
        try:
            self.session.set_ignore_if_contains(self.registered_words)
            self.session.set_do_follow(True, percentage=100)
            self.session.set_comments(self.registered_comments)
            self.session.set_do_comment(enabled=True, percentage=80)
            self.session.set_user_interact(amount=3, randomize=True, percentage=100)
            self.session.set_do_like(True, percentage=100)
            if self.isSessionRun:
                self.session.set_dont_include(self.followers)
                self.session.like_by_tags(self.hashtag_listbox.curselection())
            else:
                with smart_run(self.session):
                    self.followers = self.session.grab_followers(username=self.user_information['username'], amount="full", live_match=True, store_locally=True)
                    self.session.set_dont_include(self.followers)
                    self.session.like_by_tags([self.registered_hashtags[i] for i in self.hashtag_listbox.curselection()])
                    self.isSessionRun = True

        except Exception as error:
            tkinter.messagebox.showinfo("warning", error)

    def UserId_Target_LikeNComment(self):
        try:
            self.session.set_comments(self.registered_comments)
            self.session.set_do_comment(enabled=True, percentage=100)
            self.session.set_do_like(True, percentage=100)
            if self.isSessionRun:
                self.session.interact_by_users(self.registered_userids, randomize=True)
            else:
                with smart_run(self.session):
                    self.session.interact_by_users(self.registered_userids, randomize=True)
                    self.isSessionRun = True
        except Exception as error:
            tkinter.messagebox.showinfo("warning", error)




app = SimpleApp(None)
app.title = 'Grapic User Interface'
app.mainloop()
