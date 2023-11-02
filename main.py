import autogen
import dotenv
import os


dotenv.load_dotenv('.env')

OPEN_API_KEY = os.getenv(key="OPENAI_API_KEY")

config_list=[
        {
            "model": "gpt-3.5-turbo",
            "api_key": OPEN_API_KEY,
            "api_type": "open_ai",
            "api_base": "https://api.openai.com/v1",
            "api_version": None,
        }
    ]

completion = autogen.Completion.create(
    config_list=config_list,
    prompt = "Hello how are you?",
    use_cache=True,
    )

reply_content = completion.choices[0].message.content
logs = autogen.ChatCompletion.logged_history
print(reply_content)