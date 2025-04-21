from django.db import models


# Cat fact model
class Fact(models.Model):
    name = models.CharField(max_length=100)  # Fact title
    description = models.CharField(max_length=500)  # Fact content
    breed = models.CharField(max_length=100)  # Cat breed

    # Display name in admin shell
    def __str__(self):
        return self.name
