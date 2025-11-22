from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True)
    banner = models.ImageField(upload_to='events/', blank=True, null=True)
    whatsapp_link = models.CharField(max_length=255, blank=True, help_text="opcional: link wa.me para marcar presença")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['-date']

class SocialAction(models.Model):
    title = models.CharField(max_length=200)
    short_story = models.TextField(help_text="Resumo da ação")
    long_story = models.TextField(blank=True)
    date = models.DateField()
    cover = models.ImageField(upload_to='social_actions/', blank=True, null=True)

   
    def __str__(self):
        return f"{self.title} ({self.date})"

    class Meta:
        verbose_name = "Ação Social"
        verbose_name_plural = "Ações Sociais"
        ordering = ['-date']

class Photo(models.Model):
    social_action = models.ForeignKey(SocialAction, on_delete=models.CASCADE, related_name='photos', null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='photos', null=True, blank=True)
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.caption or f'Foto {self.id}'

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"