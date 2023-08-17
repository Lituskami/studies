import random

when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan','Tomorrow?']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat', 'a machine']
name = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker', 'Carlin']
residence = ['Barcelona','India', 'Germany', 'Venice', 'England', 'Coreto']
went = ['cinema', 'university','seminar', 'school', 'laundry', 'boca']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']


if when == 'Tomorrow?':
    print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', will go to ' + random.choice(went) + ' and ' + random.choice(happened))

print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))