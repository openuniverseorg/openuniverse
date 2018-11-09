from django.test import TestCase
from .models import Project

class ProjectModelTest(TestCase):
    def test_name_representation(self):
        project = Project(name="atom")
        self.assertEqual(str(project), project.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Project._meta.verbose_name_plural), "Projects")

class PageTest(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

