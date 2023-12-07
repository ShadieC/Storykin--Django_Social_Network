from django.contrib import admin
from .models import Post,Article,Book,PostComment
# Register your models here.

admin.site.register(Post)
admin.site.register(Article)
admin.site.register(Book)
admin.site.register(PostComment)
