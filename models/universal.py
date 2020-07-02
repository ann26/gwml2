from django.contrib.gis.db import models


class Quantity(models.Model):
    """ Model to define quantity. """
    value = models.FloatField(
        null=True, blank=True)
    unit = models.TextField(
        null=True, blank=True)

    def __str__(self):
        return '{} ({})'.format(self.value, self.unit)


class GWTerm(models.Model):
    """ Abstract model for Term """
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class PositionalAccuracyType(GWTerm):
    """Description of the accuracy of the elevation measurement."""

    pass


class ElevationMeasurementMethodType(GWTerm):
    """Method used to measure the elevation, e.g. GPS, Survey, DEM, etc."""

    pass


class ElevationTypeTerm(GWTerm):
    """Type of reference elevation, defined as a feature, e.g. Top of Casing, Ground, etc."""

    pass


class Elevation(models.Model):
    """
    7.6.2 Elevation
    Elevation of a feature in reference to a datum.

    """

    elevation = models.PointField(
        null=False, blank=False, verbose_name="elevation",
        help_text="Numeric value, coordinate reference system (CRS), "
                  "and unit of measure (UoM) for the elevation.")
    elevation_accuracy = models.ForeignKey(
        PositionalAccuracyType, null=True, blank=True,
        on_delete=models.SET_NULL, verbose_name="elevationAccuracy",
        help_text="Description of the accuracy of the elevation measurement.")
    elevation_measurement_method = models.ForeignKey(
        ElevationMeasurementMethodType, null=True, blank=True,
        on_delete=models.SET_NULL, verbose_name="elevationMeasurementMethod",
        help_text="Description of the accuracy of the elevation measurement.")
    elevation_type = models.ForeignKey(
        ElevationTypeTerm, null=True, blank=True,
        on_delete=models.SET_NULL, verbose_name="elevationType",
        help_text="Type of reference elevation, defined as a feature, e.g. Top of Casing, Ground, etc.")
