from fastapi import FastAPI,Request

app = FastAPI()

async def basic_header(request:Request):
	print(request.form)
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
	response["body"] = body
	form = await request.form()
	response["form"] = form
	response["method"] = request.method
	response["client"] = request.client
	response["cookies"] = request.cookies
	response["query_params"] = request.query_params
	response["path_params"] = request.path_params
	return response

@app.get("/header")
async def get_header(request:Request):
	return await basic_header(request)

@app.post("/header")
async def post_header(request:Request):
	return await basic_header(request)

#@app.head("/header")
#async def head_header(request:Request):
#	return await basic_header(request)
