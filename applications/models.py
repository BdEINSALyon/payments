from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=100)
    oauth_id = models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)
    test_mode = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ApplicationRequest(models.Model):
    application = models.ForeignKey(
        to=Application,
        on_delete=models.CASCADE,
        related_name='requests'
    )
    endpoint = models.TextField()
    method = models.CharField(max_length=10)
    params = models.TextField(blank=True)
    response = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

