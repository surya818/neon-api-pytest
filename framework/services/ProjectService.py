from framework.http.HttpClientImpl import HttpClientImpl
from framework.services.BaseService import BaseService
from framework.models.CreateProjectModel import CreateProjectModel
from framework.models.UpdateProjectModel import UpdateProjectModel

import json


class ProjectService(BaseService):
    def __init__(self):
        super().__init__()
        self.project_id = None
        self.bearer_token = None

    def set_bearer_token(self, bearer_token):
        self.bearer_token = bearer_token

    def set_project_id(self, project_id):
        self.project_id = project_id

    def get_all_projects(self):
        cli = HttpClientImpl()
        # Example GET request to the JSONPlaceholder API
        url = self.base_url + '/api/v2/projects'
        headers = {'Authorization': 'Bearer ' + self.bearer_token}
        get_projects = self.http_client.get(url, headers=headers)
        return get_projects

    def create_project(self, payload_object: CreateProjectModel):
        payload = json.dumps(payload_object.serialize_to_json())
        # Example GET request to the JSONPlaceholder API
        url = self.base_url + '/api/v2/projects'
        headers = {'Authorization': 'Bearer ' + self.bearer_token}
        project = self.http_client.post(url, headers=headers, body=payload)
        return project

    def update_project(self, payload_object: UpdateProjectModel):
        print(type(payload_object))
        payload = json.dumps(payload_object.serialize_to_json())

        # Example GET request to the JSONPlaceholder API
        url = self.base_url + '/api/v2/projects'+'/'+self.project_id
        headers = {'Authorization': 'Bearer ' + self.bearer_token}
        project = self.http_client.patch(url, headers=headers, body=payload)
        return project
