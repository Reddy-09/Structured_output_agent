# Structured_output_agent

📧 Structured Outputs: Email Generator Agent (```email_generator```)
Project Overview
Welcome to the Structured Outputs Example! This project demonstrates a critical capability for building production-ready AI applications: ensuring the agent's output is consistently formatted and validated.

Our main agent, ```email_generator```, uses the Agent Development Kit (ADK) and Pydantic models to guarantee that every email it drafts is returned as a clean, predictable JSON object, ready for integration into a mail service or another agent.

💡 What are Structured Outputs?
Structured Outputs in ADK allow you to define a fixed, schema-bound format for agent inputs and outputs using Pydantic models. This offers several key advantages over relying on free-form text:

Controlled Output Format: The ```output_schema``` parameter forces the LLM to produce a response that conforms to a specific JSON structure.

Data Validation: Pydantic automatically validates that all required fields are present and correctly typed.

Improved Downstream Processing: Standardized JSON is easy to parse, store, or pass to other systems (like a backend API or another agent in a pipeline).


📩 The Email Generator Example
In this example, we've created an agent that produces structured email content based on a user prompt.

Output Schema Definition
The core of this project is the ```EmailContent``` Pydantic model, which defines the exact required structure:

Python:
```
class EmailContent(BaseModel):
    """Schema for email content with subject and body."""
    
    subject: str = Field(
        description="The subject line of the email. Should be concise and descriptive."
    )
    body: str = Field(
        description="The main content of the email. Should be well-formatted with proper greeting, paragraphs, and signature."
    )
```

How It Works
The user requests a new email draft (e.g., "Draft an email to a client...").

The ```email_generator``` agent processes the request.

The ```output_schema``` compels the agent to generate its response as a JSON object matching the schema.

ADK validates the resulting JSON before returning it, and the structured output is stored in the session state under the specified ```output_key```.


🚧 Important Limitations
When implementing structured outputs in ADK, be aware of this major constraint:

No Tool Usage: Agents configured with an ```output_schema``` cannot use tools (like ```Google Search``` or custom functions) during their execution.

Solution: To combine tool usage with structured output, you must use a Sequential Agent pipeline where one agent calls the tool and the second agent formats the output into the required schema.


🚀 Getting Started
Project Structure

```
4-structured-outputs/
│
├── email_agent/                   # Email Generator Agent package
│   └── agent.py                   # Agent definition with output schema
│
└── README.md                      # This documentation
```

Setup
1.Activate Virtual Environment:

Bash:
```
# Ensure your environment is active
# Example: .venv\Scripts\Activate
```

2.Install Dependencies: Make sure ```pydantic``` and ```google-adk``` are installed (likely in your main ```requirements.txt```).
Bash:
```
pip install google-adk pydantic
```
3.API Key Configuration: Create a ```.env``` file in the appropriate directory and add your Google API key:

```
GOOGLE_API_KEY=your_api_key_here
```

Running the Example
1.Navigate to the parent directory:
```
Bash

cd 4-structured-outputs
```
2.Launch the Interactive Web UI:
```
Bash

adk web
```

3.Select ```"email_generator"``` from the dropdown menu in the web UI.

Example Interactions

Try these example prompts:

```Write a professional email to my team about the upcoming project deadline that has been extended by two weeks.```

```Draft an email to a client explaining that we need additional information before we can proceed with their order.```

```Create an email to schedule a meeting with the marketing department to discuss the new product launch strategy.```
