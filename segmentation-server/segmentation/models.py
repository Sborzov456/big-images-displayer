from django.db import models

class Image(models.Model):
    image_file = models.FileField(upload_to='shots/', null=True)
    image_file_name = models.CharField(max_length=255)

class Type(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    
    def __str__(self) -> str:
        return self.name

class Segmentation(models.Model):
    image = models.ForeignKey(Image, on_delete=models.RESTRICT, null=False)
    type = models.ForeignKey(Type, on_delete=models.RESTRICT)

    class Meta:
        unique_together = ['image_id', 'type'] 
    
    def __str__(self) -> str:
        return f'Image: {self.image}; Type: {self.type}; Id: {self.id}'

class Polygon(models.Model):
    segmentation = models.ForeignKey(Segmentation, related_name='polygons', on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return f'Polygon {self.id}'

class Point(models.Model):
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    polygon = models.ForeignKey(Polygon, related_name='points', on_delete=models.RESTRICT)


class Correction(models.Model):
    correction = models.JSONField()
    segmentation = models.ForeignKey(Segmentation, on_delete=models.RESTRICT)