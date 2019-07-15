# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'yyyeh12'
insta_password = 'qhsorl2'

comments = ['Nice shot! @{}',
        'I love your profile! @{}',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    # """ Activity flow """		
    # general settings		
    #session.set_dont_include(["friend1", "friend2", "friend3"])		
    # try:
    #     dismiss_notification_offer(browser, logger)
    # except:
    #     print("There is no Notification")

    # activity
    session.like_by_tags(["슬라임"], amount=1)

#   # Joining Engagement Pods
#   session.set_do_comment(enabled=True, percentage=35)
#   session.set_comments(comments)
#   session.join_pods()
