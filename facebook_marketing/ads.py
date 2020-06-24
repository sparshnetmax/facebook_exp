
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.ad import Ad
from facebook_business.api import FacebookAdsApi


dict1 =dict()
dict1['my_app_id'] = '878326592678297'
dict1['account_id'] = 'act_373503683609460'
dict1['my_app_secret'] = '1cddcfaae9c2b852188bef2520b086c9'
dict1['my_access_token'] = 'EAAMe1ViNqZAkBANZCITfMsZCSZCKVEFlhB7aOAOkQNY0A3ZCobIeFUZCjGxa01DZA7HhCxGEhRuwrgx2lAugiFbTLP3olfodaie3Whpdy4u0XeVSMTGj2CwHB9xnhfkxkZBy52LtNK0xMGe0GZA85QZAgu0YcaKMjmCa5aaeFhGOh28f4uUYeJZBZBlCaCLlZBZA6dpDgZD'
dict1['page_id'] = '1357440557629733'
dict1['campaign_id'] = '120330000451984803'
dict1['image_path'] = r'C:\test.jpg'
dict1['ad']= '120330000451987503'
def getAds(my_app_id,my_app_secret,my_access_token,account_id):
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    account = AdAccount(account_id)
    ad_set = account.get_ad_sets()
    print(ad_set)



def createAds(my_app_id,my_app_secret,my_access_token,account_id,ad_set_id):

    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    account = AdAccount(account_id)

    fields = [
    ]
    params = {
        'name': 'My Ad',
        'adset_id': ad_set_id,
        'creative': {'creative_id': creative_id},
        'status': 'PAUSED',
        'special_ad_categories': 'None',
    }
    ad = AdAccount(ad_account_id).create_ad(
        fields=fields,
        params=params,
    )
    print('ad', ad)

    ad_id = ad.get_id()
    print('ad_id:', ad_id, '\n')



createAds(my_app_id=dict1['my_app_id'],my_app_secret=dict1['my_app_secret'],
              my_access_token=dict1['my_access_token'],account_id=dict1['account_id'],ad_set_id=dict1['ad'])




getAds(my_app_id=dict1['my_app_id'],my_app_secret=dict1['my_app_secret'],
              my_access_token=dict1['my_access_token'],account_id=dict1['account_id'])

def create_image_hash(my_app_id=dict1['my_app_id'],
                      my_app_secret=dict1['my_app_secret'],
                      my_access_token=dict1['my_access_token'],
                      account_id=dict1['account_id'],
                      Image_path=dict1['image_path']):

    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

    account = AdAccount(account_id)
    image = AdImage()
    image2 = AdImage(parent_id=None)
    image[AdImage.Field.filename] = Image_path
    image.remote_create()

    # Output image Hash
    print(image[AdImage.Field.hash])

create_image_hash()