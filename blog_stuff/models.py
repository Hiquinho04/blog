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

class Text(models.Model):
    """Model responsável por gerenciar as informações adicionadas
        em cada tópico"""
    title = models.ForeignKey(Title, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """Devolve a informação"""
        if(len(self.text)<50):
            return self.text
        else:
            return self.text[:50] + "..."