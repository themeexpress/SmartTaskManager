from app.models.user import User
from app.models.task import Task
from app.models.project import Project
from fastapi import HTTPException, status


# =========================
# TASK PERMISSIONS
# =========================

def can_update_task(user: User, task: Task) -> bool:
    """
    Creator 
    Assignee 
    Admin 
    """
    return (
        user.role == "admin"
        or task.created_by == user.id
        or task.assignee_id == user.id
    )


def can_delete_task(user: User, task: Task) -> bool:
    """
    Only Creator 
    or Admin 
    """
    return (
        user.role == "admin"
        or task.created_by == user.id
    )


# =========================
# PROJECT PERMISSIONS
# =========================

def can_update_project(user: User, project: Project) -> bool:
    """
    Owner 
    or Admin 
    """
    return (
        user.role == "admin"
        or project.owner_id == user.id
    )


def can_delete_project(user: User, project: Project) -> bool:
    """
    Only Owner 
    or Admin 
    """
    return (
        user.role == "admin"
        or project.owner_id == user.id
    )


# =========================
# USER PERMISSIONS
# =========================

def can_update_user(current_user: User, target_user: User) -> bool:
    """
    User can update ONLY own profile
    Admin can update anyone
    """
    return (
        current_user.role == "admin"
        or current_user.id == target_user.id
    )


def can_delete_user(current_user: User, target_user: User) -> bool:
    """
    Only Admin can delete users
    """
    return current_user.role == "admin"


# =========================
# GUARD HELPERS (OPTIONAL)
# =========================

def verify_permission(condition: bool, message: str = "Permission denied"):
    if not condition:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=message,
        )
