from django.contrib import admin
from login.models import UserProfile, Books


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'USN', 'year', 'sem', 'phone']


class BookAdmin(admin.ModelAdmin):
    list_display = ['user', 'book_name', 'price', 'description', 'negotiable', 'date_posted', 'date_updated']

    def get_queryset(self, request):  # sorts the ads wrt date (latest first)
        queryset = super(BookAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-date_posted')  # reverse the sort
        return queryset


admin.site.register(Books, BookAdmin)
