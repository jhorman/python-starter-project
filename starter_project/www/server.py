import logging
from datetime import timedelta

from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware

from starter_project.www.status import status_router

logger = logging.getLogger("starter_project.api.server")

app = FastAPI(
    middleware=[
        Middleware(
            CORSMiddleware,
            allow_origins="*",
            allow_methods="*",
            allow_headers="*",
            allow_credentials=True,
            max_age=timedelta(weeks=1).total_seconds(),
        ),
        Middleware(GZipMiddleware, minimum_size=1024),
    ],
    debug=True,
    openapi_url=None,
)

app.include_router(status_router, tags=["Status"], prefix="/status")
