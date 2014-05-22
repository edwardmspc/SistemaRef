from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class UserAdmin(UserAdmin):
	#list_display = ('username', 'email', 'first_name', 'last_name','last_login')
	#filter_horizontal = ("groups", "user_permissions")
	fieldsets = (
		('User', {'fields' : ('username', 'password')}),
		('Persona Info' , {'fields' : ('first_name',
						'last_name',
						'email',
						'referred',
						'date_joined',
						'last_login')}),
		('Permissions' , {'fields' : ('is_active',
						'is_staff',
						'is_superuser',
						'groups',
						'user_permissions'
						)}),
		)
admin.site.register(CustomUser, UserAdmin)
