from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.ad import Ad
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.adimage import AdImage
#

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


def getHashImage():
    FacebookAdsApi.init(app_id=dict1['my_app_id'] ,app_secret= dict1['my_app_secret'], account_id=dict1['account_id'] ,access_token=dict1['my_access_token'])
    fields = []
    account = AdAccount(dict1['account_id'])
    campaigns = account.get_ad_images()
    print(campaigns)
# getHashImage()


def createImageHash(my_app_id,my_app_secret,account_id,my_access_token):
    image = AdImage(parent_id=dict1['account_id'])
    image[AdImage.Field.filename] = 'test.jpg'
    image.remote_create()
    # Output image Hash
    print(image[AdImage.Field.hash])


createImageHash(my_app_id=dict1['my_app_id'],account_id=dict1['account_id'],my_app_secret=dict1['my_app_secret'],my_access_token=dict1['my_access_token'])
