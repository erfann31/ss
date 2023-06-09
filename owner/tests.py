from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from owner.models import BusinessOwner
from owner.serializers import BusinessOwnerSerializer
from rest_framework.exceptions import ValidationError
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class BusinessOwnerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.business_owner = BusinessOwner.objects.create(phone_number='09123456789', first_name='John', last_name='Doe')

    def test_phone_number_label(self):
        business_owner = BusinessOwner.objects.get(id=self.business_owner.id)
        field_label = business_owner._meta.get_field('phone_number').verbose_name
        self.assertEqual(field_label, 'شماره تلفن')

    def test_first_name_max_length(self):
        business_owner = BusinessOwner.objects.get(id=self.business_owner.id)
        max_length = business_owner._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 31)

    def test_object_name_is_phone_number(self):
        business_owner = BusinessOwner.objects.get(id=self.business_owner.id)
        expected_object_name = f"{business_owner.first_name} {business_owner.last_name}"
        self.assertEqual(expected_object_name, str(business_owner))


class BusinessOwnerViewSetTest(TestCase):
    def setUp(self):
        self.business_owner = BusinessOwner.objects.create(phone_number='09123456789', first_name='John', last_name='Doe')
        self.user = User.objects.create_user(username='john.doe', password='password')  # Create a user
        self.business_owner.user = self.user  # Associate the user with the business owner
        self.business_owner.save()
        self.token = Token.objects.create(user=self.user)  # Create a Token object for the user
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.client.force_authenticate(user=self.user)

    def test_permissions(self):
        url = reverse('owner-api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_queryset(self):
        response = self.client.get(reverse('owner-api'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), BusinessOwner.objects.count())

    def test_search_fields(self):
        response = self.client.get(reverse('owner-api') + '?search=09123456789')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["phone_number"], "09123456789")



class BusinessOwnerSerializerTest(TestCase):
    def test_invalid_verification_code(self):
        owner = BusinessOwner(phone_number='09123456789', first_name='John', last_name='Doe')
        data = {'verification_code': '123456'}
        serializer = BusinessOwnerSerializer(instance=owner, data=data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_read_only_fields(self):
        owner = BusinessOwner(phone_number='09123456789', first_name='John', last_name='Doe')
        serializer = BusinessOwnerSerializer(owner)
        self.assertIn('id', serializer.data)
        self.assertIn('created_at', serializer.data)

