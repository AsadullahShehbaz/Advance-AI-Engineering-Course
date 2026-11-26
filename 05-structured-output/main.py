from groq import BadRequestError
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model(
    "openai/gpt-oss-120b",
    model_provider="groq"
)


class CustomerInfo(BaseModel):
    name: str = Field(description="Customer's full name")
    email: str = Field(description="Customer's email")
    skills: list[str] = Field(description="Customer's skills")
    experience: int = Field(ge=0)

customer = CustomerInfo(
    name="Ali",
    email="ali@example.com",
    skills=["Python", "FastAPI"],
    experience=3,
)

structured_model = model.with_structured_output(CustomerInfo)

# result = structured_model.invoke(
#     """Extract customer information:
# My name is Ali Ahmed.
# My email is ali@example.com.
# I have 3 years of experience with Python and FastAPI."""
# )

# print(result)
# print(result.model_dump())

# Validation and Error Handling

structured_model = model.with_structured_output(
    CustomerInfo,
    include_raw=True,
)

result = structured_model.invoke(
  """  Extract customer information:
My name is Ali Ahmed.
My email is ali@example.com.
I have 3 years of experience with Python and FastAPI."""
)

if result["parsing_error"]:
    print("Parsing error:", result["parsing_error"])
elif result["parsed"] is not None:
    print(result["parsed"].model_dump())



