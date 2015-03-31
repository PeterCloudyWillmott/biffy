from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from accounts.models import Account,BiffyUser
# Register your models here.

#class B1ifAdmin(admin.ModelAdmin):


#admin.site.register(B1if, B1ifAdmin)
admin.site.register(Account)

class BiffyUserInline(admin.StackedInline):
    model = BiffyUser
    can_delete = False
    verbose_name_plural = 'biffy user'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (BiffyUserInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)