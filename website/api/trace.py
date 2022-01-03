from .. import db
from ..models import Trace
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import datetime as dt

trace_put_args = reqparse.RequestParser()
trace_put_args.add_argument("people_id", type=str, help="people_id of the trace is required", required=True)
trace_put_args.add_argument("place_id", type=str, help="place_id of the trace is required", required=True)

resource_fields = {
	'people_id': fields.String,
	'place_id': fields.String,
    'time': fields.DateTime,
}
class Api_Of_Trace(Resource):
    @marshal_with(resource_fields)
    def put(self):
        args = trace_put_args.parse_args()
        people_id = args['people_id']
        place_id = args['place_id']
        new_trace = Trace(people_id = people_id, place_id = place_id, time = dt.datetime.now())
        db.session.add(new_trace)
        db.session.commit()
        return new_trace