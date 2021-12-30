from api.api import people
from .. import db
from ..models import People
from flask_restful import Resource, reqparse, abort, fields, marshal_with

place_get_args = reqparse.RequestParser()
place_get_args.add_argument("people_id", type=str, help="people_id of the place is required", required=True)
place_get_args.add_argument("name", type=str, help="name of the place is required")
place_get_args.add_argument("gender", type=str, help="gender of the place is required")
place_get_args.add_argument("contact_number", type=str, help="contact_number of the place is required")
place_get_args.add_argument("address", type=str, help="address of the place is required")

place_put_args = reqparse.RequestParser()
place_put_args.add_argument("name", type=str, help="name of the place is required", required=True)
place_put_args.add_argument("gender", type=str, help="gender of the place is required", required=True)
place_put_args.add_argument("contact_number", type=str, help="contact_number of the place is required")
place_put_args.add_argument("address", type=str, help="address of the place is required")

place_patch_args = reqparse.RequestParser()
place_patch_args.add_argument("people_id", type=str, help="people_id of the place is required", required=True)
place_patch_args.add_argument("name", type=str, help="name of the place is required")
place_patch_args.add_argument("gender", type=str, help="gender of the place is required")
place_patch_args.add_argument("contact_number", type=str, help="contact_number of the place is required")
place_patch_args.add_argument("address", type=str, help="address of the place is required")

resource_fields = {
	'people_id': fields.String,
	'name': fields.String,
    'gender': fields.String,
    'contact_number': fields.String,
	'address': fields.String
}

class Api_of_People(Resource):
    @marshal_with(resource_fields)
    def get(self):
        args = place_get_args.parse_args()
        if args['people_id']:
            data = db.session.query(People).filter(People.people_id == args['people_id']).first()
        
        if not data:
            abort(404, message="error searching...")
        else:
            return data

    @marshal_with(resource_fields)
    def put(self):
        args = place_put_args.parse_args()
        people_id = ""
        name = args['name']
        address = args['address']
        new_place = People(people_id=people_id, name=name, address=address)
        db.session.add(new_place)
        db.session.commit()
        return new_place, 401

    @marshal_with(resource_fields)
    def patch(self):
        args = place_patch_args.parse_args()
        data = db.session.query(People).filter(People.people_id == args['people_id']).first()
        if not data:
            abort(404, message="ID doesn't exist, cannot update")
        
        if args['name']:
            data.name = args['name']
        if args['address']:
            data.address = args['address']
        
        db.session.commit()
        return data
        
    def delete(self):
        pass