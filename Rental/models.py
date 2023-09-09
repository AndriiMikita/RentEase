from django.db import models


class Feature(models.Model):
    name = models.CharField(unique=True,
                            max_length=250)
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
    
class Town(models.Model):
    name = models.CharField(unique=True, 
                            max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
    
class Apartment(models.Model):
    name = models.CharField(unique=True, 
                            max_length=250)
    description = models.TextField()
    square = models.PositiveIntegerField(default=0,)
    occupants = models.PositiveIntegerField(default=0,)
    town = models.ForeignKey(Town, 
                             on_delete=models.SET_NULL, 
                             null=True, 
                             related_name='apartments')

    def __str__(self):
        return self.name
    
class ApartmentFeature(models.Model):
    apartment = models.ForeignKey(Apartment, 
                                  on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature,
                                on_delete=models.CASCADE,
                                default="")
    count = models.PositiveIntegerField(default=0,)
    
class Type(models.Model):
    name = models.CharField(unique=True, 
                            max_length=100)
    apartments = models.ForeignKey(Apartment, 
                                   on_delete=models.SET_NULL, 
                                   null=True,
                                   blank=True,)
    def __str__(self):
        return self.name.capitalize()
    class Meta:
        ordering = ['name']
    
class ApartmentImages(models.Model):
    apartment = models.ForeignKey(Apartment, 
                                  on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Image for {self.apartment.title}"
    
class Booking(models.Model):
    apartment = models.ForeignKey('Apartment', 
                                  on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()