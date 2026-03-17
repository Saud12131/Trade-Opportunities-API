import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from app.utils.prompt import generate_prompt

load_dotenv()


class AIAnalyzer:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )

        self.deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    async def analyze(self, sector: str, data: str) -> str:
        try:
            # ✅ generate prompt here
            prompt = generate_prompt(sector, data)

            response = self.client.chat.completions.create(
                model=self.deployment,
                messages=[
                    {"role": "system", "content": "You are an expert financial analyst."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )

            return response.choices[0].message.content

        except Exception as e:
            print("AIAnalyzer Error:", str(e))
            raise Exception("Failed to analyze data")