from dataclasses import dataclass

@dataclass
class AppItemResponse:
    item_id:int
    name: str
    icon_url: str
    direct_url: str
    description: str