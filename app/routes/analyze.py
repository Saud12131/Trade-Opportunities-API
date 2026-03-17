from fastapi import APIRouter, HTTPException, Query
from app.services.analyze_service import AnalysisService
from app.middleware.session import get_session, add_history, add_request
from app.middleware.auth import validate_api_key
from app.services.rate_limiter import check_rate_limit

router = APIRouter()
service = AnalysisService()


@router.get("/analyze/{sector}")
async def analyze_sector(
    sector: str,
    api_key: str = Query(..., description="Use test123 or demo123"),
):
 try:
    # validate API key
    validate_api_key(api_key)
    
    if not sector.isalpha():
        raise HTTPException(400, "Invalid sector")

    #  session
    session = get_session(api_key)

    #rate limit
    check_rate_limit(api_key)

    #  track request
    add_request(api_key)
    add_history(api_key, sector)

    # main logic
    result = await service.run(sector)
            
    return {"report": result}
 except HTTPException as he:
        # Re-raise HTTPExceptions (like auth errors) as-is
        raise he
 except Exception as e:
        print("AnalyzeSector Error:", str(e))
        raise HTTPException(500, "Internal server error")