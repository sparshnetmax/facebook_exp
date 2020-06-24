from facebookads.adobjects.adimage import AdImage
from facebookads.adobjects.adasyncrequestset import AdAsyncRequestSet
from facebook_business.api import FacebookAdsApi
dict1 =dict()
dict1['my_app_id'] = '878326592678297'
dict1['account_id'] = 'act_373503683609460'
dict1['my_app_secret'] = '1cddcfaae9c2b852188bef2520b086c9'
dict1['my_access_token'] = 'EAAMe1ViNqZAkBANZCITfMsZCSZCKVEFlhB7aOAOkQNY0A3ZCobIeFUZCjGxa01DZA7HhCxGEhRuwrgx2lAugiFbTLP3olfodaie3Whpdy4u0XeVSMTGj2CwHB9xnhfkxkZBy52LtNK0xMGe0GZA85QZAgu0YcaKMjmCa5aaeFhGOh28f4uUYeJZBZBlCaCLlZBZA6dpDgZD'

FacebookAdsApi.init(dict1['my_app_id'] , dict1['my_app_secret'], dict1['my_access_token'])

request_set = AdAsyncRequestSet('120330000451987503')
request_set.remote_read(fields=[
    AdAsyncRequestSet.Field.name,
    AdAsyncRequestSet.Field.success_count,
    AdAsyncRequestSet.Field.error_count,
    AdAsyncRequestSet.Field.is_completed,
])
# image = AdImage(parent_id='878326592678297')
# image[AdImage.Field.filename] = r'C:\test.jpg'
# image.remote_create()
#
# # Output image Hash
# print(image[AdImage.Field.hash])