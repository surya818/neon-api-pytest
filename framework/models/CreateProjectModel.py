import json
from typing import Any
from dataclasses import dataclass


@dataclass
class ProjectModel:
    name: str
    pg_version: int

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _name = str(obj.get("name"))
        _pg_version = int(obj.get("pg_version"))
        return ProjectModel(_name, _pg_version)

    def to_dict(self):
        return {
            'name': self.name,
            'pg_version': self.pg_version
        }


@dataclass
class CreateProjectModel:
    project: ProjectModel

    def to_dict(self):
        ob = self.project.to_dict()
        return {'project': ob}

    def serialize_to_json(custom_object):
        dictionary = custom_object.to_dict()
        return dictionary
