from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.ad import Ad
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adcreative import AdCreative
dict1 =dict()
dict1['my_app_id'] = '878326592678297'
dict1['account_id'] = 'act_373503683609460'
dict1['my_app_secret'] = '1cddcfaae9c2b852188bef2520b086c9'
dict1['my_access_token'] = 'EAAMe1ViNqZAkBANZCITfMsZCSZCKVEFlhB7aOAOkQNY0A3ZCobIeFUZCjGxa01DZA7HhCxGEhRuwrgx2lAugiFbTLP3olfodaie3Whpdy4u0XeVSMTGj2CwHB9xnhfkxkZBy52LtNK0xMGe0GZA85QZAgu0YcaKMjmCa5aaeFhGOh28f4uUYeJZBZBlCaCLlZBZA6dpDgZD'
dict1['page_id'] = '1357440557629733'
dict1['campaign_id'] = '120330000451984803'
dict1['image_path'] = r'C:\test.jpg'
dict1['ad']= '120330000451987503'
dict1['page_id'] = '1357440557629733'
def creative(my_app_id,my_app_secret,my_access_token,account_id,page_id):
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token,)
    account = AdAccount(account_id)



    fields = [
    ]
    params = {
        'name': 'crative 1',
        'object_id': 173982236872898,
        'title': 'IMPRESSIONS',
        'image_url': 'https://image.shutterstock.com/z/stock-photo-white-transparent-leaf-on-mirror-surface-with-reflection-on-turquoise-background-macro-artistic-1029171697.jpg',
        'body': 'Hello everyone',

    }
    creative = AdCreative(parent_id=account_id).api_create(
        fields=fields,
        params=params,
        parent_id=dict1['account_id']
    )
    print( 'creative', creative)
    creative_id = creative.get_id()
    print ('creative_id:', creative_id, '\n')

creative(my_app_id=dict1['my_app_id'],my_app_secret=dict1['my_app_secret'],
              my_access_token=dict1['my_access_token'],account_id=dict1['account_id'],page_id=dict1['page_id'])

