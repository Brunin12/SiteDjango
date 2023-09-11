from django.db import models

class Categoria(models.Model):
  dt_creation = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=100)
  def __str__(self):
    return self.name

class Transacao(models.Model):
  dt_creation = models.DateTimeField()
  description = models.CharField(max_length=200)
  value = models.DecimalField(max_digits=7, decimal_places=2)
  category = models.ForeignKey(Categoria, on_delete=models.CASCADE)
  notes = models.TextField()
  id_usuario = ''


  def __str__(self):
    return self.description

