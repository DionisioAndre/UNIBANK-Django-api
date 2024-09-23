from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Banco(models.Model):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    banco = models.CharField(max_length=200, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.banco)


class Conta(models.Model):
    conta = models.CharField(max_length=200, null=False, blank=False)
    bancoID = models.ForeignKey(Banco, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.conta)

class Perfil(models.Model):
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE, null=True)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)  # Utilize EmailField para e-mails
    telefone = models.CharField(max_length=20, null=True, blank=True)  # Alterado para CharField
    foto= models.ImageField(null=True, blank=True, default="/images/placehold.png", upload_to="images/")
    bi_frente = models.ImageField(null=True, blank=True, default="/images/placehold1.png", upload_to="images/")
    bi_verso = models.ImageField(null=True, blank=True, default="/images/placehold2.png", upload_to="images/")

    def __str__(self):
        return str(self.first_name)
