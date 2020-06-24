from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.session import FacebookSession
session = FacebookSession.debug
print(session)
def createCampaign(my_app_id,my_app_secret,account_id,my_access_token):
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    fields = [
    ]
    account = AdAccount(account_id)
    campaign = account.create_campaign(fields=fields,params= {

        'name': 'Lets Talk Openly',
        'buying_type': 'AUCTION',
        'objective': 'LINK_CLICKS',
        'status': 'PAUSED',
        'special_ad_categories':'None',
    })
    print('campaign', campaign)



dict1 =dict()
dict1['my_app_id'] = '878326592678297'
dict1['account_id'] = 'act_373503683609460'
dict1['my_app_secret'] = '1cddcfaae9c2b852188bef2520b086c9'
dict1['my_access_token'] = 'EAAMe1ViNqZAkBANZCITfMsZCSZCKVEFlhB7aOAOkQNY0A3ZCobIeFUZCjGxa01DZA7HhCxGEhRuwrgx2lAugiFbTLP3olfodaie3Whpdy4u0XeVSMTGj2CwHB9xnhfkxkZBy52LtNK0xMGe0GZA85QZAgu0YcaKMjmCa5aaeFhGOh28f4uUYeJZBZBlCaCLlZBZA6dpDgZD'


# createCampaign(my_app_id=dict1['my_app_id'],account_id=dict1['account_id'],my_app_secret=dict1['my_app_secret'],my_access_token=dict1['my_access_token'])



def getCampaign():
    FacebookAdsApi.init(app_id=dict1['my_app_id'] ,app_secret= dict1['my_app_secret'], account_id=dict1['account_id'] ,access_token=dict1['my_access_token'])
    fields = []
    account = AdAccount(dict1['account_id'])
    campaigns = account.get_campaigns()
    print(campaigns)

getCampaign()