from api.api import people
from .. import db
from ..models import Place
from flask_restful import Resource, reqparse, abort, fields, marshal_with

place_patch_args = reqparse.RequestParser()
place_patch_args.add_argument("place_id", type=str, help="place_id of the place is required", required=True)
place_patch_args.add_argument("place_name", type=str, help="place_name of the place is required")
place_patch_args.add_argument("address", type=str, help="address of the place is required")

place_get_args = reqparse.RequestParser()
place_get_args.add_argument("place_id", type=str, help="place_id of the place is required")
place_get_args.add_argument("place_name", type=str, help="place_name of the place is required")
place_get_args.add_argument("address", type=str, help="address of the place is required")

place_put_args = reqparse.RequestParser()
place_put_args.add_argument("place_name", type=str, help="place_name of the place is required", required=True)
place_put_args.add_argument("address", type=str, help="address of the place is required", required=True)

resource_fields = {
	'place_id': fields.String,
	'place_name': fields.String,
	'address': fields.String
}

class Api_of_Place(Resource):
    @marshal_with(resource_fields)
    def get(self):
        args = place_get_args.parse_args()
        if args['place_id']:
            data = db.session.query(Place).filter(Place.place_id == args['place_id']).all()
        
        if not data:
            abort(404, message="error searching...")
        else:
            return data

    @marshal_with(resource_fields)
    def put(self):
        args = place_put_args.parse_args()
        place_id = ""
        place_name = args['place_name']
        address = args['address']
        new_place = Place(place_id=place_id, place_name=place_name, address=address)
        db.session.add(new_place)
        db.session.commit()
        return new_place, 401

    @marshal_with(resource_fields)
    def patch(self):
        args = place_patch_args.parse_args()
        data = db.session.query(Place).filter(Place.place_id == args['place_id']).first()
        if not data:
            abort(404, message="ID doesn't exist, cannot update")
        
        if args['place_name']:
            data.place_name = args['place_name']
        if args['address']:
            data.address = args['address']
        
        db.session.commit()
        return data
        
    def delete(self):
        pass