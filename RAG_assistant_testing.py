import autogen

from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
import chromadb
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

assistant = RetrieveAssistantAgent(
    name="assistant", 
    system_message="You are a helpful assistant.",
    llm_config={
        "request_timeout": 600,
        "seed": 42,
        "config_list": config_list,
    },
)

ragproxyagent = RetrieveUserProxyAgent(
    name="ragproxyagent",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    retrieve_config={
        "task": "code",
        "docs_path": "data", 
        "chunk_token_size": 1000,
        "model": config_list[0]["model"],
        "client": chromadb.PersistentClient(path="db"),
        "embedding_model": "all-mpnet-base-v2",
        "get_or_create": False,
    },
)

ragproxyagent = RetrieveUserProxyAgent(
    name="ragproxyagent",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    retrieve_config={
        "task": "qa",  
        "model": config_list[0]["model"],
        "client": chromadb.PersistentClient(path="db"),
        "embedding_model": "all-mpnet-base-v2",
        "get_or_create": False, 
    },
)
assistant.reset()
problem = "Who is the ceo of liberate labs?"
ragproxyagent.initiate_chat(assistant, problem=problem)  
