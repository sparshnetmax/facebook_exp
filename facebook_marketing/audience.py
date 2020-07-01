from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.customaudience import CustomAudience
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.customaudience import CustomAudience
from facebook_business.adobjects.targeting import Targeting

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


def getAudience():
    access_token = dict1['my_access_token']
    app_secret = dict1['my_app_secret']
    app_id = dict1['my_app_id']
    id = dict1['account_id']
    FacebookAdsApi.init(access_token=access_token)

    fields = [
      'id',
    ]
    params = {
    }
    print( AdAccount(id).get_custom_audiences(
      fields=fields,
      params=params,
    ))
def CreateAudience():
    access_token = dict1['my_access_token']
    app_secret = dict1['my_app_secret']
    app_id = dict1['my_app_id']
    id = dict1['account_id']
    FacebookAdsApi.init(access_token=access_token)
    custAud = CustomAudience(parent_id=dict1['account_id'])
    custAud[CustomAudience.Field.name]= 'My audience'
    custAud[CustomAudience.Field.description]="My audience description"
    custAud[Targeting.Field.age_max]=30
    custAud[Targeting.Field.age_min]=20
    custAud[Targeting.Field.countries]=['US']
    custAud[Targeting.Field.connections] = ''
    custAud[CustomAudience.Field.customer_file_source]='USER_PROVIDED_ONLY'
    custAud[CustomAudience.Field.subtype] = 'CUSTOM'
    custAud.remote_create(params={'customer_file_source':0,'subtype':0})
    print(custAud)

# CreateAudience()