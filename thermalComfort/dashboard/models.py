from django.db import models


class Floor(models.Model):
    code = models.CharField('Code', max_length=12)
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'floor'
        verbose_name_plural = 'Floors'


class Room(models.Model):
    code = models.CharField('Code', max_length=12)
    name = models.CharField('Name', max_length=50)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE,
                              related_name='rooms')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'room'
        verbose_name_plural = 'Rooms'


class Measurement(models.Model):
    name = models.CharField('Name', max_length=50)
    unit = models.CharField('Unit', max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'measurement'
        verbose_name_plural = 'Measurements'


class Sensor(models.Model):
    code = models.CharField('Code', max_length=12)
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE,
                                    related_name='sensors')
    room = models.ForeignKey(Room, on_delete=models.CASCADE,
                             related_name='sensors', null=True)

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'sensor'
        verbose_name_plural = 'Sensors'


class RealTimeData(models.Model):
    date = models.DateTimeField('DateTime', auto_now_add=True)
    value = models.DecimalField('Value', max_digits=5, decimal_places=2,
                                default=0.00)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE,
                               related_name='realtimedata')

    def __str__(self):
        return str(self.sensor.code) + ': ' + str(self.date)

    class Meta:
        db_table = 'realtimedata'
        verbose_name_plural = 'RealTimeData'


class ConsolidatedData(models.Model):
    dateInit = models.DateTimeField('Initial DateTime', auto_now_add=True)
    dateEnd = models.DateTimeField('Final DateTime', auto_now_add=True)
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE,
                                    related_name='consolidateddata')
    room = models.ForeignKey(Room, on_delete=models.CASCADE,
                             related_name='consolidateddata')

    def __str__(self):
        return str(self.sensor.code) + ': ' + str(self.date)

    class Meta:
        db_table = 'consolidateddata'
        verbose_name_plural = 'ConsolidatedData'
