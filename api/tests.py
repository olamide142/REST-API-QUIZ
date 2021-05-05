import json

from django.test import TestCase
from api.models import Task


class TaskTestCase(TestCase):

    def setUp(self) -> None:
        a = Task.objects.create(title="Title Test", completed=None)
        a.save()
        b = Task.objects.create(title="Test Boy", completed=None)
        b.save()

    def test_task(self):
        a = Task.objects.get(id=1)
        b = Task.objects.get(id=2)
        self.assertEqual(str(a), "Title Test")
        self.assertEqual(str(b), "Test Boy")

    def test_rest_overview(self):

        res = self.client.get("/api/v1/")
        self.assertEqual(res.status_code, 200)

    def test_listview(self):

        res = self.client.get("/api/v1/task-list/")
        self.assertEqual(res.status_code, 200)
        self.assertIn("Title Test", str(res.content))

    def test_detail_view(self):

        res = self.client.get("/api/v1/task-detail/2/")
        self.assertEqual(res.status_code, 200)
        self.assertIn("Test Boy", str(res.content))

    def test_create_view(self):

        res = self.client.post("/api/v1/task-create/", \
                               {'title': "Test Master"})
        self.assertEqual(res.status_code, 200)
        self.assertIn("Test Master", str(res.content))

    def test_update_view(self):

        res = self.client.put("/api/v1/task-update/1/", \
                              {'title': "Test Girl", "completed": "None"})
        # self.assertEqual(res.status_code, 200)
        # self.assertIn("Test Girl" , str(res.content))
