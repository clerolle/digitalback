
import json
from django.http import HttpResponse
from django.views import View
from User.models.user import User


class UserView(View):
    def get(self, request):
        list_users = []
        users = User.objects.filter(is_active=True)
        for user in users:
            list_users.append(User.serialize(user))
        return HttpResponse(json.dumps({
            'data': list_users
        }), content_type="application/json")

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        user = User.from_instance(data)
        user.save()
        return HttpResponse(json.dumps({
            'mesagge': 'Creacion Exitosa'
        }), content_type="application/json")

    def put(self, request):
        update_fields = []
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        user = User.objects.get(id=data['id'])

        if data.get('name'):
            update_fields.append('name')
            user.name = data['name']

        if data.get('gender'):
            update_fields.append('gender')
            user.gender = data['gender']

        if data.get('birthday'):
            update_fields.append('birthday')
            user.birthday = data['birthday']

        user.save(update_fields=update_fields)
        return HttpResponse(json.dumps({
            'mesagge': 'Actualizacion Exitosa'
        }), content_type="application/json")

    def delete(self, request):
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        user = User.objects.get(id=data['id'])
        user.is_active = False
        user.save(update_fields=['is_active'])
        return HttpResponse(json.dumps({
            'mesagge': 'Eliminacion Exitosa'
        }), content_type="application/json")
