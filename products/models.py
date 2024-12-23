from django.db import models
from PIL import Image as PILImage, ImageDraw
from django.conf import settings

class Location(models.Model):
    location = models.CharField(max_length=255)
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.location

    class Meta:
        indexes = [
            models.Index(fields=['location']),
        ]


class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.FloatField()
    location = models.ForeignKey(Location, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['location']),
        ]

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, blank=True, )

    def __str__(self):
        return f"Image | {self.product.title}"
    
    def save(self, *args, **kwargs):
        # Save the image first
        super().save(*args, **kwargs)

        # Open the saved image
        img_path = self.image.path
        img = PILImage.open(img_path).convert("RGBA")

        # Open the watermark
        watermark = PILImage.open(settings.WATERMARK_PATH).convert("RGBA")

        # Resize the watermark to match the dimensions of the image
        watermark = watermark.resize(img.size, PILImage.Resampling.LANCZOS)

        # Apply the watermark
        blended = PILImage.alpha_composite(img, watermark)

        # Save the modified image
        blended = blended.convert("RGB")  # Convert back to RGB if needed
        blended.save(img_path, format="JPEG")  # Save as JPEG or PNG
