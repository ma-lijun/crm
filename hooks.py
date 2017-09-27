from sqlalchemy.event import listen

from crm.utils import get_current_username
from crm.db import BaseModel


def generate_record_id(mapper, connect, target):
    """
    Given a target (model) replace target.id with target.uid
    target.uid is a unique uid of 5 characters used to identify
    record and auto generated
    
    :param mapper: 
    :param connect: 
    :param target: Target model
    """
    target.id = target.uid


def update_last_author(mapper, connect, target):
    """
    Only used if model actually successfully changed
    
    Given a target (model) update target.author_last 
    with the current user.

    :param mapper: 
    :param connect: 
    :param target: Target model
    """
    target.author_last = get_current_username()


def update_original_author(mapper, connect, target):
    """
    Only used if model actually created

    Given a target (model) update target.author_original 
    with the current user.

    :param mapper: 
    :param connect: 
    :param target: Target model
    """
    target.author_original = get_current_username()


for klass in BaseModel.__subclasses__():
    listen(klass, 'before_insert', generate_record_id)
    listen(klass, 'before_insert', update_original_author)
    listen(klass, 'before_update', update_last_author)
