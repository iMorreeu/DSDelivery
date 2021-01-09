from django.db import models


# Create your models here.
class Product(models.Model):
    class Meta:
        verbose_name_plural = "Produtos"
        verbose_name = "Produto"

    name = models.CharField(max_length=30, verbose_name="Nome")
    price = models.FloatField()
    description = models.TextField()
    imageUri = models.ImageField(upload_to="uploads", verbose_name="Imagem")

    def formatted_uri(self):
        return "http://localhost:8000/" + self.imageUri.name.replace(
            "uploads", "images"
        )
