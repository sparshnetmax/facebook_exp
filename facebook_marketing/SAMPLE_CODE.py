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
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adpreview import AdPreview
from facebook_business.api import FacebookAdsApi

access_token = 'EAAMe1ViNqZAkBANZCITfMsZCSZCKVEFlhB7aOAOkQNY0A3ZCobIeFUZCjGxa01DZA7HhCxGEhRuwrgx2lAugiFbTLP3olfodaie3Whpdy4u0XeVSMTGj2CwHB9xnhfkxkZBy52LtNK0xMGe0GZA85QZAgu0YcaKMjmCa5aaeFhGOh28f4uUYeJZBZBlCaCLlZBZA6dpDgZD'
ad_account_id = 'act_373503683609460'
app_secret = '1cddcfaae9c2b852188bef2520b086c9'
page_id = '1357440557629733'
app_id = '878326592678297'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
    'name': 'Lets Talk Openly',
    'buying_type': 'AUCTION',
    'objective': 'LINK_CLICKS',
    'status': 'PAUSED',
'special_ad_categories':'None',
}
campaign = AdAccount(ad_account_id).create_campaign(
    fields=fields,
    params=params,
)
print ('campaign', campaign)

campaign_id = campaign.get_id()
print( 'campaign_id:', campaign_id, '\n')

fields = [
]
params = {
    'name': 'My AdSet',
    'optimization_goal': 'LANDING_PAGE_VIEWS',
    'billing_event': 'IMPRESSIONS',
    'bid_amount': '10',
    'promoted_object': {'page_id': page_id},
    'daily_budget': '10050',
    'campaign_id': campaign_id,
    'targeting': {'geo_locations':{'countries':['US']}},
    'status': 'PAUSED',
'special_ad_categories':'None',
}
ad_set = AdAccount(ad_account_id).create_ad_set(
    fields=fields,
    params=params,
)
print ('ad_set', ad_set)

ad_set_id = ad_set.get_id()
print ('ad_set_id:', ad_set_id, '\n')

fields = [
]
params = {
    'name': 'My Creative',
    'object_id': page_id,
    'title': 'Like Page',
    'image_url': r'C:\test.jpg',
    'body': 'Like Page',

}
creative = AdAccount(ad_account_id).create_ad_creative(
    fields=fields,
    params=params,
)
print( 'creative', creative)

creative_id = creative.get_id()
print ('creative_id:', creative_id, '\n')

fields = [
]
params = {
    'name': 'My Ad',
    'adset_id': ad_set_id,
    'creative': {'creative_id':creative_id},
    'status': 'PAUSED',
'special_ad_categories':'None',
}
ad = AdAccount(ad_account_id).create_ad(
    fields=fields,
    params=params,
)
print( 'ad', ad)

ad_id = ad.get_id()
print ('ad_id:', ad_id, '\n')

fields = [
]
params = {
    'ad_format': 'DESKTOP_FEED_STANDARD',
    'special_ad_categories':'None',
}
print( Ad(ad_id).get_previews(
    fields=fields,
    params=params,
))


