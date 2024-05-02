from django.contrib import admin
from .models import Profile, Project, Application, Review, Specialization

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Application)
admin.site.register(Review)
admin.site.register(Specialization)