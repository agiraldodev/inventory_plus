from django.db import models
from django.forms import ValidationError


class Equipo(models.Model):
    ubicacion = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    procesador = models.CharField(max_length=200)
    arquitecturaBoard = models.CharField(
        max_length=100, verbose_name='Arquitectura Board')
    tarjetaMadre = models.CharField(
        max_length=100, verbose_name='Tarjeta Madre')
    memoria = models.CharField(max_length=200)
    disco_duro = models.CharField(max_length=100, verbose_name='Disco Duro')
    monitor = models.CharField(max_length=200)
    dvd = models.CharField(max_length=100, verbose_name='Unidad CD/DVD')
    tarjetaRed = models.CharField(max_length=100, verbose_name='Tarjeta Red')
    mouse = models.CharField(max_length=100)
    teclado = models.CharField(max_length=100)
    parlantes = models.CharField(max_length=100)
    tarjetaAceleradora = models.CharField(
        max_length=100, verbose_name='Tarjeta Aceleradora')
    sistemaOperativo = models.CharField(
        max_length=100, verbose_name='Sistema Operativo')
    office = models.CharField(max_length=100)
    antivirus = models.CharField(max_length=100)

    def __str__(self):
        return self.codigo


class TipoMantenimiento(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Mantenimiento(models.Model):
    fechaHoraMantenimiento = models.DateTimeField(verbose_name='Fecha y Hora de Mantenimiento')
    descripcion = models.TextField(blank=True, null=True, verbose_name='Mantenimiento Realizado')

    tiposMantenimiento = models.ManyToManyField(TipoMantenimiento, verbose_name='Tipos de Mantenimiento')
    equipoID = models.ForeignKey(Equipo, related_name='mantenimientos', on_delete=models.CASCADE)

    def __str__(self):
        return self.fechaHoraMantenimiento.strftime('%Y-%m-%d %H:%M:%S')
