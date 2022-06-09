# Features

- Postgres DB connection
- JWT authentication / authorization
- Emails with Jinja2 templates
- Caching with redis
- Response caching
- Alembic for database migrations
- Logger configuration
- CORS
- Dockerized
- Production ready: Gitlab CI/CD different docker-compose settings for dev & prod out of the box.

# Checklist

- Create a virtual environment:

```
python3 -m venv
```

- Install dependencies:

```
pip install -r requirements.txt
```

- In `docker-compose.dev.yml` and `docker-compose.prod.yml` rename images, networks and volumes according to your needs.
- Execute:

```
cp .env .env.example
```

and fill in the values in `.env` according to your needs.

- In `.gitlab-ci.yml` make sure you point to the correct images
- Make sure that all files in the scripts directory are executable:

```
chmod +x ./scripts/filename
```

- Double check that your environment variables match your docker-compose configuration.
- Make sure that all your environment variables are taken into account under `./scripts/generate-env.sh`
- Make sure that you have all environment variables also stored in Gitlab. This is because during the CI/CD pipeline, `./scripts/generate-env.sh` will be executed and search for all the environment variables in Gitlab.
- Boot your development environment by executing:

```
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
```

- After the first build, you can start your development environment by executing

```
./scripts/start-dev.sh
```

- (Optional) In `.vscode/launch.json` change the ports according to your needs.
- (Optional) Change the file output in `logger.conf` according to your needs.
- Execute:

```
alembic upgrade head
```

to execute all outstanding database migrations.
