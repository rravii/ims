from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class DUser(User):
    type = models.CharField(max_length=50)

    def joined(self):
        return  self.date_joined.strftime('%d %B, %Y')

    class Meta:
        db_table = "users"
