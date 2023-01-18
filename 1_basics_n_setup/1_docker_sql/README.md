### Running Postgres with Docker

#### Linux and MacOS

```
docker run -it \
	-e POSTGRES_USER="" \
    -e POSTGRES_PASSWORD="" \
	-e POSTGRES_DB="ny_taxi" \
	-v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
	postgres:13
```

#### CLI for Postgres

##### Installing pgcli

```
pip install pgcli
```

##### Using pgcli to connect to Postgres

```
pgcli -h localhost -p 5432 -u root -d ny_taxi
```

```
pgcli -h localhost -p 5432 -u root -d ny_taxi
```

##### Download Data

```
wget https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/yellow
```
convert to csv with gunzip:

```gunzip yellow_tripdata_2021-01.csv.gz
```


