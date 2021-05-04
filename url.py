import bitly_api 


API_USER = "brittlevader"
API_KEY ="0963f4fc93105f14e6f6308c81def2248b6c5e6c" 

response = bitly_api.connection(API_USER, API_KEY)

print(response)