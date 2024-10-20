from django.core.management.base import BaseCommand
from accounts.models import User
from django.conf import settings

class Command(BaseCommand):
    def handle(self, *args, **options):

        if User.objects.filter(email=settings.SUPERUSER_EMAIL).exists():
            print('管理アカウントがすでに存在します')
            return
       
        user = User.objects.create_superuser(
            email=settings.SUPERUSER_EMAIL,
            password=settings.SUPERUSER_PASSWORD,
        )
        print('管理アカウントを作成しました')