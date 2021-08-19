from instapy import InstaPy

session = InstaPy(username="ig kullanıcı adınız", password="şifreniz")
session.login()
session.like_by_tags(["german engineers", "turkey"], amount=5)
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["nice", "iyiymiş knk", "Beautiful :heart_eyes:"])
session.end()