from django.db import models


# Create your models here.
class sportsData(models.Model):
    league_id = models.IntegerField()
    league_name  = models.CharField(max_length=100)
    league_type = models.CharField(max_length=100)
    league_country = models.CharField(max_length=100)
    league_season_year =  models.CharField(max_length=100)
    league_season_start = models.CharField(max_length=100)
    league_season_end = models.CharField(max_length=100)

    def __str__(self):
        return self.league_id
    
