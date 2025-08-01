from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.user import User
from app.models.user_team import UserTeam
from app.models.team import Team
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id: int) -> Optional[User]:
        """Get user by ID."""
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email."""
        return self.db.query(User).filter(User.email == email).first()

    def get_user_by_username(self, username: str) -> Optional[User]:
        """Get user by username."""
        return self.db.query(User).filter(User.username == username).first()

    def get_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        """Get all users with pagination."""
        return self.db.query(User).offset(skip).limit(limit).all()

    def create_user(self, user: UserCreate) -> User:
        """Create a new user."""
        hashed_password = get_password_hash(user.password)
        db_user = User(
            email=user.email,
            username=user.username,
            hashed_password=hashed_password,
            full_name=user.full_name,
            is_active=user.is_active
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update_user(self, user_id: int, user_update: UserUpdate) -> Optional[User]:
        """Update user."""
        user = self.get_user(user_id)
        if not user:
            return None

        update_data = user_update.dict(exclude_unset=True)
        if "password" in update_data:
            update_data["hashed_password"] = get_password_hash(update_data.pop("password"))

        for field, value in update_data.items():
            setattr(user, field, value)

        self.db.commit()
        self.db.refresh(user)
        return user

    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        """Authenticate user with username and password."""
        user = self.get_user_by_username(username)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def assign_teams_to_user(self, user_id: int, team_ids: List[int]) -> bool:
        """Assign teams to a user."""
        user = self.get_user(user_id)
        if not user:
            return False

        # Remove existing assignments
        self.db.query(UserTeam).filter(UserTeam.user_id == user_id).delete()

        # Add new assignments
        for team_id in team_ids:
            user_team = UserTeam(user_id=user_id, team_id=team_id)
            self.db.add(user_team)

        self.db.commit()
        return True

    def get_user_teams(self, user_id: int) -> List[Team]:
        """Get teams assigned to a user."""
        user_teams = self.db.query(UserTeam).filter(UserTeam.user_id == user_id).all()
        team_ids = [ut.team_id for ut in user_teams]
        return self.db.query(Team).filter(Team.id.in_(team_ids)).all()
