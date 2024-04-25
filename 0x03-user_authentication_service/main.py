#!/usr/bin/env python3
"""
Main file for testing web server for the corresponding end-points.
"""
import requests


def register_user(email: str, password: str) -> None:
    """
    Test for registering a user with the given email and password.

    Args:
        email (str): The email of the user.
        password (str): The password of the user.

    Returns:
        None
    """
    r = requests.post('(link unavailable)',
                      data={'email': email, 'password': password})
    if r.status_code == 200:
        assert (r.json() == {"email": email, "message": "user created"})
    else:
        assert(r.status_code == 400)
        assert (r.json() == {"message": "email already registered"})


def log_in_wrong_password(email: str, password: str) -> None:
    """
    Test for logging in with the given wrong credentials.

    Args:
        email (str): The email of the user.
        password (str): The password of the user.

    Returns:
        None
    """
    r = requests.post('(link unavailable)',
                      data={'email': email, 'password': password})
    assert (r.status_code == 401)


def log_in(email: str, password: str) -> str:
    """
    Test for logging in with the given correct email and password.

    Args:
        email (str): The email of the user.
        password (str): The password of the user.

    Returns:
        str: The session_id of the user.
    """
    r = requests.post('(link unavailable)',
                      data={'email': email, 'password': password})
    assert (r.status_code == 200)
    assert(r.json() == {"email": email, "message": "logged in"})
    return r.cookies['session_id']


def profile_unlogged() -> None:
    """
    Test for profile without being logged in with session_id.

    Returns:
        None
    """
    r = requests.get('(link unavailable)')
    assert(r.status_code == 403)


def profile_logged(session_id: str) -> None:
    """
    Test for profile with being logged in with session_id.

    Args:
        session_id (str): The session_id of the user.

    Returns:
        None
    """
    cookies = {'session_id': session_id}
    r = requests.get('(link unavailable)',
                     cookies=cookies)
    assert(r.status_code == 200)


def log_out(session_id: str) -> None:
    """
    Test for logging out with the given session_id.

    Args:
        session_id (str): The session_id of the user.

    Returns:
        None
    """
    cookies = {'session_id': session_id}
    r = requests.delete('(link unavailable)',
                        cookies=cookies)
    if r.status_code == 302:
        assert(r.url == '(link unavailable)')
    else:
        assert(r.status_code == 200)


def reset_password_token(email: str) -> str:
    """
    Test for reset password token with the given email.

    Args:
        email (str): The email of the user.

    Returns:
        str: The reset_token of the user.
    """
    r = requests.post('(link unavailable)',
                      data={'email': email})
    if r.status_code == 200:
        return r.json()['reset_token']
    assert(r.status_code == 401)


def update_password(email: str, reset_token: str,
                    new_password: str) -> None:
    """
    Test for updating password with the given email,
    reset_token and new_password.

    Args:
        email (str): The email of the user.
        reset_token (str): The reset_token of the user.
        new_password (str): The new password of the user.

    Returns:
        None
    """
    data = {'email': email, 'reset_token': reset_token,
            'new_password': new_password}
    r = requests.put('(link unavailable)',
                     data=data)
    if r.status_code == 200:
        assert(r.json() == {"email": email, "message": "Password updated"})
    else:
        assert(r.status_code == 403)


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3
