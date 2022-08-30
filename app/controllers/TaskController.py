from masonite.controllers import Controller
from masonite.views import View
from masonite.response import Response
from masonite.request import Request
from app.models.Task import Task


class TaskController(Controller):
    def index(self, view: View):
        tasks = Task.all()

        context = {
            "tasks": tasks
        }
        return view.render("tasks.index", context)

    def create(self, view: View):
        return view.render("tasks.create")

    def store(self, view: View, response: Response, request: Request):

        post_data = request.only('content', 'description')

        Task.create(post_data)

        return response.redirect('/')

    def show(self, view: View, request: Request):
        id = request.param('id')
        task = Task.find_or_fail(id)

        context = {
            "task": task
        }

        return view.render("tasks.show", context)

    def edit(self, view: View, request: Request):
        id = request.param('id')
        task = Task.find_or_fail(id)

        context = {
            "task": task
        }
        return view.render("tasks.edit", context)

    def update(self, view: View, response: Response, request: Request):
        id = request.param('id')
        task = Task.find_or_fail(id)

        post_data = request.only('content', 'description')

        task.update(post_data)

        return response.redirect('/')

    def destroy(self, request : Request, response: Response):
        id = request.param('id')
        task = Task.find_or_fail(id)
        task.delete()
        return response.redirect('/')
