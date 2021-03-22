# Amelia Musical Playhouse Static API

[![Netlify Status](https://api.netlify.com/api/v1/badges/3241152b-de8b-4096-a78b-a306b126adb7/deploy-status)](https://app.netlify.com/sites/plaehaus-amp-static-api-478f0e/deploys)

At build time, fetch a list of "upcoming productions" from a Wordpress site `graphql` endpoint, and save the response in a JSON file. A build is trigerred whenever a post is saved on the WordPress site.

## Why?

This static API allows website data to be served from a fast Netlify CDN instead of an underpowered WordPress website. This works well because the data in question does not change too often, and the few seconds it takes to rebuild the static API seems an acceptable trade-off whenever data changes.

## Build Command

```
python3 build.py
```

## Publish Directory

```
data
```

## Environment Variables

- `AMP_STATIC_API_GRAPHQL_URI`

## Generated JSON File

https://plaehaus-amp-static-api-478f0e.netlify.app/upcoming-productions.json
