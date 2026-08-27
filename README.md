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


## In bash (Optional. Kokchun showing the backend side in bash)

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


## Deploying in Azure (IMPORTANT)
- **LINK: https://www.youtube.com/watch?v=qeVT9id3eAo**
- Create resource group.
- Go in research group. Go in CREATE. CHoose container registry
- 1.png
- Wait until deployment is complete.
- 2,3 png
- VSCODE in docker yaml, 4,5 png


- In terminal log in to Azure: 
```
az --version
az acr login --name "ADD the login server from access keys in azure"
```
- Should get:
```
Registry name is 'deployaira'. The following suffix '-btangacjhacadfee.azurecr.io' is automatically omitted.
Login Succeeded
```
- Run `docker compose build`
- Result should be that frontend and backend are built.
- Check:  `docker images`
- `docker compose push` - This pushes to docker container registry
- Result: Everything should show that its pushed.
- CHeck: Go back to deploy_practice/deployaira/Repositories, should see both frontend and backend. 6.png
- Resource group - marketplace - container app create 
- 7.png, 8,9 png - next ingress
- Ingress check
- 10.png
- Create & Deploy
- check: localhost:8080/docs

- Resource group- create web app
- 11.png - Database - Container 
- **12. png (Image: Frontend, Tag: v2)**
- Resoruce  group
- web app with the world icon, ADD, 13.png
- **HERE I GOT STUCK**