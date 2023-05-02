from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    
    def __str__(self) -> str:
        return self.name

class Segmentation(models.Model):
    image_id = models.IntegerField(null=False)
    type = models.ForeignKey('Type', on_delete=models.RESTRICT)

    class Meta:
        unique_together = ['image_id', 'type'] 
    
    def __str__(self) -> str:
        return f'Image: {self.image_id}; Type: {self.type}; Id: {self.id}'

class Box(models.Model):
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    segmentation = models.ForeignKey(Segmentation, related_name='boxes', on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return f'Box {self.id}'
    
class Correction(models.Model):
    correction = models.JSONField()
    segmentation = models.ForeignKey(Segmentation, on_delete=models.RESTRICT)