from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field, conlist

# --- Define Output Schema (FIXED) ---
class EmailContent(BaseModel):
    subject: str = Field(
        description="The subject line of the email. Should be concise and descriptive."
    )
    body: str = Field(
        description="The main content of the email. Should be well-formatted with proper greeting, paragraphs, and signature."
    )
    # Added field to prevent Pydantic validation failure based on Instructions
    attachments: conlist(str) = Field(
        default=[],
        description="A list of file names (strings) to be suggested as attachments. Can be empty."
    )

# --- Create Email Generator Agent ---
root_agent = LlmAgent(
    name="email_agent",
    model="gemini-2.5-flash", # Consistent model name
    instruction="""
        You are an Email Generation Assistant.
        Your task is to generate a professional email based on the user's request.

        GUIDELINES:
        - Create an appropriate subject line (concise and relevant)
        - Write a well-structured email body with:
            * Professional greeting
            * Clear and concise main content
            * Appropriate closing
            * Your name as signature
        - Suggest relevant attachments if applicable (empty list if none needed)
        - Keep emails concise but complete

        IMPORTANT: Your response MUST be valid JSON matching the structure of the provided schema.
        DO NOT include any explanations or additional text outside the JSON response.
    """,
    description="Generates professional emails with structured subject and body",
    output_schema=EmailContent,
    output_key="email",
)
