import os
from os import urandom
from fastapi import FastAPI, status, HTTPException
from jose import JWTError, jwt
from pydantic import BaseModel
from datetime import datetime, timedelta, date
from base64 import b64encode

SECRET_KEY = "a9ddbcaba8c0ac1a0a812dc0c2f08514b23f2db0a68343cb8199ebb38a6d91e4ebfb378e22ad39c2d01d0b4ec9c34aa91056862ddace3fbbd6852ee60c36acbf"

ALGORITHM = "HS512"

class Token(BaseModel):
	access_token: str
	token_type: str

app = FastAPI()

def generate_jwt_token(data: dict):
	to_encode = data.copy()
	
	req_timestamp = datetime.utcnow()
	to_encode.update({"iat": req_timestamp})

	random_bytes = urandom(64)
	nonce = b64encode(random_bytes).decode('utf-8')
	to_encode.update({"jti": nonce})
	
	encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
	
	return encoded_jwt

# the endpoint to generat JWT token
@app.get("/get-token")
async def get_token(q: str):

	today = date.today()
	data = { "payload": {
				"data": q, 
				"date": str(today)
			}
		}
	token = generate_jwt_token(data=data)
	return {"jwt-token": token}

# the endpoint to verify JWT token
@app.get("/verify-token")
async def verify_token(token: str):
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		return payload
	except JWTError:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="JWT Token Validation Failed",
		)
