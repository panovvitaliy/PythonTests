import json
from marshmallow import Schema, fields, validate


class CategorySchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)


class TagSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)


class PetSchema(Schema):
    id = fields.Int(required=True)
    category = fields.Nested(CategorySchema, required=True)
    name = fields.Str(required=True)
    photoUrls = fields.List(fields.Str(), required=True)
    tags = fields.List(fields.Nested(TagSchema), required=True)
    status = fields.Str(required=True, validate=validate.OneOf(["available", "sold"]))


if __name__ == '__main__':
    # Read data from the JSON file
    with open('pets.json', 'r') as file:
        data = json.load(file)

    # Validate the data using the schema
    pets_dto = PetSchema(many=True).load(data)

    # Print information about each pet
    for pet in pets_dto:
        tags = [tag['name'] for tag in pet['tags']]
        print(pet['name'], pet['category']['name'], tags)
