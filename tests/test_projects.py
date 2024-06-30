from framework.services.ProjectService import ProjectService
import pytest
from tests.basetest import BaseTest
from framework.models.CreateProjectModel import CreateProjectModel
from framework.models.CreateProjectModel import ProjectModel
from framework.models.UpdateProjectModel import UpdateProjectModel
from framework.models.UpdateProjectModel import ProjectModel as pvModel
from framework.models.Projects import Projects


def create_project_payload_generate(name, postgres_version) -> CreateProjectModel:
    return CreateProjectModel(ProjectModel(name, postgres_version))


def generate_update_project_payload(name):
    return UpdateProjectModel(pvModel(name))


def verify_projects_response(response: Projects):
    assert response is not None
    assert response.projects[0].id is not None
    assert response.projects[0].name is not None
    assert response.projects[0].pg_version == 16


project_service: ProjectService = ProjectService()


class TestProjects(BaseTest):
    @pytest.fixture(autouse=True)
    def setup(self):
        project_service.set_bearer_token(self.access_token)
        return project_service

    """
    Happy Path test, calls GET /project and verifies some properties in the response
    """

    def test_get_all_projects(self):
        all_projects = project_service.get_all_projects().json()
        projects = Projects.from_dict(all_projects)
        verify_projects_response(projects)

    def test_create_project_with_existing_name_expect_error(self):
        all_projects = project_service.get_all_projects().json()
        name = all_projects['projects'][0]['name']
        payload = create_project_payload_generate(name, 16)
        create_project_response = project_service.create_project(payload)
        assert create_project_response.status_code == 422

    def test_update_project(self):
        all_projects = project_service.get_all_projects().json()
        name = all_projects['projects'][0]['name']
        updated_name = name + "-updated"
        project_id = all_projects['projects'][0]['id']

        # Patch and update project with updated name
        patch_payload = generate_update_project_payload(updated_name)
        project_service.set_project_id(project_id)
        update_project_response = project_service.update_project(patch_payload)
        assert update_project_response.status_code == 200

        # Assert the update is successful
        all_projects = project_service.get_all_projects().json()
        name_new = all_projects['projects'][0]['name']
        assert name_new == updated_name

        # revert the name
        patch_payload = generate_update_project_payload(name)
        project_service.set_project_id(project_id)
        update_project_response = project_service.update_project(patch_payload)
        assert update_project_response.status_code == 200
