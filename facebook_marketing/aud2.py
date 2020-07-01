# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.customaudience import CustomAudience
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adpreview import AdPreview
from facebook_business.api import FacebookAdsApi

access_token = 'EAAMe1ViNqZAkBAKJYbKZBow49DKe8vSZCsWa2kKgL5cj89JLH6ncp872zaxWiryU3iYnYZCMVJNZCcNEtlnGhySaCsQ6apGpOQHeoW4QcyEDtcSx2QjimwzWFZCdq6izgPvOvG0VPVY1oRHbaGVXZAFzZBZCIeJRUgmSO2ayMqGljUjcdPMz7ZCiAiOZBHBU7xYoQwZD'
app_secret = '1cddcfaae9c2b852188bef2520b086c9'
ad_account_id = 'act_373503683609460'
audience_name = 'test'
audience_retention_days = '30'
pixel_id = '746309156138914'
app_id = '878326592678297'
FacebookAdsApi.init(access_token=access_token)

# fields = [
# ]
# params = {
#     'name': 'My Campaign',
#     'buying_type': 'AUCTION',
#     'objective': 'LINK_CLICKS',
#     'status': 'PAUSED',
# }
# campaign = AdAccount(ad_account_id).create_campaign(
#     fields=fields,
#     params=params,
# )
# print ('campaign', campaign)
#
# campaign_id = campaign.get_id()
# print ('campaign_id:', campaign_id, '\n')
#
# fields = [
# ]
# params = {
#     'pixel_id': pixel_id,
#     'name': audience_name,
#     'subtype': 'WEBSITE',
#     'retention_days': audience_retention_days,
#     'rule': {'url':{'i_contains':''}},
#     'prefill': true,
# }
# custom_audience = AdAccount(ad_account_id).create_custom_audience(
#     fields=fields,
#     params=params,
# )
# print ('custom_audience', custom_audience)
#
# custom_audience_id = custom_audience.get_id()
# print ('custom_audience_id:', custom_audience_id, '\n')
#
# fields = [
# ]
# params = {
#     'name': 'My AdSet',
#     'optimization_goal': 'REACH',
#     'billing_event': 'IMPRESSIONS',
#     'bid_amount': '20',
#     'daily_budget': '1000',
#     'campaign_id': campaign_id,
#     'targeting': {'custom_audiences':[{'id':custom_audience_id}], 'geo_locations':{'countries':['US']}},
#     'status': 'PAUSED',
# }
# ad_set = AdAccount(ad_account_id).create_ad_set(
#     fields=fields,
#     params=params,
# )
# print ('ad_set', ad_set)
#
# ad_set_id = ad_set.get_id()
# print ('ad_set_id:', ad_set_id, '\n')
#
# fields = [
# ]
# params = {
#     'name': 'My Creative',
#     'title': 'My Page Like Ad',
#     'body': 'Like My Page',
#     'object_url': 'www.facebook.com',
#     'link_url': 'www.facebook.com',
#     'image_url': 'http://www.facebookmarketingdevelopers.com/static/images/resource_1.jpg',
# }
# creative = AdAccount(ad_account_id).create_ad_creative(
#     fields=fields,
#     params=params,
# )
# print ('creative', creative)
#
# creative_id = creative.get_id()
# print ('creative_id:', creative_id, '\n')
from facebook_business.adobjects.customaudience import CustomAudience

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


FacebookAdsApi.init(access_token=dict1['my_access_token'])
audience = CustomAudience(parent_id='act_id')
audience[CustomAudience.Field.subtype] = CustomAudience.Subtype.custom
audience[CustomAudience.Field.name] = 'My new CA'
audience[CustomAudience.Field.description] = 'People who bought on my website'
audience[CustomAudience.Field.countries]= "USA"
audience[CustomAudience.Field.gender]= "Male"

audience.remote_create()

