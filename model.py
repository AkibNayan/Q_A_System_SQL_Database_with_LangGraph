from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os
from dotenv import load_dotenv

load_dotenv()

"""from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import HuggingFacePipeline


model_id = "microsoft/Phi-3-mini-4k-instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

pipe = pipeline(
    "text-generation", model=model, tokenizer=tokenizer, max_new_tokens=1024
)

llm = HuggingFacePipeline(pipeline=pipe)"""

sql_agent_api = os.getenv("sql_agent_api")

model = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    huggingfacehub_api_token=sql_agent_api,
    temperature=0,
    max_new_tokens=1024,
)

llm = ChatHuggingFace(llm=model)
