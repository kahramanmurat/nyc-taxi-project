### Running Postgres with Docker

#### Linux and MacOS

```
docker run -d \
	-e POSTGRES_USER="" \
    -e POSTGRES_PASSWORD="" \
	-e POSTGRES_DB="ny-taxi" \
	-v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
	postgres:13
```