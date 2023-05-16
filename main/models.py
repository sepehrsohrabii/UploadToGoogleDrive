from django.db import models
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()


class Sample(models.Model):
    id = models.AutoField( primary_key=True)
    sample_name = models.CharField(max_length=200)
    sample_data = models.FileField(upload_to='test/', storage=gd_storage)