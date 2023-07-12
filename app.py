from clavesAPI import OPENAI_API_KEY
openai_api_key=OPENAI_API_KEY

from langchain.chat_models import ChatOpenAI
from langchain.chains import TransformChain, LLMChain, SimpleSequentialChain
from langchain.chains import create_tagging_chain, create_tagging_chain_pydantic
from langchain.prompts import PromptTemplate, ChatPromptTemplate

