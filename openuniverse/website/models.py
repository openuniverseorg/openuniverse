from mongoengine import *
from openuniverse.settings import MONGO_DATABASE

connect(MONGO_DATABASE)

# Create your models here.

class Projects(Document):
    name = StringField()
    pull_merged_total = StringField()
    star_total = StringField()
    url = StringField()
    newcomer_total = StringField()
    has_contributing = StringField()
    commit_total = StringField()
    main_language = StringField()
    owner_type = StringField()
    used_languages_total = StringField()
    fork_total = StringField()
    open_issues_total = StringField()
    age = StringField()
    has_readme = StringField()
    domain = StringField()
    license = StringField()
    