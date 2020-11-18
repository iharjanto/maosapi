from flask import Blueprint
from .schema import all_plantSchema, plantSchema
from .service import query_all
from .models import Plant, Telemetry, Connector, Sensor

exbp = Blueprint('api', __name__)

table_list = {
    'plant': Plant,
    'sensor': Sensor,
    'connector': Connector
}
@exbp.route('/plant/')
def plants():
    all = Plant.query.all()
    return all_plantSchema.dumps(all)

@exbp.route('/plant/<id>')
def get_plant(id):
    p = Plant.query.filter_by(plant_id=id).first()
    return plantSchema.dumps(p)

