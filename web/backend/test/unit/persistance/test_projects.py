from unittest.mock import MagicMock, patch
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model.projects import Base, Project, ProjectORM
from persistance.projects import get_one
import pytest

engine = create_engine("sqlite:///./test.db")
Session = sessionmaker(bind=engine)


GENERIC_COUNT = 5


def test_get_one(mocker):
    """Test get_one function"""
    mock_session = MagicMock(spec=Session)
    mock_query = MagicMock()
    mock_session.query.return_value = mock_query
    mock_query.count.return_value = GENERIC_COUNT

    with patch("sqlalchemy.orm.sessionmaker", return_value=mock_session):
        assert get_one() == GENERIC_COUNT
