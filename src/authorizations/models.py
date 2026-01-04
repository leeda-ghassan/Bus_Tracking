from enum import Enum
# from pydantic import BaseModel, Field
# from uuid import UUID
# from datetime import datetime

class StatusEnum(str, Enum):
    active = 'active'
    disabled = 'disabled'
    in_progress = 'in_progress'
    arrived = 'arrived'
    under_maintenance = 'under_maintenance'
    delayed = 'delayed'