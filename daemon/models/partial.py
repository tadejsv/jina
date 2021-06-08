from typing import Dict, Union

from jina import Flow
from jina.peapods import Pea, Pod

from .base import StoreItem, StoreStatus


class PartialStoreItem(StoreItem):
    arguments: Dict


class PartialFlowItem(PartialStoreItem):
    yaml_source: str


class PartialStoreStatus(StoreStatus):
    items: StoreItem = StoreItem()

    def __len__(self):
        return 1