from django.db import models

class Article(models.Model):
    Autor = models.CharField(max_length = 50)
    Editora = models.CharField(max_length = 50)
    Paginas = models.IntegerField()
    Titulo = models.CharField(max_length = 50)
    ano = models.IntegerField()
    Email = models.EmailField(null = True)


    def __str__(self):
        return self.headline


# Create your models here.
