from framework.http.HttpClientImpl import HttpClientImpl
from framework.services.BaseService import BaseService
from framework.models.CreateBranchModel import CreateBranchModel
from framework.models.UpdateProjectModel import UpdateProjectModel

import json


class BranchService(BaseService):
    def __init__(self):
        super().__init__()
        self.project_id = None
        self.bearer_token = None

    def set_bearer_token(self, bearer_token):
        self.bearer_token = bearer_token

    def set_project_id(self, project_id):
        self.project_id = project_id

    def get_all_branches(self, project_id):
        cli = HttpClientImpl()
        # Example GET request to the JSONPlaceholder API
        url = self.base_url + f'/api/v2/projects/{project_id}/branches'
        headers = {'Authorization': 'Bearer ' + self.bearer_token}
        get_branches = self.http_client.get(url, headers=headers)
        return get_branches

    def create_branch(self, project_id, payload_object: CreateBranchModel):
        payload = json.dumps(payload_object.serialize_to_json())
        # Example GET request to the JSONPlaceholder API
        url = self.base_url + f'/api/v2/projects/{project_id}/branches'
        headers = {'Authorization': 'Bearer ' + self.bearer_token}
        project = self.http_client.post(url, headers=headers, body=payload)
        return project

    def delete_branch(self, project_id, branch_id):
        # Example GET request to the JSONPlaceholder API
        url = self.base_url + f'/api/v2/projects/{project_id}/branches/{branch_id}'
        headers = {'Authorization': 'Bearer ' + self.bearer_token}
        project = self.http_client.delete(url, headers=headers)
        return project

