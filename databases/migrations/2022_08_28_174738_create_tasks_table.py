"""CreateTasksTable Migration."""

from masoniteorm.migrations import Migration


"""
table tasks:
    id :int
    content:str(255)
    description: text
    is_complete: bool (true/false)
"""


class CreateTasksTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("tasks") as table:
            table.increments("id")
            table.string("content", length=255)
            table.text("description")
            table.boolean("is_complete").default(False)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("tasks")
