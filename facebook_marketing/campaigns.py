from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.session import FacebookSession

def createCampaign(my_app_id,my_app_secret,account_id,my_access_token):
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    fields = [
    ]
    account = AdAccount(account_id)
    campaign = account.create_campaign(fields=fields,params= {
        'name': 'Lets Talk Openly','buying_type': 'AUCTION',
        'objective': 'LINK_CLICKS',
        'status': 'PAUSED',
        'special_ad_categories':'None',
        'targeting': {'age_min': 20, 'age_max': 35,'genders':[1],'geo_locations':{'countries':['US']}
                      }})

    print('campaign', campaign)
#


dict1 =dict()
dict1['my_app_id'] = '878326592678297'
dict1['account_id'] = 'act_373503683609460'
dict1['my_app_secret'] = '1cddcfaae9c2b852188bef2520b086c9'
dict1['my_access_token'] = 'EAAMe1ViNqZAkBAF1F0pHcwdlq2buBggSwGIAaYO8PIhQOwNAXAyvOLc5nZBI9dIZA4ZAVcA6isStGWiWemwX8TRxy7hUhDAHjw93MP1ecubzw4ZACv2M3vJrZB1Icfnz30LnZCyJyeH3bZCfOZBA3Ux6t5flvLKZAncfg1ZBnZCL7SGXo8ZAbkZAb4wNrfBhQX1gvn8mwZD'


# createCampaign(my_app_id=dict1['my_app_id'],account_id=dict1['account_id'],my_app_secret=dict1['my_app_secret'],my_access_token=dict1['my_access_token'])

def getCampaign():
    FacebookAdsApi.init(app_id=dict1['my_app_id'] ,app_secret= dict1['my_app_secret'], account_id=dict1['account_id'] ,access_token=dict1['my_access_token'])
    fields = ['id','name','objective']
    account = AdAccount(dict1['account_id'])
    campaigns = account.get_campaigns(fields=fields)
    for i in campaigns:
        if i['id']=='120330000453089803':
            print(i)
getCampaign()

