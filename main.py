from fastapi import FastAPI
import uvicorn

app = FastAPI(title="CCSolutions.io Helloworld Application",
              description="For educations purposes",
              version="0.0.1")


@app.on_event("startup")
async def startup_event():
    print("-----> Hello World!")
    print("""
          #####   #####   #####                                                                 
          #     # #     # #     #  ####  #      #    # ##### #  ####  #    #  ####      #  ####  
          #       #       #       #    # #      #    #   #   # #    # ##   # #          # #    # 
          #       #        #####  #    # #      #    #   #   # #    # # #  #  ####      # #    # 
          #       #             # #    # #      #    #   #   # #    # #  # #      #     # #    # 
          #     # #     # #     # #    # #      #    #   #   # #    # #   ## #    # ### # #    # 
          #####   #####   #####   #####  ######  ####    #   #  ####  #    #  ####  ### #  #### 
          """)


@app.get("/")
async def root():
    return {"message": "CCSolutions.io says hello!"}

@app.get("/helloworld")
async def root():
    return {"message": "Hello World!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=False)