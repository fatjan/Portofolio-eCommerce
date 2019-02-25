import logging, json
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from . import *
from blueprints import db
from flask_jwt_extended import jwt_required, get_jwt_claims

bp_user = Blueprint('user', __name__)
api = Api(bp_user)

class UserResource(Resource): 

    def __init__(self):
        pass
    
    @jwt_required  #for admin to see all users 
    def get(self, id=None):
        if id is None:
            parser = reqparse.RequestParser()
            parser.add_argument('p', type=int, location='args', default=1)
            parser.add_argument('rp', type=int, location='args', default=5)
            parser.add_argument('user_type', location='args')
            parser.add_argument('username', location='args')
            parser.add_argument('address', location='args')
            args = parser.parse_args()
            rumus_offset = args['p'] * args['rp'] - args['rp']
            qry = Users.query
            if args['username'] is not None:
                qry = qry.filter(Users.username.like("%"+args['username']+"%")) #for name with this name, and not case sensitive
            if args['user_type'] is not None:
                qry = qry.filter_by(name=args['user_type']) #qry that is filtered by name >> for exact name
            if args['address'] is not None:
                qry = qry.filter(Users.username.like("%"+args['address']+"%"))    
            rows = []
            for row in qry.limit(args['rp']).offset(rumus_offset).all():
                rows.append(marshal(row, Users.response_field))
            if get_jwt_claims()['user_type'] == 'admin':
                return rows, 200, {'Content-Type': 'application/json'}
            return {'message': 'Sorry, this page is not accessible'}, 404, {'Content-Type': 'application/json'}
        else:
            qry = Users.query.get(id) #select * from where id = id
            if qry != None and id == get_jwt_claims()['id']:
                return marshal(qry, Users.response_field), 200, {'Content-Type': 'application/json'}   
            return {'status': 'not found', 'message': 'you can only see your profile details'}, 404, {'Content-Type': 'application/json'}
            #penjual and publik can only see their own user profile

    def post(self): #for everyone to register and login        
        parser = reqparse.RequestParser()
        parser.add_argument('user_type', location='args')
        parser.add_argument('username', location='json')
        parser.add_argument('password', location='json')
        parser.add_argument('address', location='json')
        args = parser.parse_args() #this becomes str_serialized
        if args['user_type'] is None:
            args['user_type'] = 'publik'
        user_new = Users(None, args['user_type'], args['username'], args['password'], args['address'])
        db.session.add(user_new) #insert the input data into the database
        db.session.commit() 
        return marshal(user_new, Users.response_field)   
    
    @jwt_required #if user wants to change their profile details
    #admin can only edit user's profile if needed.
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('username', location='json')
        parser.add_argument('password', location='json')
        parser.add_argument('address', location='json')
        args = parser.parse_args()
        qry_user = Users.query.get(id)
        if qry_user is not None and get_jwt_claims['id'] == id or get_jwt_claims['user_type'] == 'admin':
            # if args['username'] is not None:
            qry_user.username = args['username']
            # if args['password'] is not None:
            qry_user.password = args['password']
            # if args['address'] is not None:
            qry_user.address = args['address']
            db.session.commit()
            return marshal(qry_user, Users.response_field), 200, {'Content-Type': 'application/json'}
        return 'Data with that id number is not found', 404, {'Content-Type': 'application/json'}

    @jwt_required #only for admin if any users do some violation of use.  
    def delete(self, id):
        qry_del = Users.query.get(id)
        if qry_del is not None:
            db.session.delete(qry_del)
            db.session.commit()
            return 'user with id = %d has been deleted' % id, 200, {'Content-Type': 'application/json'}
        return {'status': 'ID_IS_NOT_FOUND'}, 404, {'Content-Type': 'application/json'}
        
    def patch(self):
        return 'Not yet implemented', 501

api.add_resource(UserResource, '', '/<int:id>')
