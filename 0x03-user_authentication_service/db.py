#!/usr/bin/env python3
"""
DB module for database operations
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:
    """
    DB class for database operations
    """

    def __init__(self) -> None:
        """
        Initialize a new DB instance

        Creates a new database engine and session,
        and sets up the database schema.
        """
        self._engine = create_engine("sqlite:///a.db",
                                     connect_args={"check_same_thread": False})
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Memoized session object

        Returns a new session if one doesn't exist,
        or the existing one if it does.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user to the database

        Args:
            email (str): The email address of the user
            hashed_password (str): The hashed password of the user

        Returns:
            User: The newly created user
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Find a user by the given criteria

        Args:
            **kwargs: The criteria to search for

        Returns:
            User: The found user

        Raises:
            NoResultFound: If no user is found
        """
        user = self._session.query(User).filter_by(**kwargs).first()
        if not user:
            raise NoResultFound("No user found")
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Update the given user

        Args:
            user_id (int): The id of the user to update
            **kwargs: The fields to update

        Returns:
            None

        Raises:
            ValueError: If the user is not found or the update fails
        """
        try:
            user = self.find_user_by(id=user_id)
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
                else:
                    raise InvalidRequestError
            self._session.commit()
        except (NoResultFound, InvalidRequestError, ValueError):
            raise ValueError
