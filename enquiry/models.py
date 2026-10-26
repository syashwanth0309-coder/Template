from django.db import models
class Enquiry(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Enquiries"
    def __str__(self):
        return f"{self.name} — {self.email}"
