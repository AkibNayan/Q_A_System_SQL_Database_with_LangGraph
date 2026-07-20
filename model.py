from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import HuggingFacePipeline

model_id = "microsoft/Phi-3-mini-4k-instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

pipe = pipeline(
    "text-generation", model=model, tokenizer=tokenizer, max_new_tokens=1024
)

llm = HuggingFacePipeline(pipeline=pipe)
