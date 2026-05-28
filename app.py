from flask import Flask, jsonify

app = Flask(__name__)


# =========================
# HOME ROUTE
# =========================

@app.route("/")
def home():

    return jsonify({
        "status": "running",
        "message": "Bot Running Successfully"
    })


# =========================
# HEALTH ROUTE
# =========================

@app.route("/health")
def health():

    return jsonify({
        "status": "ok",
        "server": "active"
    })


# =========================
# PING ROUTE
# =========================

@app.route("/ping")
def ping():

    return jsonify({
        "response": "pong"
    })


# =========================
# ERROR HANDLER
# =========================

@app.errorhandler(404)
def not_found(error):

    return jsonify({
        "error": "Route Not Found"
    }), 404


@app.errorhandler(500)
def internal_error(error):

    return jsonify({
        "error": "Internal Server Error"
    }), 500


# =========================
# MAIN
# =========================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=10000,
        debug=False
    )