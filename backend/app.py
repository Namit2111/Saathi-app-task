
from fastapi import FastAPI
from app import recommend  
import uvicorn
# import debugpy

# debugpy.listen(("0.0.0.0", 5678))
# print("⏳ Waiting for debugger attach...")
# debugpy.wait_for_client()



app = FastAPI(title="Recommendation System API")


app.include_router(recommend.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
