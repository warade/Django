from django.contrib import admin
from .models import PostModel

class PostModelAdmin(admin.ModelAdmin):
	fields = [
		'title',
		'slug',
		'content',
		'publish',
		'publish_date',
		'active',
		'timestamp',
		'updated',
		'new_content',
		'get_age'
	]
	readonly_fields = ['timestamp', 'updated', 'new_content', 'get_age']

	def new_content(self, obj, *args, **kwargs):
		return str(obj.title)
	
	def get_age(self, obj, *args, **kwargs):
		return str(obj.age)
	class Meta:
		model = PostModel


admin.site.register(PostModel, PostModelAdmin)