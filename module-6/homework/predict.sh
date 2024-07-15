#!/usr/bin/env bash
export AWS_ACCESS_KEY_ID="dummy"
export AWS_SECRET_ACCESS_KEY="dummy"
export AWS_DEFAULT_REGION="us-east-1"
export INPUT_FILE_PATTERN="s3://nyc-duration/in/{year:04d}-{month:02d}.parquet"
export OUTPUT_FILE_PATTERN="s3://nyc-duration/out/{year:04d}-{month:02d}.parquet"
export S3_ENDPOINT_URL="http://localhost:4566"

docker-compose up -d
sleep 5
aws  s3 mb s3://nyc-duration --endpoint-url=${S3_ENDPOINT_URL}
sleep 5
pipenv run python integration_test/batch_q5.py 2023 01
pipenv run python batch_q6.py
sleep 5

ERROR_CODE=$?
if [ ${ERROR_CODE} != 0 ]; then
    docker-compose logs
    docker-compose down
    exit ${ERROR_CODE}
fi

echo "SUCCESS"
docker-compose down