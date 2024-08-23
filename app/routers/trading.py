### 거래 관련 라우팅 및 엔드포인트 정의 ###
from fastapi import APIRouter, Depends, HTTPException
from ..models.settings import BotSettings
from ..services.trading_service import start_trading_bot

router = APIRouter(prefix="/trading", tags=["trading"])

@router.post("/start_bot")
async def start_bot(settings: BotSettings):
    try:
        result = start_trading_bot(settings)
        return {"message": "Bot started successfully", "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
