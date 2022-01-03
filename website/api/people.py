from .. import db
from ..models import People
from flask_restful import Resource, reqparse, abort, fields, marshal_with

people_get_args = reqparse.RequestParser()
people_get_args.add_argument("people_id", type=str, help="people_id of the people is required", required=True)
people_get_args.add_argument("name", type=str, help="name of the people is required")
people_get_args.add_argument("gender", type=str, help="gender of the people is required")
people_get_args.add_argument("contact_number", type=str, help="contact_number of the people is required")
people_get_args.add_argument("address", type=str, help="address of the people is required")

people_put_args = reqparse.RequestParser()
people_put_args.add_argument("name", type=str, help="name of the people is required", required=True)
people_put_args.add_argument("gender", type=str, help="gender of the people is required", required=True)
people_put_args.add_argument("contact_number", type=str, help="contact_number of the people is required")
people_put_args.add_argument("address", type=str, help="address of the people is required")

people_patch_args = reqparse.RequestParser()
people_patch_args.add_argument("people_id", type=str, help="people_id of the people is required", required=True)
people_patch_args.add_argument("name", type=str, help="name of the people is required")
people_patch_args.add_argument("gender", type=str, help="gender of the people is required")
people_patch_args.add_argument("contact_number", type=str, help="contact_number of the people is required")
people_patch_args.add_argument("address", type=str, help="address of the people is required")

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
        args = people_get_args.parse_args()
        if args['people_id']:
            data = db.session.query(People).filter(People.people_id == args['people_id']).first()
        
        if not data:
            abort(404, message="error searching...")
        else:
            return data

    @marshal_with(resource_fields)
    def put(self):
        args = people_put_args.parse_args()

        import string
        import random
        length_of_string = 32
        while True:
            people_id = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
            check = db.session.query(People).filter(People.people_id == people_id).first()
            if not check:
                break

        new_people = People(
            people_id=people_id,
            name=args['name'],
            gender=args['gender'],
            contact_number=args['contact_number'],
            address=args['address']
            )
        db.session.add(new_people)
        db.session.commit()
        return new_people, 401

    @marshal_with(resource_fields)
    def patch(self):
        args = people_patch_args.parse_args()
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