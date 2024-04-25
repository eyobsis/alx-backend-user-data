#!/usr/bin/env python3
""" Authentication helper class
"""
from bcrypt import hashpw, gensalt, checkpw
from db import DB
import uuid
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from typing import Union


def _hash_password(password: str) -> bytes:
    """ Hash password

    Args:
        password (str): The password to hash

    Returns:
        bytes: The hashed password
    """
    return hashpw(password.encode(), gensalt())


def _generate_uuid() -> str:
    """ Generate a unique ID

    Returns:
        str: A unique ID
    """
    return str(uuid.uuid4())


class Auth:
    """ Auth class
    """

    def __init__(self):
        """ Constructor

        Initializes a new Auth instance with a DB instance.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ User registration

        Args:
            email (str): The email address of the user
            password (str): The password of the user

        Returns:
            User: The newly registered user

        Raises:
            ValueError: If the user already exists
        """
        try:
            users_found = self._db.find_user_by(email=email)
            if users_found:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed_password = _hash_password(password).decode('utf-8')
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """ Login validation

        Args:
            email (str): The email address of the user
            password (str): The password of the user

        Returns:
            bool: Whether the login is valid
        """
        if not email or not password:
            return False
        try:
            users_found = self._db.find_user_by(email=email)
            hashed_password = users_found.hashed_password
            return checkpw(password.encode(),
                           hashed_password.encode('utf-8'))
        except (NoResultFound, InvalidRequestError):
            return False

    def create_session(self, email: str) -> Union[str, None]:
        """ Create a new session for a user

        Args:
            email (str): The email address of the user

        Returns:
            Union[str, None]: The session ID, or None if the user is not found
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except (NoResultFound, ValueError):
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """ Get a user from the session

        Args:
            session_id (str): The session ID

        Returns:
            Union[User, None]: The user, or None if the session ID is invalid
        """
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ Destroy a user session

        Args:
            user_id (int): The ID of the user
        """
        try:
            self._db.update_user(user_id, session_id=None)
        except ValueError:
            pass

    def get_reset_password_token(self, email: str) -> str:
        """ Get reset password token

        Args:
            email (str): The email address of the user

        Returns:
            str: The reset password token

        Raises:
            ValueError: If the user is not found
        """
        try:
            user = self._db.find_user_by(email=email)
            if user.reset_token:
                return user.reset_token
            token = _generate_uuid()
            self._db.update_user(user.id, reset_token=token)
            return token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """ Update user password

        Args:
            reset_token (str): The reset password token
            password (str): The new password

        Raises:
            ValueError: If the reset token is invalid
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password).decode('utf-8')
            self._db.update_user(user.id, hashed_password=hashed_password,
                                 reset_token=None)
        except NoResultFound:
            raise ValueError
