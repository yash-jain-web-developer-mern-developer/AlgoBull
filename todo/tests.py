from django.test import TestCase
from .models import Todo, Tag

class TodoModelTest(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(name="Work")
        self.todo = Todo.objects.create(title="Test Task", description="Test Description", status="OPEN")

    def test_todo_creation(self):
        self.assertEqual(self.todo.title, "Test Task")
        self.assertEqual(self.todo.status, "OPEN")
