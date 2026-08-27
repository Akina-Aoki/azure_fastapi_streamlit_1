Video Link: https://www.youtube.com/watch?v=CzeKRM2CYiM
Github Link: https://github.com/AIgineerAB/cloud_databricks_azure_course/tree/main/15_dockerize_deploy_fastapi_streamlit



#### ** How to run the full dockerized applications backend and frontend
## Backend
- `$ cd backend/src/backend`
- `$ uv run uvicorn api:app --reload`
- Open `http://127.0.0.1:8000/pokemons/stats`


## Frontend
- Open new terminal
- $ `cd frontend/src/frontend`
- `uv run streamlit run dashboard.py`
- This will open `http://localhost:8501/`



## Running the docker container
- `docker compose up -d` * Add service name in the end if needed 


## In bash

- `docker ps`
- `docker exec -it "container id" bash`
- `docker images`
- get the backend image
- `docker run -it "image chosen" bash`
- CTRL + D to exit


# jump in to an existing running container
docker exec -it container_name bash

# if container is dead - spin up a new one interactively
docker run -it image_name bash