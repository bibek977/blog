from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):

    id = models.AutoField(primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Blog(BaseModel):

    title = models.CharField(max_length=400)
    description = models.TextField()
    image = models.ImageField(upload_to="media")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")


    def __str__(self):
        return self.title