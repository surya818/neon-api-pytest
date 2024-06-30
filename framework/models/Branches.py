from typing import List
from typing import Any
from dataclasses import dataclass
import json


@dataclass
class Branch:
    id: str
    project_id: str
    name: str
    current_state: str
    logical_size: int
    creation_source: str
    primary: bool
    default: bool
    protected: bool
    cpu_used_sec: int
    compute_time_seconds: int
    active_time_seconds: int
    written_data_bytes: int
    data_transfer_bytes: int
    created_at: str
    updated_at: str

    @staticmethod
    def from_dict(obj: Any) -> 'Branch':
        _id = str(obj.get("id"))
        _project_id = str(obj.get("project_id"))
        _name = str(obj.get("name"))
        _current_state = str(obj.get("current_state"))
        _logical_size = int(obj.get("logical_size"))
        _creation_source = str(obj.get("creation_source"))
        _primary = obj.get("primary")
        _default = obj.get("default")
        _protected = obj.get("protected")
        _cpu_used_sec = int(obj.get("cpu_used_sec"))
        _compute_time_seconds = int(obj.get("compute_time_seconds"))
        _active_time_seconds = int(obj.get("active_time_seconds"))
        _written_data_bytes = int(obj.get("written_data_bytes"))
        _data_transfer_bytes = int(obj.get("data_transfer_bytes"))
        _created_at = str(obj.get("created_at"))
        _updated_at = str(obj.get("updated_at"))
        return Branch(_id, _project_id, _name, _current_state, _logical_size, _creation_source, _primary, _default,
                      _protected, _cpu_used_sec, _compute_time_seconds, _active_time_seconds, _written_data_bytes,
                      _data_transfer_bytes, _created_at, _updated_at)


@dataclass
class Branches:
    branches: List[Branch]

    @staticmethod
    def from_dict(obj: Any) -> 'Branches':
        _branches = [Branch.from_dict(y) for y in obj.get("branches")]
        return Branches(_branches)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
