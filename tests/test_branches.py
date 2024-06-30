from framework.services.ProjectService import ProjectService
from framework.services.BranchService import BranchService

import pytest
from tests.basetest import BaseTest
from framework.models.UpdateProjectModel import UpdateProjectModel
from framework.models.UpdateProjectModel import ProjectModel as pvModel
from framework.models.Branches import Branches
from framework.models.CreateBranchModel import CreateBranchModel
from framework.models.CreateBranchModel import BranchModel


def create_branch_payload_generate(name, parent_id) -> CreateBranchModel:
    return CreateBranchModel(BranchModel(name, parent_id))


def generate_update_project_payload(name):
    return UpdateProjectModel(pvModel(name))


def verify_branches_response(response: Branches):
    assert response is not None
    assert response.branches[0].id is not None
    assert response.branches[0].name is not None
    assert response.branches[0].project_id is not None


project_service: ProjectService = ProjectService()
branch_service: BranchService = BranchService()


class TestBranches(BaseTest):
    @pytest.fixture(autouse=True)
    def setup(self):
        branch_service.set_bearer_token(self.access_token)
        project_service.set_bearer_token(self.access_token)
        self.project_id = project_service.get_all_projects().json()['projects'][0]['id']
        return branch_service

    """
    Happy Path test, calls GET /project and verifies some properties in the response
    """

    def test_get_all_branches(self):
        all_branches = branch_service.get_all_branches(self.project_id).json()
        branches = Branches.from_dict(all_branches)
        self.parent_branch_id = branches.branches[0].id
        verify_branches_response(branches)

    def test_create_branch(self):
        """
        Create a branch called develop
        Verify the successful creation and that the new branch is not the primary branch
        """
        # Fetch parent branch id
        all_branches = branch_service.get_all_branches(self.project_id).json()
        assert len(all_branches['branches']) == 1
        parent_id = all_branches['branches'][0]['id']
        branch_name = 'develop'
        # Create Branch Payload generation
        payload = create_branch_payload_generate(branch_name, parent_id)
        # Create branch API call
        create_branch_response = branch_service.create_branch(self.project_id, payload)
        assert create_branch_response.status_code == 201
        all_branches = branch_service.get_all_branches(self.project_id).json()
        assert len(all_branches['branches']) == 2
        for branch in all_branches['branches']:
            if branch['name'] == 'develop':
                assert branch['primary'] is False
            if branch['name'] == 'main':
                assert branch['primary'] is True

    @pytest.mark.depends(on=['test_create_branch'])
    def test_delete_branch(self):
        """
        Delete the develop branch created in previous step
        """
        all_branches = branch_service.get_all_branches(self.project_id).json()
        for branch in all_branches['branches']:
            if branch['name'] == 'develop':
                self.branch_id = branch['id']
        # Fetch parent branch id
        delete_response = branch_service.delete_branch(self.project_id, self.branch_id)
        assert delete_response.status_code == 200
