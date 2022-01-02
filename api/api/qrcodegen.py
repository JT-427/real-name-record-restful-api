from .. import db
from ..models import People
from flask_restful import Resource, reqparse, abort, fields, marshal_with

people_post_args = reqparse.RequestParser()
people_post_args.add_argument("people_id", type=str, help="place_id of the place is required", required=True)
# place_post_args.add_argument("place_name", type=str, help="place_name of the place is required")
# place_post_args.add_argument("address", type=str, help="address of the place is required")

class qrcode_gen(Resource):
    def post(self):
        args = people_post_args.parse_args()
        p = db.session.query(People).filter(People.people_id == args['people_id']).first()
        if p:
            import qrcode # 匯入模組
            img = qrcode.make(p.people_id) # QRCode資訊
            img.save(f"./qrcode/{p.name}.png") # 儲存圖片
        return