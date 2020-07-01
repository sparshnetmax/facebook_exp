from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.adaccount import AdAccount
# First, upload the ad image that you will use in your ad creative
# Please refer to Ad Image Create for details.
from facebook_business.adobjects.adcreativeobjectstoryspec import AdCreativeObjectStorySpec
# Then, use the image hash returned from above
dict1 =dict()
dict1['my_app_id'] = '878326592678297'
dict1['account_id'] = 'act_373503683609460'
dict1['my_app_secret'] = '1cddcfaae9c2b852188bef2520b086c9'
dict1['my_access_token'] = 'EAAMe1ViNqZAkBANZCITfMsZCSZCKVEFlhB7aOAOkQNY0A3ZCobIeFUZCjGxa01DZA7HhCxGEhRuwrgx2lAugiFbTLP3olfodaie3Whpdy4u0XeVSMTGj2CwHB9xnhfkxkZBy52LtNK0xMGe0GZA85QZAgu0YcaKMjmCa5aaeFhGOh28f4uUYeJZBZBlCaCLlZBZA6dpDgZD'
dict1['page_id'] = '1357440557629733'
dict1['campaign_id'] = '120330000451984803'
dict1['image_path'] = r'C:\test.jpg'
dict1['ad_set']= '120330000451987503'
dict1['page_id'] = '1357440557629733'
dict1['Image_hash'] = '8bf45e74d7155516987488fb74bd0d01'
dict1['Image_hash_id'] = '373503683609460:8bf45e74d7155516987488fb74bd0d01'
dict1['url'] =  "https://scontent.fixc2-1.fna.fbcdn.net/v/t45.1600-4/106421921_120330000452704003_663442688879659474_n.jpg?_nc_cat=103&_nc_sid=2aac32&_nc_ohc=p467-ZOxvxsAX9ldzSc&_nc_ht=scontent.fixc2-1.fna&oh=aa9117fe9cc3f03ac857dc880843588c&oe=5F1E5CEC"
from facebook_business.api import FacebookAdsApi
FacebookAdsApi.init(app_id=dict1['my_app_id'] ,app_secret= dict1['my_app_secret'], account_id=dict1['account_id'] ,access_token=dict1['my_access_token'])

fields = [
]
params = {
    'name': 'My Creative',
    'object_id': dict1['page_id'],
    'image_url': dict1['url'],
    'Call to Action': 'Like Page',

}
creative = AdAccount(dict1['account_id']).create_ad_creative(
    fields=fields,
    params=params,
)
print( 'creative', creative)

creative_id = creative.get_id()
print ('creative_id:', creative_id, '\n')