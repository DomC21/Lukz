from fastapi import FastAPI, Query, HTTPException, Request, Depends, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.security import APIKeyHeader
from typing import Optional, List, Dict
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
import re
from app.security import verify_api_key, validate_ticker, sanitize_input

# Initialize rate limiter
limiter = Limiter(key_func=get_remote_address)
from app.services.unusual_whales import get_congress_trades
from app.services.greek_flow import get_greek_flow, get_greek_descriptions
from app.services.market_tide import get_market_tide
from app.services.earnings import generate_mock_earnings_data
from app.services.insider_trading import generate_mock_insider_data
from app.services.premium_flow import generate_mock_premium_flow, get_sector_descriptions
from app.services.feedback import save_feedback
from app.services.insights import (
    generate_congress_trades_insight,
    generate_greek_flow_insight,
    generate_earnings_insight,
    generate_insider_trading_insight,
    generate_premium_flow_insight
)

app = FastAPI(title="Lukz Financial API")

# Add rate limiting middleware
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

# Add trusted host middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"]  # Configure based on deployment environment
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure based on deployment environment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-RateLimit-Limit", "X-RateLimit-Remaining", "X-RateLimit-Reset"]
)

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.get("/api/congress/trades")
@limiter.limit("60/minute")
async def congress_trades(
    request: Request,
    api_key: str = Depends(verify_api_key),
    ticker: Optional[str] = Query(None, description="Filter by stock ticker"),
    congress_member: Optional[str] = Query(None, description="Filter by congress member name"),
    start_date: Optional[str] = Query(None, description="Start date (YYYY-MM-DD)"),
    end_date: Optional[str] = Query(None, description="End date (YYYY-MM-DD)")
) -> Dict:
    """Get recent congress trades with optional filtering"""
    try:
        return await get_congress_trades(ticker, congress_member, start_date, end_date)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/greek-flow/data")
@limiter.limit("60/minute")
async def greek_flow_data(
    request: Request,
    api_key: str = Depends(verify_api_key),
    ticker: str = Query(..., description="Stock ticker (required)"),
    start_date: Optional[str] = Query(None, description="Start date (YYYY-MM-DD)"),
    end_date: Optional[str] = Query(None, description="End date (YYYY-MM-DD)")
) -> Dict:
    """Get Greek flow data with optional filtering"""
    # Validate ticker format
    if not validate_ticker(ticker):
        raise HTTPException(status_code=400, detail="Invalid ticker format")
    try:
        return await get_greek_flow(ticker, start_date, end_date)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/greek-flow/descriptions")
async def greek_descriptions() -> Dict[str, str]:
    """Get descriptions of Greek metrics for tooltips"""
    return get_greek_descriptions()

@app.get("/api/earnings/data")
@limiter.limit("60/minute")
async def earnings_data(
    request: Request,
    api_key: str = Depends(verify_api_key),
    sector: Optional[str] = Query(None, description="Filter by sector"),
    surprise_type: Optional[str] = Query(None, description="Filter by surprise type (positive/negative)"),
    start_date: Optional[str] = Query(None, description="Start date (YYYY-MM-DD)"),
    end_date: Optional[str] = Query(None, description="End date (YYYY-MM-DD)")
) -> Dict:
    """Get earnings data with optional filtering"""
    # Sanitize inputs
    if sector:
        sector = sanitize_input(sector)
    if surprise_type:
        surprise_type = sanitize_input(surprise_type)
    try:
        data = generate_mock_earnings_data(sector, surprise_type, start_date, end_date)
        return {
            "data": data,
            "insight": generate_earnings_insight(data)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/insider-trading/data")
@limiter.limit("60/minute")
async def insider_trading_data(
    request: Request,
    api_key: str = Depends(verify_api_key),
    insider_role: Optional[str] = Query(None, description="Filter by insider role (e.g., CEO, CFO)"),
    trade_type: Optional[str] = Query(None, description="Filter by trade type (buy/sell)"),
    start_date: Optional[str] = Query(None, description="Start date (YYYY-MM-DD)"),
    end_date: Optional[str] = Query(None, description="End date (YYYY-MM-DD)")
) -> Dict:
    """Get insider trading data with optional filtering"""
    # Sanitize inputs
    if insider_role:
        insider_role = sanitize_input(insider_role)
    if trade_type:
        trade_type = sanitize_input(trade_type)
    try:
        data = generate_mock_insider_data(insider_role, trade_type, start_date, end_date)
        return {
            "data": data,
            "insight": generate_insider_trading_insight(data)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/premium-flow/data")
@limiter.limit("60/minute")
async def premium_flow_data(
    request: Request,
    api_key: str = Depends(verify_api_key),
    option_type: Optional[str] = Query(None, description="Filter by option type (call/put)"),
    sector: Optional[str] = Query(None, description="Filter by sector"),
    start_date: Optional[str] = Query(None, description="Start date (YYYY-MM-DD)"),
    end_date: Optional[str] = Query(None, description="End date (YYYY-MM-DD)"),
    lookback_days: int = Query(30, description="Number of days to look back for historical comparison"),
    is_intraday: bool = Query(False, description="Use intraday granularity")
) -> Dict:
    """Get premium flow data with optional filtering and historical context"""
    # Sanitize inputs
    if option_type:
        option_type = sanitize_input(option_type)
    if sector:
        sector = sanitize_input(sector)
    try:
        data, historical_stats = generate_mock_premium_flow(
            option_type, sector, start_date, end_date, lookback_days, is_intraday
        )
        return {
            "data": data,
            "historical_stats": historical_stats,
            "insight": generate_premium_flow_insight(data, historical_stats, is_intraday)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/market-tide/data")
@limiter.limit("60/minute")
async def market_tide_data(
    request: Request,
    api_key: str = Depends(verify_api_key),
    date: Optional[str] = Query(None, description="Target date (YYYY-MM-DD)"),
    interval_5m: bool = Query(False, description="Use 5-minute intervals instead of 1-minute"),
    lookback_days: int = Query(30, description="Number of days to look back for historical comparison"),
    granularity: str = Query("minute", description="Data granularity: 'minute' or 'daily'")
) -> Dict:
    """Get market-wide options flow data with historical context"""
    # Validate granularity
    if granularity not in ["minute", "daily"]:
        raise HTTPException(status_code=400, detail="Invalid granularity value")
    try:
        return await get_market_tide(date, interval_5m, lookback_days, granularity)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/feedback")
@limiter.limit("10/minute")
async def submit_feedback(
    request: Request,
    api_key: str = Depends(verify_api_key),
    feedback: Dict = Body(...)
) -> Dict:
    """Submit user feedback"""
    try:
        # Sanitize feedback message
        feedback["message"] = sanitize_input(feedback.get("message", ""))
        
        # Save feedback
        if save_feedback(feedback):
            return {"status": "success"}
        else:
            raise HTTPException(status_code=500, detail="Failed to save feedback")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/premium-flow/sectors")
async def sector_descriptions() -> Dict[str, str]:
    """Get descriptions of sectors for tooltips"""
    return get_sector_descriptions()
