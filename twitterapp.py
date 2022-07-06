from pytwitter import Api
import json

api = Api(bearer_token = 'AAAAAAAAAAAAAAAAAAAAAFNSeQEAAAAAayPWo8IHonqMSkMAZxDBemHu3JA%3D5yaETCA3pDYOSjepwVGxKayvgy1VIwUPqOWaz1HSAJ2YZBwtFQ')


def get_username(id):
    response = api.get_user(user_id = id)
    return response.data.username


def get_following(id):
    response = api.get_following(user_id = id, max_results = 100)
    return response.data


def get_followers(id):
    response = api.get_followers(user_id = id, max_results = 100)
    return response.data


def main():
    following = get_following("1542616796888309760")
    for account in following:
        print(account.name)

    followers = get_followers("1542616796888309760")
    for follower in followers:
        print(follower.username)

   

if __name__ == "__main__":
    main()