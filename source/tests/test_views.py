# Tutorial: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing

'''
from django.test import TestCase
from django.urls import reverse

from website.models import Projects

class ProjectsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_projects = 15

        for project_id in range(number_of_projects):
            Projects.objects.create(
                name='Project {project_id}',
                owner='Owner {project_id}',
                owner_type='Organization {project_id}',
                updated_at='2010-10-10T10:10:10Z',
                created_at='2010-10-10T10:10:10Z',
                domain='Documentation',
                license='GPL 3.0',
                age=10,
                main_language='Python',
                github_url='https://github.com/openuniverseorg/openuniverse',
                statistics={},
                time_series={},
                features={}
            )
           
    def test_find_view_url_exists_at_desired_location(self):
        response = self.client.get('/find/?')
        self.assertEqual(response.status_code, 200)
'''