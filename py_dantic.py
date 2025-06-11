from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
model = ChatOpenAI(model_name="gpt-4", api_key=st.secrets['api_key'], temperature=0)
st.title("Review Analysis")
class Student(BaseModel):
    Sentiment: Literal["Positive", "Negative", "Neutral"] = Field(description="Return sentiment of the review either negative, positive or neutral")
    Key_Themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    Summary: str = Field(description="A brief summary of the review")
    Pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
    Cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list")
    Name: Optional[str] = Field(default=None, description="Write the name of the reviewer")

# ⚠️ Fix this too: You're referencing "Review" instead of "Student"
structured_model = model.with_structured_output(Student)
review=st.text_input("Enter your review")
# result = structured_model.invoke("""
# I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

# The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

# However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

# Pros:
# Insanely powerful processor (great for gaming and productivity)
# Stunning 200MP camera with incredible zoom capabilities
# Long battery life with fast charging
# S-Pen support is unique and useful
                                 
# Review by Nitish Singh
# """)

# print(result)

if st.button('Summarize'):
    # ✅ Send the final string to the model
    
    result = structured_model.invoke(review)

    # ✅ Show model output
    st.write(result)
