from pydantic import BaseModel

class ErrorResponse(BaseModel):
    error_code: int
    error_mgs: str
    error_detail: str = None
