bind = ["0.0.0.0:8000"]
worker_class = "uvicorn.workers.UvicornWorker"
workers = 1
errorlog = "-"
loglevel = "error"
keepalive = 600


def pre_fork(server, worker):
    import starter_project  # noqa: F401
