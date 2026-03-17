from app.services.data_collector import DataCollector
from app.services.ai_analyzer import AIAnalyzer

class AnalysisService:
    def __init__(self):
        self.collector = DataCollector()
        self.analyzer = AIAnalyzer()

    async def run(self, sector: str):
        try:
            data = await self.collector.fetch(sector)
        except Exception as e:
            return f"## Error\nFailed to fetch market data: {str(e)}"

        try:
            analysis = await self.analyzer.analyze(sector, data)
        except Exception as e:
            return f"## Error\nAI analysis failed: {str(e)}"

        return analysis