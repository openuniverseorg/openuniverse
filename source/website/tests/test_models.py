from django.test import TestCase
from website.models import Project
from website.models import ProjectStatistics
from website.models import ProjectFeatures
from website.models import TimeSeries
from django.utils import timezone

class ProjectTest(TestCase):
    def create_project(self):
        return Project.objects.create(name="Lorem Ipsum", 
                                      owner="Lorem Ipsum", 
                                      owner_type="Lorem Ipsum", 
                                      created_at=timezone.now(),
                                      updated_at=timezone.now(),
                                      application_domain="Lorem Ipsum",
                                      software_license="Lorem Ipsum",
                                      age=1,
                                      main_language="Lorem Ipsum",
                                      github_url="Lorem Ipsum")

    def test_project_creation(self):
        project = self.create_project()
        self.assertTrue(isinstance(project, Project))
        self.assertEqual(project.__unicode__(), project.name)

class ProjectStatisticsTest(TestCase):
    def create_statistics(self, project):
        return ProjectStatistics.objects.create(project=project,
                                                pulls_merged_total=1, 
                                                newcomers_total=1, 
                                                open_issues_total=1,
                                                used_languages_total=1,
                                                forks_total=1,
                                                stars_total=1,
                                                commits_total=1,
                                                contributors_total=1,
                                                core_members_total=1)

    def test_statistics_creation(self):
        project = ProjectTest().create_project()
        statistics = self.create_statistics(project)
        self.assertTrue(isinstance(statistics, ProjectStatistics))
        self.assertEqual(statistics.__unicode__(), project)

class ProjectFeaturesTest(TestCase):
    def create_features(self, project):
        return ProjectFeatures.objects.create(project=project,
                                              has_contributing=True, 
                                              has_readme=False)

    def test_features_creation(self):
        project = ProjectTest().create_project()
        features = self.create_features(project)
        self.assertTrue(isinstance(features, ProjectFeatures))
        self.assertEqual(features.__unicode__(), project)

class TimeSeriesTest(TestCase):
    def create_time_series(self, project):
        return TimeSeries.objects.create(project=project,
                                         data_type="Lorem Ipsum", 
                                         count=1,
                                         date=timezone.now())

    def test_features_creation(self):
        project = ProjectTest().create_project()
        time_series = self.create_time_series(project)
        self.assertTrue(isinstance(time_series, TimeSeries))
        self.assertEqual(time_series.__unicode__(), project)
