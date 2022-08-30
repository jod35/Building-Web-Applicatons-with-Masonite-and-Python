""" Task Model """

from masoniteorm.models import Model


class Task(Model):
    """Task Model"""

    __table__ = "tasks"
