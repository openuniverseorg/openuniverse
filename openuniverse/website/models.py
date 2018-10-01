from mongoengine import connect, Document, StringField, IntField, DictField
from openuniverse.settings import MONGO_DATABASE

connect(MONGO_DATABASE)

class Projects(Document):
    project_id = StringField()
    name = StringField()
    owner = StringField()
    owner_type = StringField()
    domain = StringField()
    license = StringField()
    age = IntField()
    main_language = StringField()
    github_url = StringField()
    statistics = DictField()
    time_series = DictField()
    features = DictField()