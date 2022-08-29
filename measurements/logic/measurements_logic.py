from ..models import Measurement

def get_measurements():
    measurements=Measurement.objects.all()
    return measurements
    
def get_measurement(measurement_pk):
    measurement=Measurement.objects.get(pk=measurement_pk)
    return measurement

def create_measurement(new_measurement):
    measurement = Measurement(variable=new_measurement["variable"],value=new_measurement["value"],
    unit=new_measurement["unit"],place=new_measurement["place"])
    measurement.save()
    return measurement

def update_measurement(measurement_pk, new_measurement):
    measurement=get_measurement(measurement_pk)
    measurement.variable=new_measurement["variable"]
    measurement.value=new_measurement["value"]
    measurement.unit=new_measurement["unit"]
    measurement.place=new_measurement["place"]
    measurement.save()
    return measurement

def delete_measurement(measurement_pk):
    measurement=get_measurement(measurement_pk)
    measurement.delete()
    return measurement
