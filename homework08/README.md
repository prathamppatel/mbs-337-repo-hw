# Homework 08 - Demo Dashboard

A minimal Dash app demonstrating containerization, staging vs. production deployments, CI/CD pipelines, and Makefile automation.

## Setup Instructions

Run these commands from the `homework08/` directory:
```bash
cd homework08
make compose        # start production
make compose-staging  # start staging
```

## Makefile Targets

- **`make compose`** - Starts the production environment (port 8050)
- **`make compose-staging`** - Starts the staging environment (port 8051)
- **`make compose-down`** - Stops the production environment
- **`make compose-down-staging`** - Stops the staging environment

## Staging vs. Production

- **Production** (`docker-compose.yml`) runs on port 8050 and is the live, stable deployment
- **Staging** (`docker-compose-staging.yml`) runs on port 8051 and is used for testing changes before pushing to production

## GitHub Actions Workflows

### 1. `integration-test.yml`
Runs pytest automatically on every push to the repository to verify the app is responding correctly.

### 2. `push-to-registry.yml`
Automatically builds and pushes the container image to the GitHub Container Registry whenever a new tag is added to the repository.
