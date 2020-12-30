## BASE IMAGE
FROM nginx:1.18 AS BUILDER

## IMAGE METADATA
LABEL Maintainer="Peter Keech <pkeech@ngds.com>"

## IMAGE DEPENDENCIES
FROM Builder AS Dependencies
RUN apt-get update && apt-get upgrade -y
COPY nginx.conf /etc/nginx/nginx.conf

## DEV IMAGE
FROM Dependencies AS Development

## TEST IMAGE
FROM Dependencies AS Test

## PRODUCTION IMAGE
FROM Dependencies AS Production