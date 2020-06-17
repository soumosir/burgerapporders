from django.db import models
# Create your models here.
class Order(models.Model):

    username = models.CharField(max_length=256)
    slices = models.IntegerField(default=0)
    cutlets = models.IntegerField(default=0)
    salad = models.BooleanField(default=False)
    buns = models.IntegerField(default=2)
    timestamp = models.TimeField(auto_now_add=True)
    cost = models.IntegerField(default=10)

# ("id","username","salad","buns","slices","cutlets","cost","timestamp")

    # class Meta:
    #     ordering = ('timestamp', )

    def __str__(self):
        return str(self.id) + " --- " + self.username




