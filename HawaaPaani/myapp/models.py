from django.db import models


# Create your models here.
class WQI(models.Model):
    STATE = models.CharField(max_length=4, primary_key=True)
    MONTH = models.IntegerField(default=0)
    TEMP = models.FloatField(default=0, null=True)
    DO = models.FloatField(default=0, null=True)
    PH = models.FloatField(default=0, null=True)
    COND = models.FloatField(default=0, null=True)
    BOD = models.FloatField(default=0, null=True)
    NITRITE = models.FloatField(default=0, null=True)
    FECAL = models.FloatField(default=0, null=True)
    TOTALCOLIFORM = models.FloatField(default=0, null=True)
    TURB = models.FloatField(default=0, null=True)
    TDS = models.FloatField(default=0, null=True)
    RESULT = models.CharField(max_length=500, blank="True")

    def categorize_wqi(self):
        fields_to_consider = [
            self.TEMP,
            self.DO,
            self.PH,
            self.COND,
            self.BOD,
            self.NITRITE,
            self.FECAL,
            self.TOTALCOLIFORM,
            self.TURB,
            self.TDS,
        ]

        si = [20, 7.25, 7.5, 1500, 4, 10, 5000, 10, 5, 300]
        denom = 0
        num = 0
        index = 0
        for field_value in fields_to_consider:
            qi = field_value / si[index]

            wi = 1 / si[index]

            if qi != 0:
                denom += wi

            num += qi * wi
            index = index + 1

        wqi = (num / denom) * 100

        if wqi >= 90:
            return "Excellent"
        elif wqi >= 70:
            return "Good"
        elif wqi >= 50:
            return "Fair"
        else:
            return "Poor"

    def save(self, *args, **kwargs):
        self.RESULT = self.categorize_wqi()
        super().save(*args, **kwargs)


class AQI(models.Model):
    STATE = models.CharField(max_length=4, primary_key=True)
    MONTH = models.IntegerField(default=0)
    PM = models.FloatField(default=0, null=True)
    RESULT = models.CharField(max_length=500, blank="True")

    def categorize_aqi(self):
        if 0 <= self.PM <= 30:
            return "Good"
        elif 31 <= self.PM <= 60:
            return "Satisfactory"
        elif 61 <= self.PM <= 90:
            return "Moderate"
        elif 91 <= self.PM <= 120:
            return "Poor"
        elif 121 <= self.PM <= 250:
            return "Very Poor"
        elif self.PM >= 251:
            return "Severe"
        else:
            return "Invalid"

    def save(self, *args, **kwargs):
        self.RESULT = self.categorize_aqi()
        super().save(*args, **kwargs)
