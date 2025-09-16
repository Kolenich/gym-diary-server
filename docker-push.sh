#!/bin/sh

docker build -t server .
docker tag server kolenich/diary:server
docker push kolenich/diary:server