from .models import Blog
from django.contrib.auth.models import User

def create_admin():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'password')

    def get_blog_by_id(id):
        return Blog.objects.get(id=id)