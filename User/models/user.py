
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name', null=False, blank=True)
    gender = models.CharField(max_length=1, verbose_name='Gender', null=False, blank=True)
    birthday = models.DateTimeField(auto_now=False)
    is_active = models.BooleanField(default=True, verbose_name='Is_Active', null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User'

    @staticmethod
    def from_instance(data: dict) -> 'User':
        user = User()
        user.name = data['name']
        user.gender = data['gender']
        user.birthday = data['birthday']

        return user

    @staticmethod
    def serialize(user):
        return {
            'id': user.id,
            'name': user.name,
            'gender': user.gender,
            'birthday': user.birthday.strftime('%Y-%m-%d'),
        }
