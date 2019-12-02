import os
from bottle import route, run, Bottle
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn=os.environ.get("SENTRY"),
    integrations=[BottleIntegration()]
)

app = Bottle()
@app.route("/success")
def success():
    return


@app.route("/fail")
def fail():
    raise RuntimeError
    return


if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8081, debug=True)
