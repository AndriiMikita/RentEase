from django.db import models

class Feature(models.Model):
    name = models.CharField(unique=True,
                            max_length=250)
    count = models.PositiveBigIntegerField()
    
class Apartment(models.Model):
    name = models.CharField(unique=True, 
                            max_length=250)
    description = models.TextField()
    features = models.ManyToManyField(Feature)

class Town(models.Model):
    name = models.CharField(unique=True, 
                            max_length=100)
    apartments = models.ForeignKey(Apartment, 
                                   on_delete=models.SET_NULL, 
                                   null=True)
    def __str__(self):
        apartment_names = ", ".join(apartment.name for apartment in self.apartment_set.all())
        return f"{self.name.capitalize()}: {apartment_names}"
    
class Type(models.Model):
    name = models.CharField(unique=True, 
                            max_length=100)
    apartments = models.ForeignKey(Apartment, 
                                   on_delete=models.SET_NULL, 
                                   null=True)
    def __str__(self):
        apartment_names = ", ".join(apartment.name for apartment in self.apartment_set.all())
        return f"{self.name.capitalize()}: {apartment_names}"
    
class ApartmentImages(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Image for {self.apartment.title}"