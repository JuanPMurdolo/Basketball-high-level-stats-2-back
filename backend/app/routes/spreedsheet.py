from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from app.core.spreedsheet_processor import process_csv
from app.services.stats import StatsService
from app.schemas.stats import StatCreate, StatOut
from app.core.db import get_db
from sqlalchemy.orm import Session
import tempfile
import os

router = APIRouter()

@router.post("/upload", response_model=list[StatOut])
async def upload_spreadsheet(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):    try:
        suffix = os.path.splitext(file.filename)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            content = await file.read()
            tmp.write(content)
            tmp_path = tmp.name

        stats_data = process_csv(tmp_path)
        os.remove(tmp_path)

        service = StatsService(db)
        created_stats = []
        for team in stats_data["teams"]:
            for player in team["players"]:
                stat_create = StatCreate(**player)
                created_stat = service.create_stat(stat_create)
                created_stats.append(created_stat)
        return created_stats

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error procesando archivo: {str(e)}")