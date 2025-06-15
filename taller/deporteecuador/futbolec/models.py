from django.db import models

class Club(models.Model):
    nombre_club = models.CharField(max_length=100)
    codigo_club = models.CharField(max_length=10)
    usuario_twitter = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre_club} ({self.codigo_club})"

class Deportista(models.Model):
    nombre_jugador = models.CharField(max_length=100)
    rol_juego = models.CharField(max_length=30)
    dorsal = models.IntegerField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    club_asociado = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_jugador} - {self.club_asociado.nombre_club}"

class Torneo(models.Model):
    titulo_torneo = models.CharField(max_length=100)
    empresa_auspiciante = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titulo_torneo} ({self.empresa_auspiciante})"

class ParticipacionClub(models.Model):
    temporada = models.IntegerField()
    club_participante = models.ForeignKey(Club, on_delete=models.CASCADE)
    torneo_asociado = models.ForeignKey(Torneo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.temporada} - {self.club_participante.nombre_club} - {self.torneo_asociado.titulo_torneo}"
