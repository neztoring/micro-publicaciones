from flask import Flask, request
import json
from service import create_post
from datetime import datetime
import re



app = Flask(__name__)



# Public Endpoints
@app.route('/posts', methods = ['GET','POST'])
def createpost():
    if request.method == 'POST':
        try:
            routeId = request.json["routeId"] 
            expireAt = request.json["expireAt"] 
            
            if routeId == "" or expireAt == "" :
                raise Exception("Campos vacios")
            
            int(routeId)   

            regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$'
            match_iso8601 = re.compile(regex).match
            if match_iso8601( expireAt ) is None:
                raise Exception("Fecha no cunmple ISO")
            

            fecha=datetime.strptime(expireAt, '%Y-%m-%dT%H:%M:%S.%f%z')
            if fecha <= datetime.now():
                raise Exception("La fecha no es futura")

            #datetime.fromisoformat(expireAt)


        except Exception as e:
            print(e)    
            return "",400

        return create_post(request)
    else:
        return {"respuesta":'Opción GET'},201
    