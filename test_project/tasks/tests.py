from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Task


class TaskAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_url = reverse('task-list')
        self.task_data = {'title': 'Test task', 'description': 'Test description', 'completed': False}

    def test_create_task(self):
        response = self.client.post(self.task_url, self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_tasks(self):
        Task.objects.create(**self.task_data)
        response = self.client.get(self.task_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_task(self):
        task = Task.objects.create(**self.task_data)
        update_url = reverse('task-detail', args=[task.id])
        response = self.client.put(update_url, {'title': 'Updated task', 'description': 'Updated description', 'completed': True}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        task = Task.objects.create(**self.task_data)
        delete_url = reverse('task-detail', args=[task.id])
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
