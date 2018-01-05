from django.db import models


class Brand(models.Model):
    B_Id = models.IntegerField(default=0, primary_key=True)
    brandName = models.TextField(default="")
    modelName = models.TextField(default="", null=True)
    version = models.TextField(default="", null=True)
    link = models.TextField(default="")


class Car(models.Model):
    B_Id = models.IntegerField(default=0)
    L_Id = models.IntegerField(default=0, primary_key=True)

    year = models.IntegerField(default=0)
    mileage = models.IntegerField(default=0)
    power = models.IntegerField(default=0)
    capacity = models.IntegerField(default=0)
    fuel = models.TextField(default=0)
    color = models.TextField(default=0)
    usedOrNew = models.TextField(default=0)
    doors = models.TextField(default=0)
    gearBox = models.TextField(default=0)

    price = models.IntegerField(default=0)
    time = models.DateTimeField()

    def __str__(self):
        msg = ""
        msg += "Year: %d, " % self.year
        msg += "Mileage: %d, " % self.mileage
        msg += "Power: %d, " % self.power
        msg += "Capacity: %d, " % self.capacity
        msg += "Fuel: %s, " % self.fuel
        msg += "Color: %s, " % self.color
        msg += "State: %s, " % self.usedOrNew
        msg += "GearBox: %s, " % self.gearBox
        msg += "Price: %d" % self.price
        return msg
