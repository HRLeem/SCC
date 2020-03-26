email = 'dlagkfka93@naver.com'


def check_mail(email):
    return email.find('@') > -1


print(check_mail(email))


def get_mail(email):
    return email.split('@')[1].split('.')[0]


print(get_mail(email))
