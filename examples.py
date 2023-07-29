from metabase_api import MetabaseAPI

metabase_api = MetabaseAPI(
	base_url="http://localhost:3000", 
	user_name="durgaprasad141632@gmail.com", 
	password="Vcy5ka@@"
)

payload =  [
        {
            "type": "text",
            "value": "borer-hudson@yahoo.com",
            "target": ["variable", ["template-tag", "email"]]
            
        }
    ]

print(metabase_api.access_token)

question_response = metabase_api.get_data_from_saved_metabase_question(
	card_id=65
)
print(question_response)
