broker_url = "redis://:H733Kdjndks81@127.0.0.1:6379/0"

# # broker_url = "redis://:H733Kdjndks81@192.168.0.101:6379/0"
# broker_transport_options = {'master_name': "mymaster"}
# result_backend_transport_options = {'master_name': "mymaster"}

imports = [
    'tasks.server',
]

worker_concurrency = 10

broker_transport_options = {'visibility_timeout': 100}

worker_prefetch_multiplier = 1
task_acks_late = True
task_reject_on_worker_lost = True
# task_time_limit = 10
