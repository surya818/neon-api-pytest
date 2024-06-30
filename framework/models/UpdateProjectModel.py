import json
from typing import Any
from dataclasses import dataclass


@dataclass
class ProjectModel:
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _name = str(obj.get("name"))
        return ProjectModel(_name)

    def to_dict(self):
        return {
            'name': self.name,
        }


@dataclass
class UpdateProjectModel:
    project: ProjectModel

    def to_dict(self):
        ob = self.project.to_dict()
        return {'project': ob}

    def serialize_to_json(custom_object):
        dictionary = custom_object.to_dict()
        return dictionary
