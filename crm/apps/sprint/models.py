from crm.db import db, BaseModel, RootModel
from crm.mailer import sendemail


class Sprint(db.Model, BaseModel, RootModel):

    __tablename__ = "sprints"

    name = db.Column(
        db.String(255),
        nullable=False,
        index=True
    )

    # should be markdown.
    description = db.Column(
        db.Text(),
        default="",
        index=True
    )

    start_date = db.Column(
        db.TIMESTAMP,
        index=True
    )

    deadline = db.Column(
        db.TIMESTAMP,
        index=True
    )

    contacts = db.relationship(
        "Contact",
        secondary="contacts_sprints",
        backref="sprints"
    )

    tasks = db.relationship(
        "Task",
        backref="sprint"
    )

    comments = db.relationship(
        "Comment",
        backref="sprint"
    )

    links = db.relationship(
        "Link",
        backref="sprint"
    )

    messages = db.relationship(
        "Message",
        backref="sprint"
    )

    owner_id = db.Column(
        db.String(5),
        db.ForeignKey('users.id')
    )

    project_id = db.Column(
        db.String(5),
        db.ForeignKey('projects.id')
    )

    def notify(self, msgobj, attachments=[]):
        emails = []
        for c in self.contacts:
            if c.emails:
                emails.extend(c.emails.split(","))
        if self.owner and self.owner.emails:
            emails.extend(self.owner.emails.split(","))
        sendemail(to=emails, subject=msgobj.title,
                  body=msgobj.content, attachments=attachments)

    @property
    def percentage_done(self):
        pass

    @property
    def hours_open(self):
        pass

    @property
    def hours_open_person_avg(self):
        pass

    @property
    def hours_open_person_max(self):
        pass

    def __str__(self):
        return self.name
