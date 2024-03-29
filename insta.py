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
                  headless_browser=True)

with smart_run(session):
    # """ Activity flow """		
    # general settings		
    #session.set_dont_include(["friend1", "friend2", "friend3"])		
    # try:
    #     dismiss_notification_offer(browser, logger)
    # except:
    #     print("There is no Notification")
    session.set_do_follow(True, percentage=100, times=1)
    session.set_comments([u'Nice shot! :heart:', u'Really nice! :thumbsup:', u'Loving your work! :smile:', u'This photo is :fire:', u'Great work! :heart:', u'Love it! :heart: :thumbsup:'])
    session.set_do_comment(enabled=True, percentage=100)
    session.set_user_interact(amount=3, randomize=True, percentage=100)

    # activity
    # session.set_do_comment (enabled = True, percentage=100)
    # session.set_comments(comments='wow')
    session.like_by_tags(["슬라임"], amount=3)

#   # Joining Engagement Pods
#   session.set_do_comment(enabled=True, percentage=35)
#   session.set_comments(comments)
#   session.join_pods()
