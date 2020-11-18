from app.main import ms


class PlantSchema(ms.Schema):
    class Meta:
        fields = ('plant_id', 'nama')

plantSchema = PlantSchema()
all_plantSchema = PlantSchema(many = True)
