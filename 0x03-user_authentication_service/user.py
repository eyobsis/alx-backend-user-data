#!/usr/bin/env python3
"""Defines the User model for the application.

This module creates a User class that represents a user in the database.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


# Create the base class for the User model
Base = declarative_base()


class User(Base):
    """Represents a user in the database.

    This class defines the columns for the users table in the database.
    """
    __tablename__ = 'users'

    # Define the columns for the users table
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
