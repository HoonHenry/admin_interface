import os
import csv


PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(PATH, type(PATH))
# info = {"id": 'asdf', "password": 'asdfasdf', "phone_number": "010-1234-1234", "email": "asdf@asdf.com"}


# get inputs from html form
def get_userinfo(**kwargs):
    user = kwargs
    print(user)
    return user


def save_to_csv(user):
    file = open(PATH+'/temp_data/test.csv', mode='w')
    writer = csv.writer(file)
    writer.writerow(['id', 'pw', 'name', 'email', 'phone', 'cl'])
    print("Header is prepped")
    writer.writerow(list(user.values()))
    print("A new user info is added")
    return


def show_infos():
    pass





