from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebookads.adobjects.adcreativeobjectstoryspec import AdCreativeObjectStorySpec
from facebook_business.adobjects.adcreative import AdCreative
from facebookads.adobjects.adcreativelinkdata import AdCreativeLinkData
import time
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adsinsights import AdsInsights
from facebookads.adobjects.adreportrun import AdReportRun
from facebookads.api import FacebookAdsApi


dict1 =dict()

dict1['my_app_id'] = '878326592678297'
dict1['account_id'] = 'act_373503683609460'
dict1['my_app_secret'] = '1cddcfaae9c2b852188bef2520b086c9'
dict1['my_access_token'] = 'EAAMe1ViNqZAkBAIcJOgdOFyNVuqMfgvvR8o7KjLg4bJLc0TJ3zNTiV9HZASyXC2L3oC7CqmN4HQNqwlSsWT5ZClOBWcfhT7NDBPppO3ZCnGQZBmHr8OXXJv1HxS8AoBIByn4OgIXcbt88ZA7wZCPNDm5scMMlQ7N1PMWcpaHjyKZCBlEakMMjlBI5WPFrlWiZCLAZD'
dict1['page_id'] = 1357440557629733
dict1['campaign_id'] = '120330000451984803'
dict1['image_path'] = r'C:\test.jpg'
dict1['ad']= '120330000451987503'
dict1['page_id'] = '1357440557629733'

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.customaudience import CustomAudience
from facebook_business.api import FacebookAdsApi

access_token = dict1['my_access_token']
app_secret = dict1['my_app_secret']
app_id = dict1['my_app_id']
id =dict1['account_id']

FacebookAdsApi.init(access_token=access_token)
time.sleep(1)
fields = []
params = {'name': 'test audience',
  'rule': {'inclusions':{'operator':'or','rules':[{'event_sources':[{'id':dict1['page_id'],'type':'page'}],'retention_seconds':31536000,'filter':{'operator':'and','filters':[{'field':'event','operator':'eq','value':'page_engaged'}]}}]}},
  'prefill': '1'}
print( AdAccount(id).create_custom_audience(
  fields=fields,params=params
))

