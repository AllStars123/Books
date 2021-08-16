from django.contrib.auth import get_user_model
from django.test import Client
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

User = get_user_model()


class ProfileTest(APITestCase):
    def setUp(self):
        self.auth_client = Client()
        self.user = User.objects.create_user(
            username='nikita1',
            password='Posha2602'
        )
        self.auth_client.force_login(self.user)

    def test_registration(self):
        data = {'username': 'test', 'password1': 'Posha2602', 'password2': 'Posha2602'}
        response = self.client.post('/registration/', data)
        self.assertEqual(response.status_code, 201)


class ProfileTestGetPutDelete(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="nikita1",
                                             password="Posha2602",
                                             )
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        self.unauth_client = Client()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_get_all_books(self):
        response = self.client.get("/getbooks/")
        self.assertEqual(response.status_code, 200)

    def test_user_delete(self):
        response = self.client.delete("deletebook/1")
        self.assertEqual(response.status_code, 404)

    def test_user_put_update(self):
        data = {"title": "Test", "description": "test", "author": 1}
        response = self.unauth_client.put("/updatebook/1", data)
        self.assertEqual(response.status_code, 401)

    def test_user_add(self):
        data = {"title": "Finansis", "description": "Good book", "author": 1}
        response = self.unauth_client.post("/addbooks/", data)
        self.assertEqual(response.status_code, 401)
