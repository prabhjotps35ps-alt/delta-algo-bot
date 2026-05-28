from flask import Flask
from flask import jsonify
from flask import render_template_string

from quantum_master_controller import (
    QuantumMasterController
)

app = Flask(__name__)

controller = (
    QuantumMasterController()
)

# =========================
# HTML DASHBOARD
# =========================

dashboard_html = """

<!DOCTYPE html>
<html>

<head>

<title>
OMEGA INSTITUTIONAL DASHBOARD
</title>

<style>

body {

    background-color: #0f172a;

    color: white;

    font-family: Arial;

    padding: 20px;

}

.card {

    background: #1e293b;

    padding: 20px;

    border-radius: 12px;

    margin-bottom: 20px;

}

.title {

    font-size: 24px;

    font-weight: bold;

    margin-bottom: 10px;

}

.value {

    font-size: 20px;

    color: #38bdf8;

}

.status {

    color: #4ade80;

}

.warning {

    color: #facc15;

}

.danger {

    color: #ef4444;

}

</style>

</head>

<body>

<h1>
OMEGA AI INSTITUTIONAL DASHBOARD
</h1>

<div class="card">

<div class="title">
MASTER MODE
</div>

<div class="value">
{{mode}}
</div>

</div>

<div class="card">

<div class="title">
LAST SIGNAL
</div>

<div class="value">
{{signal}}
</div>

</div>

<div class="card">

<div class="title">
TOTAL CYCLES
</div>

<div class="value">
{{cycles}}
</div>

</div>

<div class="card">

<div class="title">
SYSTEM STATUS
</div>

<div class="status">
ACTIVE
</div>

</div>

</body>

</html>

"""

# =========================
# DASHBOARD HOME
# =========================

@app.route("/")
def dashboard():

    return render_template_string(

        dashboard_html,

        mode=controller.master_mode,

        signal=controller.last_signal,

        cycles=controller.cycle_count

    )

# =========================
# API STATUS
# =========================

@app.route("/api/status")
def api_status():

    return jsonify({

        "mode":
        controller.master_mode,

        "last_signal":
        controller.last_signal,

        "cycles":
        controller.cycle_count,

        "active":
        controller.active

    })

# =========================
# AI DRIVERS
# =========================

@app.route("/api/drivers")
def drivers():

    try:

        report = (
            controller.driver_engine()
        )

        return jsonify(report)

    except Exception as e:

        return jsonify({

            "error":
            str(e)

        })

# =========================
# AUTO TEST REPORT
# =========================

@app.route("/api/tests")
def tests():

    try:

        report = (
            controller.auto_test_engine()
        )

        return jsonify(report)

    except Exception as e:

        return jsonify({

            "error":
            str(e)

        })

# =========================
# START DASHBOARD
# =========================

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5050,

        debug=False

    )