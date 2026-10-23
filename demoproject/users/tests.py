from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group

class UserAccessTestCase(TestCase):
    def setUp(self):

        self.client = Client()
        
        self.reader_group = Group.objects.create(name='Lezer')
        self.reader_user = User.objects.create_user(username='reader', password='reader')
        self.reader_user.groups.add(self.reader_group)

        self.employee_group = Group.objects.create(name='Medewerker')
        self.employee_user = User.objects.create_user(username='employee', password='employee')
        self.employee_user.groups.add(self.employee_group)
        
        self.target_url = reverse('users')  # Replace 'users' with your actual path name

    def test_unauthenticated_user_is_redirected(self):
        
        response = self.client.get(self.target_url)
        
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

    def test_employee_user_has_access(self):

        self.client.login(username='employee', password='employee')  

        response = self.client.get(self.target_url)

        self.assertEqual(response.status_code, 200)

    def test_reader_user_is_blocked_from_admin_url(self):
        
        self.client.login(username='reader', password='reader')   

        response = self.client.get(self.target_url)

        self.assertEqual(response.status_code, 302)
