from django.db import models

# Create your models here.
class Predmet(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'

    def __str__(self):
        return self.name

class Profil(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'

    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'уровень'
        verbose_name_plural = 'уровни'

    def __str__(self):
        return self.name

class Orgs(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(blank=True)
    short_name = models.CharField(max_length=255)
    class Meta:
        verbose_name = 'организатор'
        verbose_name_plural = 'организаторы'

    def __str__(self):
        return self.name    

class Olymps(models.Model):
    full_name = models.CharField(max_length=255)
    url = models.URLField(blank=True)
    class Meta:
        verbose_name = 'олимпиада'
        verbose_name_plural = 'олимпиады'

    def __str__(self):
        return self.full_name   

class OlympNapr(models.Model):
    olympiad = models.ForeignKey(Olymps, on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil, on_delete=models.SET_NULL, null=True, blank=True)
    predmet = models.ForeignKey(Predmet, on_delete=models.SET_NULL, null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.full_name   

class OlympOrgs(models.Model):
    olympiad = models.ForeignKey(Olymps, on_delete=models.CASCADE)
    orgs = models.ForeignKey(Orgs, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('olympiad', 'organisator')
        verbose_name = 'Олимпиада – организатор'
        verbose_name_plural = 'Олимпиады – организаторы'
