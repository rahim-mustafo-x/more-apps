from pydantic import BaseModel, Field


class AppItemResponse(BaseModel):
    item_id: int = Field(alias="itemId")
    name: str
    icon_url: str = Field(alias="iconUrl")
    direct_url: str = Field(alias="directUrl")
    description: str