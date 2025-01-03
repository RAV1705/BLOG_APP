from django.apps import AppConfig


class UsersConfig(AppConfig):
     name = 'users'
     
     def ready(self):  #override the ready method
        import users.signals    #import the signals module when the app is ready 
