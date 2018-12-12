from django.db import models

class Mag(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    class Meta:
        verbose_name = "Mag"
        verbose_name_plural = "Mags"

    def __str__(self):
        return self.name

class Prod(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    class Meta:
        verbose_name = "Prod"
        verbose_name_plural = "Prods"

    def __str__(self):
        return self.name

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mag = models.ForeignKey(
        'Mag',
        on_delete=models.CASCADE,
        blank=True,
    )
    prod = models.ForeignKey(
        'Prod',
        on_delete=models.CASCADE,
        default=None,
        blank=True,
    )


    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)