from mongoengine import connect, Document, StringField, DictField, IntField, BooleanField
from openuniverse.settings import MONGO_DATABASE

connect(MONGO_DATABASE)

class Projects(Document):
    # String Fields
    name = StringField()
    owner = StringField()
    url = StringField()
    main_language = StringField()
    owner_type = StringField()
    domain = StringField()
    license = StringField()
    cluster = StringField()
    
    # Boolean Fields
    has_readme = BooleanField()
    has_contributing = BooleanField()

    # Integer Fields
    pull_merged_total = IntField()
    star_total = IntField()
    newcomer_total = IntField()
    commit_total = IntField()
    used_languages_total = IntField()
    fork_total = IntField()
    open_issues_total = IntField()
    age = IntField()

    # Dictionary Fields
    time_series = DictField()