from django.db import models
import os
import uuid


def recipe_image_file_path(instance, filename):
    """
    Generate a file path and unique name for new recipe image
    """
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"

    return os.path.join("uploads/recipe/", filename)


class Book(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()
    poster_image = models.ImageField(null=True, upload_to=recipe_image_file_path)

    def __str__(self):
        return self.title
