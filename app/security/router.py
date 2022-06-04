from fastapi import APIRouter

router = APIRouter(
    prefix='/security',
    tags=['security']
)

# @TODO:
# - Reset password
# - Verify email
