from app.main.models import Plant, Sensor, Telemetry, Connector
from app.main import db

def save_newplant(data):
    plant = Plant.query.filter_by(plant_id = data['plant_id']).first()
    if not plant:
        new_plant = Plant(**data)
        save_change(new_plant)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201

    else:
        response_object={
            'status':'fail',
            'message': 'gagal input, Plant telah ada'

        }
        return response_object, 409

def query_all(tab):
    return tab.query.all()


def query_plant(id):
    res = Plant.query.filter_by(plant_id=id).first()
    return res



def save_change(data):
    db.session.add(data)
    db.session.commit()