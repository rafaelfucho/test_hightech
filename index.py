#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 14:30:48 2020

@author: ralvarez
"""

from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_restful import Resource, Api

client = MongoClient('localhost', 27017)
db = client.prueba

app = Flask(__name__)
api = Api(app)



class Usuario(Resource):
    def get(self):
        data=[]
        for post in db.usuario.find({}, {"_id":0}):
            data.append(post)
        result = {'data': data}
        return jsonify(result)
    
    def post(self):
        valida = db.token.find_one()
        token = valida['token']
        if token == request.json['token']:
            nombre = request.json['nombre']
            apellido = request.json['apellido']
            tdc = request.json['tdc']
            post = {"id": db.usuario.find().count()+1,
                    "nombre": nombre,
                    "apellido": apellido,
                    "tdc": tdc}
            post_id = db.usuario.insert_one(post).inserted_id
            return {'status': 'Nuevo Usuario añadido'}
        else:
            return {'status': 'token invalido'}
    
class UsuarioData(Resource):
    def get(self, usuarioid):
        data=[]
        id_user ={'id': int(usuarioid)}
        for post in db.usuario.find(id_user, {"_id":0}):
            data.append(post)
        result = {'data': data}
        return jsonify(result)

    def put(self, usuarioid):
        valida = db.token.find_one()
        token = valida['token']
        if token == request.json['token']:
            nombre = request.json['nombre']
            apellido = request.json['apellido']
            tdc = request.json['tdc']
            id_user ={'id': int(usuarioid)}
            post = { "$set": {"nombre": nombre,
                    "apellido": apellido,
                    "tdc": tdc} }
            post_id = db.usuario.update_one(id_user, post )
            return {'status': 'Usuario editado'}
        
        else:
            return {'status': 'token invalido'}
   


api.add_resource(Usuario, '/usuario')  
api.add_resource(UsuarioData, '/usuario/<usuarioid>')

if __name__ == '__main__':
     app.run(port='5000')