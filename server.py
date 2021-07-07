#!/bin/env python3
import uvicorn

if __name__ == "__main__":
	_HOST="localhost"
	_PORT=28080
	_APP="ex:app"
	uvicorn.run(_APP,host=_HOST,port=_PORT,reload=True,root_path=".")
