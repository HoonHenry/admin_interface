# info = {"id": 'asdf', "password": 'asdfasdf', "phone_number": "010-1234-1234", "email": "asdf@asdf.com"}
import pandas as pd

# get inputs from html form
def get_userinfo(**kwargs):
    user = kwargs
    print(user)
    return user


def make_csv(user):
    users = []
    df = pd.read_csv('test.csv', index_col=0)
    df = pd.DataFrame.from_dict(user, orient='index')
    a = df.to_csv('test.csv')
    print()
    return users


def show_infos():
    pass





