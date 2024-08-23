from pydantic import BaseModel
from typing import List, Optional

class EntryCondition(BaseModel):
    entry_price: Optional[float]  # 지정가 거래 시 진입 가격
    collateral: float  # 회차별 증거금
    pnl_target: float  # 익절률
    gap: float  # 회차 간 간격 (%)

class BotSettings(BaseModel):
    symbol: str  # 거래할 코인 페어 (예: 'BTCUSDT')
    leverage: int  # 레버리지 (1 ~ 125배)
    margin_type: str  # 'CROSS' or 'ISOLATED' (교차/격리)
    entry_price_type: str  # 'MARKET' or 'LIMIT' (시장가/지정가)
    order_type: str  # 'LONG' or 'SHORT'
    conditions: List[EntryCondition]  # 각 거래 조건
    repeat_execution: bool  # 반복 실행 여부
