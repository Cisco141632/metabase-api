from metabase_api_python import MetabaseAPI

metabase_api = MetabaseAPI(
	base_url="http://localhost:3000", 
	user_name="xxxxxx@gmail.com", 
	password="xxxxxx"
)

# Get Question Reponse
question_response = metabase_api.get_data_from_saved_metabase_question(
	card_id=65
)
print(question_response)


# Get Question Reponse using parameters
payload =  [
    {
        "type": "text",
        "value": "borer-hudson@yahoo.com",
        "target": ["variable", ["template-tag", "email"]]
        
    }
]

question_response = metabase_api.get_data_from_saved_metabase_question(
	card_id=65,params=payload
)
print(question_response)


# Archive Question
metabase_api.archive_card(
	card_id=65
)