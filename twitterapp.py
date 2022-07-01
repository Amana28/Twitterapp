from pytwitter import Api

api = Api(bearer_token = 'AAAAAAAAAAAAAAAAAAAAAFNSeQEAAAAAayPWo8IHonqMSkMAZxDBemHu3JA%3D5yaETCA3pDYOSjepwVGxKayvgy1VIwUPqOWaz1HSAJ2YZBwtFQ')
id = api.get_users(ids=["783214", "2244994945"])

print(id)