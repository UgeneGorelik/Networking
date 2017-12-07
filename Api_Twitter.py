import requests
import requests_oauthlib , sys
import json

consumer_key= "mTqOUvCkEyjtnPbTMcje7dTCy"
consumer_secret ='ehUG5wDThbnwwDrpb8RbWZQmFXG8bo9CQ6ZfCSUJw40C4THJm3'
accsess_token="937953221183725568-3D0nEIclOfyMiXQYUal6oOMbmV2azTO"
accsess_secret="8oHcaNZ8gv1AfL5tJKAhrKkp3qsBmh2oBcisjQTUTqYjj"

def init_auth():
    auth_obj=requests_oauthlib.OAuth1(consumer_key,consumer_secret,accsess_token,accsess_secret)

    if verify_credentials(auth_obj):
        print('CR ok')
        return  auth_obj
    else:
        print(("CR bad"))
        sys.exit(1)

def verify_credentials(auth_obj):
    url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    response =requests.get(url ,auth=auth_obj)

    return  response.status_code==200

def get_mentions(since_id, auth_obj):
    params = {'count': 200, 'since_id': since_id,'include_rts':  0, 'include_entities': 'false'}
    url = 'https://api.twitter.com/1.1/statuses/mentions_timeline.json'
    response = requests.get(url, params=params, auth=auth_obj)
    response.raise_for_status()
    return json.loads(response.text)

def post_reply(reply_to_id, text, auth_obj):
    params = {'status': text,'in_reply_to_status_id': reply_to_id}
    url = 'https://api.twitter.com/1.1/statuses/update.json'
    response = requests.post(url, params=params, auth=auth_obj)
    response.raise_for_status()


if __name__ == '__main__':
    auth_obj = init_auth()
    since_id = 1
    for tweet in get_mentions(since_id, auth_obj):
        print(tweet['text'])
        post_reply(tweet['id'],"reply",auth_obj)