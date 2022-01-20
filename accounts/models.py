from django.contrib.auth.models import AbstractUser
from django.db import models
from stdimage.models import StdImageField
from django.conf import settings


class User(AbstractUser):
    id: int = models.AutoField(primary_key=True)
    name: str = models.CharField(blank=True, max_length=255)
    photo = StdImageField('Photo', upload_to='user_photos', variations={'thumb': (124, 124)})

    def __str__(self) -> str:
        return self.username if self.first_name == '' and self.last_name == '' else \
            self.first_name + ' ' + self.last_name

    class Meta:
        db_table: str = 'accounts_user'
        managed: bool = getattr(settings, 'DEBUG', False)
