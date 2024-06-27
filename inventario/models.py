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


class Mantenimiento(models.Model):
    TIPO_MANTENIMIENTO_CHOICES = [
        ('preventivo', 'Preventivo'),
        ('correctivo', 'Correctivo')
    ]

    fechaHoraMantenimiento = models.DateTimeField(
        verbose_name='Fecha y Hora de Mantenimiento')
    descripcion = models.TextField(
        blank=True, null=True, verbose_name='Mantenimiento Realizado')

    tipoMantenimiento = models.CharField(
        max_length=100,
        verbose_name='Tipo de Mantenimiento',
        help_text='Seleccione uno o ambos tipos separados por comas (,). Ejemplo: "preventivo, correctivo"',
        choices=TIPO_MANTENIMIENTO_CHOICES,
    )

    equipoID = models.ForeignKey(
        Equipo, related_name='mantenimientos', on_delete=models.CASCADE)

    def clean(self):
        # Validar que tipoMantenimiento contenga opciones válidas
        tipo_choices = [choice[0]
                        for choice in self.TIPO_MANTENIMIENTO_CHOICES]
        selected_choices = [choice.strip() for choice in self.tipoMantenimiento.split(
            ',') if choice.strip()]

        for choice in selected_choices:
            if choice not in tipo_choices:
                raise ValidationError(
                    f'{choice} no es una opción válida para Tipo de Mantenimiento. Seleccione entre "preventivo" y "correctivo".'
                )

    def __str__(self):
        return self.fechaHoraMantenimiento.strftime('%Y-%m-%d %H:%M:%S')
