# hw28 (avito)

## run database (docker)
```shell
docker run \
    --name hw28_db \
    -e POSTRES_PASSWORD=password \
    -e POSTGRES_USER=user \
    -e POSTGRES_DB=hw28 \
    -p 5432:5432 \
    postgres:13.0-alpine
'''