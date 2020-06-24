
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi

access_token = 'EAAIBXnH6dpoBABQUXtk7rZBQHDI3V7ZBsRfUoty2BmXdcf0xqslRA3FwnElUqOceCeYGnx1Qo9AWoxRdisPveIuqo7bF5LJlGolQ2WblBZAWuAVBqVJ5V3KBV1MNtbVZBLG7DaHHNK1C6tJV5GPCrHmmhyf6AE0OrcxHPHNg636TLYSuBVQaZBl3bCDcQEucZD'
app_secret = '638a132cb4b3d2b290f23b6385732820'
app_id = '564455104214682'
id = '311327033205854'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'My campaign',
  'objective': 'LINK_CLICKS',
  'status': 'PAUSED',
  'special_ad_categories': [],
}
print (AdAccount(id).create_campaign(
  fields=fields,
  params=params,
))

