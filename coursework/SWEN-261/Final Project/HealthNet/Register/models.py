from django.utils import timezone
from Profiles.models import Patient



# Create your models here.

class Post(Patient):

    """
    class Meta:
        db_table = 'Profiles_patient' """

    def publish(self):
        self.published_date = timezone.now()
        self.save()

