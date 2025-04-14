from prometheus_client import start_http_server, Counter
import threading

# Example metric
TASK_EXECUTIONS = Counter("airflow_task_executions", "Number of task executions", ["task_name"])

# Start a separate thread that runs the Prometheus metrics server
def start_metrics_server(port=8793):
    def run():
        start_http_server(port)
    threading.Thread(target=run, daemon=True).start()
