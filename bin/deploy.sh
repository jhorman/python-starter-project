#!/usr/bin/env bash
set -eu

ENV=$1
ORIGIN_MAIN_COMMIT="$(git rev-parse origin/main)"
COMMIT=$(git rev-parse HEAD)
BASE_TAG=$(date -u +%Y%m%dT%H%M%S)Z-${COMMIT:0:8}

if [[ $ENV == "prod" ]]; then
  TAG=prod-$BASE_TAG
  if [[ $COMMIT != $ORIGIN_MAIN_COMMIT ]]; then
    read -p "Local commit ${COMMIT:0:8} does not match origin/main ${ORIGIN_MAIN_COMMIT:0:8} - are you sure you want to deploy to prod? " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
      echo "Deployment canceled"
      exit 1
    fi
  fi
elif [[ $ENV == "dev" ]]; then
  TAG=dev-$BASE_TAG
else
  echo "Invalid environment: ${ENV}"
  exit 1
fi

git tag -a -m $TAG $TAG &> /dev/null && git push origin refs/tags/$TAG &> /dev/null

echo "Kicked off deploy to $ENV by creating & pushing tag: $TAG"
