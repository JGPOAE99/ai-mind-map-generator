from . import health


@health.route("/")
def health_check():
    return {"OK": True}
