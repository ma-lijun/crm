import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from crm.company.models import Company
from crm.contact.models import Contact
from crm.deal.models import Deal
# from crm.knowledge.models import KnowledgeBase, KnowledgeBaseCategory
from crm.link.models import Link
from crm.organization.models import Organization
from crm.project.models import Project
from crm.sprint.models import Sprint
from crm.task.models import Task, TaskTracking
from crm.comment.models import Comment
from crm.message.models import Message
# from crm.alert.models import Alert


# class KnowledgBaseTeype(SQLAlchemyObjectType):
#
#     class Meta:
#         model = KnowledgeBase
#
#
# class KnowledgeBaseCategoryType(SQLAlchemyObjectType):
#
#     class Meta:
#         model = KnowledgeBaseCategory


class ContactType(SQLAlchemyObjectType):

    class Meta:
        model = Contact


class CompanyType(SQLAlchemyObjectType):

    class Meta:
        model = Company


class OrganizationType(SQLAlchemyObjectType):

    class Meta:
        model = Organization


class DealType(SQLAlchemyObjectType):

    class Meta:
        model = Deal


class TaskType(SQLAlchemyObjectType):

    class Meta:
        model = Task


class TaskTrackingType(SQLAlchemyObjectType):

    class Meta:
        model = TaskTracking


class ProjectType(SQLAlchemyObjectType):

    class Meta:
        model = Project


class SprintType(SQLAlchemyObjectType):

    class Meta:
        model = Sprint


class LinkType(SQLAlchemyObjectType):

    class Meta:
        model = Link


class CommentType(SQLAlchemyObjectType):

    class Meta:
        model = Comment


class MessageType(SQLAlchemyObjectType):

    class Meta:
        model = Message

# class AlertType(SQLAlchemyObjectType):
#
#     class Meta:
#         model = Alert


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    contacts = graphene.List(ContactType)
    companies = graphene.List(CompanyType)
    organizations = graphene.List(OrganizationType)
    deals = graphene.List(DealType)
    links = graphene.List(LinkType)
    projects = graphene.List(ProjectType)
    sprints = graphene.List(SprintType)
    tasks = graphene.List(TaskType)
    comments = graphene.List(CommentType)
    messages = graphene.List(MessageType)
    # alerts = graphene.List(AlertType)
    # knowkedgebases = graphene.List(KnowledgBaseTeype)
    # knowledgebasecategories = graphene.List(KnowledgeBaseCategoryType)

    def resolve_contacts(self, args, context, info):
        query = ContactType.get_query(context)
        return query.all()

    def resolve_companies(self, args, context, info):
        query = CompanyType.get_query(context)
        return query.all()

    def resolve_organizations(self, args, context, info):
        query = OrganizationType.get_query(context)
        return query.all()

    def resolve_deals(self, args, context, info):
        query = DealType.get_query(context)
        return query.all()

    def resolve_projects(self, args, context, info):
        query = ProjectType.get_query(context)
        return query.all()

    def resolve_sprints(self, args, context, info):
        query = SprintType.get_query(context)
        return query.all()

    def resolve_tasks(self, args, context, info):
        query = TaskType.get_query(context)
        return query.all()

    def resolve_comments(self, args, context, info):
        query = CommentType.get_query(context)
        return query.all()

    def resolve_messages(self, args, context, info):
        query = MessageType.get_query(context)
        return query.all()

    def resolve_links(self, args, context, info):
        query = LinkType.get_query(context)
        return query.all()
    #
    # def resolve_alerts(self, args, context, info):
    #     query = AlertType.get_query(context)
    #     return query.all()
    #
    # def resolve_knowkedgebases(self, args, context, info):
    #     query = KnowledgBaseTeype.get_query(context)
    #     return query.all()
    #
    # def resolve_knowledgebasecategories(self, args, context, info):
    #     query = KnowledgeBaseCategoryType.get_query(context)
    #     return query.all()


schema = graphene.Schema(
    query=Query,
    types=[
        ContactType,
        CompanyType,
        OrganizationType,
        DealType,
        ProjectType,
        TaskType,
        LinkType,
        SprintType,
        CommentType,
        MessageType,
        # KnowledgBaseTeype,
        # KnowledgeBaseCategoryType,
        # AlertType
    ]
)
