# from flask_sqlalchemy import SQLAlchemy
from apps.users.models import User


class TestUser:
    def setup_method(self):
        self.data = {
            'username': 'vinicius_test1_username',
            'full_name': 'vinicius_test1_name',
            'active': True,
            'email': 'vinicius@test1.com',
            'password': 'password_test1',
            'cpf': '11111111111'
        }

        # Instances a User model
        self.model = User(**self.data)

    # Tests
    def test_email_field_exists(self):
        """
        Verify if email's field exists
        """
        assert self.model.email

    def test_email_field_is_str(self):
        """
        Verify is email's field is string type
        """
        assert isinstance(self.model.email, str)

    def test_active_field_exists(self):
        assert self.model.active

    def test_active_field_is_bool(self):
        """
        Verify if activate field is bool
        """
        assert isinstance(self.model.active, bool)

    def test_full_name_field_exists(self):
        """
        Verify if full_name field exists
        """
        assert self.model.full_name

    def test_full_name_field_is_str(self):
        """
        Verify if full_name is str
        """
        assert isinstance(self.model.full_name, str)

    def test_all_fields_in_model(self):
        """
        Verify if all fields are according to the model
        """
        fields = [
            '_sa_instance_state', 'active', 'cpf', 'date_created', 'email',
            'full_name', 'id', 'password', 'role', 'username'
        ]

        model_keys = [i for i in self.model.__dict__.keys()]

        assert model_keys.sort() == fields.sort()
