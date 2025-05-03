from flask import Flask, render_template, request, jsonify
from logic import run_task, count_threads, count_processes
from monitor import get_stats
from memory_share import memory_sharing_demo
from ipc_demo import ipc_demo_run

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = {}
    if request.method == "POST":
        method = request.form["method"]
        task_type = request.form["task"]

        time_taken = run_task(method, task_type)
        cpu, mem = get_stats()

        # Count threads/processes created
        threads = count_threads()
        processes = count_processes()

        result = {
            "method": method.title(),
            "task": task_type.upper(),
            "time": f"{time_taken}s",
            "cpu": f"{cpu}%",
            "mem": f"{mem} MB",
            "threads": threads,
            "processes": processes
        }

    return render_template("index.html", result=result)

@app.route("/memory_sharing")
def memory_demo():
    shared_memory_result = memory_sharing_demo()
    return jsonify(shared_memory_result)

@app.route("/ipc")
def ipc_demo():
    ipc_result = ipc_demo_run()
    return jsonify(ipc_result)

if __name__ == "__main__":
    app.run(debug=True)
