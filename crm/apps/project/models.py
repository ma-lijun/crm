from crm.db import db, BaseModel, RootModel
from crm.mailer import sendemail


class Project(db.Model, BaseModel, RootModel):

    __tablename__ = "projects"

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

    comments = db.relationship(
        "Comment",
        backref="project"
    )

    links = db.relationship(
        "Link",
        backref="project"
    )

    tasks = db.relationship(
        "Task",
        backref="project"
    )

    messages = db.relationship(
        "Message",
        backref="project"
    )

    sprints = db.relationship(
        "Sprint",
        backref="project",
        primaryjoin="Project.id==Sprint.project_id"
    )

    # alert_source_id = db.Column(
    #     db.String,
    #     db.ForeignKey("alertsources.id")
    # )

    contacts = db.relationship(
        "Contact",
        secondary="contacts_projects",
        backref=db.backref("projects")
    )

    promoter_id = db.Column(
        db.String(5),
        db.ForeignKey('users.id')
    )

    guardian_id = db.Column(
        db.String(5),
        db.ForeignKey('users.id')
    )

    def notify(self, msgobj, attachments=[]):
        emails = []
        for c in self.contacts:
            emails.extend(c.emails.split(","))
        if self.promoter and self.promoter.emails:
            emails.extend(self.promoter.emails.split(","))
        if self.guardian and self.guardian.emails:
            emails.extend(self.guardian.emails.split(","))
        if emails:
            sendemail(to=emails, subject=msgobj.title,
                      body=msgobj.content, attachments=attachments)

    @property
    def percentage_done(self):
        pass

    def __str__(self):
        return self.name
