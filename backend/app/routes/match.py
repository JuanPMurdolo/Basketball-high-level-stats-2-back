from fastapi import APIRouter, Depends
from app.services.match import MatchService
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.schemas.match import MatchCreate


router = APIRouter()

@router.get("/")
def get_matches(
    db: Session = Depends(get_db),
    match_service: MatchService = Depends(MatchService)
):
    """Get all matches."""
    return match_service.get_all_matches()

@router.post("/")
def create_match(
    match: MatchCreate,
    db: Session = Depends(get_db),
    match_service: MatchService = Depends(MatchService)
):
    """Create a new match."""
    return match_service.create_match(match)

@router.get("/zone/{zona_id}")
def get_matches_by_zone(
    zona_id: int,
    db: Session = Depends(get_db),
    match_service: MatchService = Depends(MatchService)
):
    """Get matches by zone."""
    """This endpoint retrieves all matches associated with a specific zone."""
    """It takes a zone ID as a parameter and returns the matches."""
    """This is useful for filtering matches based on their geographical or categorical zone."""
    return match_service.get_matches_by_zone(zona_id)

@router.get("/{match_id}")
def get_match_by_id(
    match_id: int,
    db: Session = Depends(get_db),
    match_service: MatchService = Depends(MatchService)
):
    """Get a match by its ID."""
    """This endpoint retrieves a specific match using its unique identifier."""
    """It returns the match details if found, or an error if not."""
    """This is useful for fetching detailed information about a specific match."""
    return match_service.get_match_by_id(match_id)

@router.put("/{match_id}")
def update_match(
    match_id: int,
    match: MatchCreate,
    db: Session = Depends(get_db),
    match_service: MatchService = Depends(MatchService)
):
    """Update a match."""
    """This endpoint allows updating the details of an existing match."""
    """It takes the match ID and the updated match data as parameters."""
    """This is useful for modifying match information after it has been created."""
    return match_service.update_match(match_id, match)

@router.delete("/{match_id}")
def delete_match(
    match_id: int,
    db: Session = Depends(get_db),
    match_service: MatchService = Depends(MatchService)
):
    """Delete a match."""
    """This endpoint allows deleting a match using its unique identifier."""
    """It returns the deleted match details if successful, or an error if not found."""
    """This is useful for removing matches that are no longer relevant or needed."""
    return match_service.delete_match(match_id)

