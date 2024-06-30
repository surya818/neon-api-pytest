import json
from typing import Any
from dataclasses import dataclass


@dataclass
class BranchModel:
    name: str
    parent_id: str

    @staticmethod
    def from_dict(obj: Any) -> 'BranchModel':
        _name = str(obj.get("name"))
        _parent_id = str(obj.get("parent_id"))
        return BranchModel(_name, _parent_id)

    def to_dict(self):
        return {
            'name': self.name,
            'pg_version': self.parent_id
        }


@dataclass
class CreateBranchModel:
    branch: BranchModel

    def to_dict(self):
        ob = self.branch.to_dict()
        return {'branch': ob}

    def serialize_to_json(custom_object):
        dictionary = custom_object.to_dict()
        return dictionary
