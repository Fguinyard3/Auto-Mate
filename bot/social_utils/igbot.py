import requests
from bot.models import AccessKey, SocialMedia



def get_client_id(key, secret):
    url = 'https://graph.facebook.com/v13.0/oauth/access_token?grant_type=fb_exchange_token&client_id={}&client_secret={}


def get_60d_access_token(key, secret):
    url = 'https://graph.facebook.com/v13.0/oauth/access_token?grant_type=fb_exchange_token&client_id={}&client_secret={}