import os,sys,django
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.extend([BASE_DIR,])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "background_app.settings")
django.setup()
# from main.views import User
#
# user =User.objects.get(id=23)
# print(user)
print("hhhh")
