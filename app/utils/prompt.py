from datetime import datetime

def generate_prompt(sector: str, data: str) -> str:
    date = datetime.now().strftime("%d %B %Y")

    return f"""
You are a financial analyst specializing in Indian markets.

Analyze the {sector} sector in India using the data below.

IMPORTANT:
- Focus on India
- Provide actionable trade opportunities

DATA:
{data}

Return a structured markdown report:

# 📊 {sector.title()} Sector Analysis (India)

**Generated on:** {date}

## Market Overview

## Key Trends

## Trade Opportunities

## Risks

## Future Outlook

---

*Data sourced from recent market news and analysis.*
"""