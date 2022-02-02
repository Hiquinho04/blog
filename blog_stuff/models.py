from django.db import models

# Create your models here.
# For a new model use 'class ...'

class Title(models.Model):
    """Model responsável por gerenciar os tópicos"""
    title = models.CharField(max_length = 50)
    date_added = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        """Devolve a informção"""
        return self.title
