from ddgs import DDGS

class DataCollector:
    async def fetch(self, sector: str) -> str:
        try:
            query = f"{sector} sector India market news trends"
            result_text = []
            with DDGS() as ddgs:
                result = ddgs.text(query, max_results=5)
                for item in result:
                    result_text.append(item['title'] + " " + item['body'])
                return "\n".join(result_text)
        except Exception as e:
            print(" DataCollector Error:", str(e))
            raise Exception("Failed to fetch market data")