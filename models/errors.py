from pydantic import BaseModel

class HTTPError(BaseModel):
    detail: str

class ValidationError(BaseModel):
    loc: list
    msg: str
    type: str

class ErrorResponse(BaseModel):
    error: str
    details: list[ValidationError] | None = None

    class Config:
        schema_extra = {
            "example": {
                "error": "Invalid input",
                "details": [
                    {
                        "loc": ["body", "title"],
                        "msg": "Field required",
                        "type": "value_error.missing"
                    }
                ]
            }
        }
