import os
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

load_dotenv()

# llm_config = { "config_list": [{ "model": "gpt-4", "api_key": os.environ.get("OPENAI_API_KEY") }] }

llm_config = {
    "config_list": [
        {
            "model": "gpt-4o-mini",  # This is your Azure deployment name
            "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
            "base_url": os.getenv("AZURE_OPENAI_BASE_URL"),  # ✅ Note: ends with slash, no /deployments
            "api_type": "azure",
            "api_version": "2024-12-01-preview"
        }
    ]
}



assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", code_execution_config=False,max_consecutive_auto_reply=4)

user_proxy.initiate_chat(
    assistant,
    message= "Write an professional email to my supervisor akash for leave on 10th and 11th of march"
)
