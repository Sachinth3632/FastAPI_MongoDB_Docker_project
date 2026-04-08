from pydantic import BaseModel
from typing import Optional
class Inspection(BaseModel):
      inspector_name: str
      position: str
      status: str
      notes: Optional[str] = None
