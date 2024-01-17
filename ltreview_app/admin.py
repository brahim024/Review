from django.contrib import admin
from .models import Ticket, Review, UserFollows, CustomUser

admin.site.register(Ticket)
admin.site.register(Review)
admin.site.register(UserFollows)
admin.site.register(CustomUser)

