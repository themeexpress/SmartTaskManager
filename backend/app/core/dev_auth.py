# app/core/dev_auth.py
from fastapi import Depends
from app.models.user import User

def get_current_user_stub():
    class U:
        id = 1
    return U()
