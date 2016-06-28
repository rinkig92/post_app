from django.contrib import admin

from .models import PostModel

class PostAdmin(admin.ModelAdmin):
	list_display = ["title", "timestamp"]
	list_display_links = ["updated"]
	list_filter = ["updated", "timestamp"]
	search_fields = ["title"]

	class Meta:
		model = PostModel

	admin.site.register(PostModel)
