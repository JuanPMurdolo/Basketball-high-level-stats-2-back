import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os, sys

# Add the root project directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.stats import StatsModel
# Setup a test database or mock session
engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
session = Session()

@pytest.fixture
def stats_instance():
    # Assuming threePointersMade is defined and works similarly to twoPointersMade
    stats = StatsModel(
        twoPointersMade=5,
        threePointersMade=3,
        # Set other necessary fields to valid values
    )
    session.add(stats)
    session.commit()
    return stats

def test_fieldGoalsMade(stats_instance):
    # Verify that fieldGoalsMade is the sum of twoPointersMade and threePointersMade
    assert stats_instance.fieldGoalsMade == 8
