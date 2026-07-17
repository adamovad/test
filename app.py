# this is  version 1.2


from fastapi import FastAPI

import uvicorn

app = FastAPI()

app.get("")
def health_check();
        return{
                "healthy":True
        }

if __name__ == "__main__":
        uvicorn.run("main:app",host="127.0.0.1", port=8000, reload=True)ַ