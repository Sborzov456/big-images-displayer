from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.name

class Segmentation(models.Model):
    patient_id = models.BigAutoField(primary_key=True, default=0)
    type = models.ForeignKey('Type', on_delete=models.RESTRICT)
    
    def __str__(self) -> str:
        return str(self.patient_id)

class Box(models.Model):
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    segmentation = models.ForeignKey('Segmentation', on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return str(self.segmentation)