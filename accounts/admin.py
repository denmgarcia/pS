from django.contrib import admin
from accounts.models import  News, AddressBook

class AddressBooksAdmin(admin.ModelAdmin):
	class Meta:
		fields = AddressBook

	search_fields = ['first_name','phone',]

	list_display = (
		'first_name', 'last_name', 'phone', 'address'

	)

class NewsAdmin(admin.ModelAdmin):
	class Meta:
		fields = News
		verbose_name_plural = "News"

	list_display = [
		'headline', 'author', 'pub_date','body',
	]


admin.site.register(AddressBook, AddressBooksAdmin)
admin.site.register(News, NewsAdmin)
admin.site.site_header = ("School System Login")
