from typing import List
from typing import Any
from dataclasses import dataclass
import json


@dataclass
class AllowedIps:
    ips: List[object]
    protected_branches_only: bool
    primary_branch_only: bool

    @staticmethod
    def from_dict(obj: Any) -> 'AllowedIps':
        _ips = [obj.from_dict(y) for y in obj.get("ips")]
        _protected_branches_only = obj.get("protected_branches_only")
        _primary_branch_only = obj.get("primary_branch_only")
        return AllowedIps(_ips, _protected_branches_only, _primary_branch_only)


@dataclass
class DefaultEndpointSettings:
    autoscaling_limit_min_cu: float
    autoscaling_limit_max_cu: float
    suspend_timeout_seconds: int

    @staticmethod
    def from_dict(obj: Any) -> 'DefaultEndpointSettings':
        _autoscaling_limit_min_cu = float(obj.get("autoscaling_limit_min_cu"))
        _autoscaling_limit_max_cu = float(obj.get("autoscaling_limit_max_cu"))
        _suspend_timeout_seconds = int(obj.get("suspend_timeout_seconds"))
        return DefaultEndpointSettings(_autoscaling_limit_min_cu, _autoscaling_limit_max_cu, _suspend_timeout_seconds)


@dataclass
class Pagination:
    cursor: str

    @staticmethod
    def from_dict(obj: Any) -> 'Pagination':
        _cursor = str(obj.get("cursor"))
        return Pagination(_cursor)


class Settings:
    pass


@dataclass
class Project:
    id: str
    platform_id: str
    region_id: str
    name: str
    provisioner: str
    default_endpoint_settings: DefaultEndpointSettings
    settings: Settings
    pg_version: int
    proxy_host: str
    branch_logical_size_limit: int
    branch_logical_size_limit_bytes: int
    store_passwords: bool
    active_time: int
    cpu_used_sec: int
    creation_source: str
    created_at: str
    updated_at: str
    synthetic_storage_size: int
    quota_reset_at: str
    owner_id: str
    compute_last_active_at: str

    @staticmethod
    def from_dict(obj: Any) -> 'Project':
        _id = str(obj.get("id"))
        _platform_id = str(obj.get("platform_id"))
        _region_id = str(obj.get("region_id"))
        _name = str(obj.get("name"))
        _provisioner = str(obj.get("provisioner"))
        _default_endpoint_settings = DefaultEndpointSettings.from_dict(obj.get("default_endpoint_settings"))
        _settings = Settings.from_dict(obj.get("settings"))
        _pg_version = int(obj.get("pg_version"))
        _proxy_host = str(obj.get("proxy_host"))
        _branch_logical_size_limit = int(obj.get("branch_logical_size_limit"))
        _branch_logical_size_limit_bytes = int(obj.get("branch_logical_size_limit_bytes"))
        _store_passwords = obj.get("store_passwords")
        _active_time = int(obj.get("active_time"))
        _cpu_used_sec = int(obj.get("cpu_used_sec"))
        _creation_source = str(obj.get("creation_source"))
        _created_at = str(obj.get("created_at"))
        _updated_at = str(obj.get("updated_at"))
        _synthetic_storage_size = int(obj.get("synthetic_storage_size"))
        _quota_reset_at = str(obj.get("quota_reset_at"))
        _owner_id = str(obj.get("owner_id"))
        _compute_last_active_at = str(obj.get("compute_last_active_at"))
        return Project(_id, _platform_id, _region_id, _name, _provisioner, _default_endpoint_settings, _settings,
                       _pg_version, _proxy_host, _branch_logical_size_limit, _branch_logical_size_limit_bytes,
                       _store_passwords, _active_time, _cpu_used_sec, _creation_source, _created_at, _updated_at,
                       _synthetic_storage_size, _quota_reset_at, _owner_id, _compute_last_active_at)


@dataclass
class Projects:
    projects: List[Project]
    pagination: Pagination

    @staticmethod
    def from_dict(obj: Any) -> 'Projects':
        _projects = [Project.from_dict(y) for y in obj.get("projects")]
        _pagination = Pagination.from_dict(obj.get("pagination"))
        return Projects(_projects, _pagination)


@dataclass
class Settings:
    allowed_ips: AllowedIps
    enable_logical_replication: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Settings':
        _allowed_ips = AllowedIps.from_dict(obj.get("allowed_ips"))
        _enable_logical_replication = obj.get("enable_logical_replication")
        return Settings(_allowed_ips, _enable_logical_replication)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
