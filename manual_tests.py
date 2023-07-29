from metabase_api import *

metabase_api = MetabaseAPI(
	base_url="http://localhost:3000", 
	user_name="xxxxx@gmail.com", 
	password="xxxxx"
)

payload =  [
        {
            "type": "text",
            "value": "borer-hudson@yahoo.com",
            "target": ["variable", ["template-tag", "email"]]
            
        }
    ]

print(metabase_api.access_token)

question_response = metabase_api.archive_card(
	card_id=33
)
print(question_response)
