# Features

## At a glance

- Modular approach so modules can be shared accross different apps
- Postgres DB connection
- JWT authentication / authorization
- RBAC (Role based access control)
- Emails with Jinja2 templates
- Slack notifications via Webhooks
- (Response) caching with Redis
- Alembic for database migrations
- Logger configuration
- CORS
- A Typer based cli
- Ready to use scripts for creating and importing database backups.
- Unit testing with Pytest.
- Dockerization
- Production ready: Gitlab CI/CD different docker-compose settings for dev & prod out of the box.

The main functionality of the repo lies in the `/app/core` directory. This way, you have visual and logical separation of the base features and the custom functionality you are going to implement yourself.

## FastAPI as the API engine

This template is based on FastAPI. For more information see [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com)

## Modular approach

The code is organized into modules in order to make things reusable accross projects. For example, all the code belonging to user logic (models, routes, services etc.) live in the `/app/core/user` direction. Similarly, code related to security lies in `/app/core/security`.

## Dockerization

The app is comletely dockerized. You of course don't have to use the provided Dockerfiles and docker-compose files. However, to get the most out of this repo, you should use them because many scripts (like those for database dumps) rely on the Docker approach.

You might see that there are multiple `docker-compose` files. This is for the separation of development and production environments (more on that later on).
For starters, you can execute the `scripts/start-dev.sh` file. That way you can be sure to boot up the correct containers for local development.

## Postgres database

This repo uses Postgres as its database. The connection settings are configured under `/app/core/db/db`.

## Alembic for database migrations

For managing database migrations, this template takes advantage of `alembic`. It comes preconfigured to connect to your database immediately.

## JWT authentication

The repo comes with the logic for creating / managing users out of the box. But not only that! It also brings to you JWT based authentication and authorization.

## Role based access control (RBAC)

You can also grant / deny access to specific resources more granularly by taking advantage of the role based access control (RBAC) that this repo delivers. You can give your users roles and allow access to endpoints based on those.

## Caching

We provide you with a redis container that the app automatically connects to (via the default environment variables). You can use it to cache specific things and even resonses.

## Notifications via Email and Slack

You can send notifications to your users via email and Slack.

Use Jinja2 templates to send rich HTML emails to your users. For example, send emails to new users in order to verify their mail address.

Send notifications to your team via Slack via Webhooks.

## Logger preconfigured

The native Pyhton logging functionality comes preconfigured in order to log to a file of your choice instead of the console.

## A CLI to interact with your app

Sometimes you don't want to interact with your app via a REST endpoint but via the console. That's why the template comes with a CLI baked in that you can extend to your needs as your app grows.
For example, you can execute `python cli user seed-super-user` to create a new super user.

## Database backups

The cli described above comes with predefined commands to create and import database backups. For example `python cli db create-dump --container-name <MY_PG_CONTAINER>` will create a sql dump of your local database for you. It's that easy!

## Unit Testing with Pytest

Unit testing with Pytest is preconfigured for you with all the scaffolding necessary to test your api endpoints as well as isolated methods.

## Gitlab CI/CD pipeline

There is a `.gitlab-ci.yml` file you can utilize for you CI/CD pipeline.

## Production ready Docker swarm mode configuration for Traefik

There are multiple `docker-compose` files that serve the different requirements between development and production environments.
The production environment is set up to work in Docker swarm mode with Traefik as an HTTPS provider and load balancer. Visit [https://dockerswarm.rocks/](https://dockerswarm.rocks/) to set up Docker in Swarm Mode with Traefik.

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
