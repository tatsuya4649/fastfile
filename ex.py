from fastapi import FastAPI,Request,File,UploadFile
from typing import List
from io import BytesIO
from PIL import Image,ImageOps

app = FastAPI()

async def basic_header(request:Request):
	response = dict()
	response["request"] = dict()
	resreq = response["request"]
	resreq["dir_request"] = list()
	for req in dir(request):
		resreq["dir_request"].append(req)
	resreq["headers"] = dict()
	for key,value in zip(request.headers.keys(),request.headers.values()):
		resreq["headers"][key] = value
	body = await request.body()
	if body.__class__ != bytes:
		response["body"] = body
	form = await request.form()
	response["form"] = form
	response["method"] = request.method
	response["client"] = request.client
	response["cookies"] = request.cookies
	response["query_params"] = request.query_params
	response["path_params"] = request.path_params
	response["url"] = request.url
	return response

@app.get("/header")
async def get_header(request:Request):
	return await basic_header(request)

@app.post("/header")
async def post_header(request:Request):
	return await basic_header(request)

@app.head("/header")
async def head_header(request:Request):
	pass

async def image_header(request:Request):
	response = dict()
	response["request"] = dict()
	resreq = response["request"]
	resreq["dir_request"] = list()
	for req in dir(request):
		resreq["dir_request"].append(req)
	resreq["headers"] = dict()
	for key,value in zip(request.headers.keys(),request.headers.values()):
		resreq["headers"][key] = value
	try:
		body = await request.body()
		if body.__class__ != bytes:
			response["body"] = body
	except:
		pass
	form = await request.form()
	response["form"] = form
	response["method"] = request.method
	response["client"] = request.client
	response["cookies"] = request.cookies
	response["query_params"] = request.query_params
	response["path_params"] = request.path_params
	response["url"] = request.url
	return response

@app.post("/image")
async def post_image(request: Request,image: UploadFile = File(...)):
	byte = await image.read()
	image = Image.open(BytesIO(byte))
	image.show()
	return await image_header(request)

@app.head("/image")
async def head_image(request:Request):
	pass
