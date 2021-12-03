def trigger_dag(data, context):
    """Create a task for a given queue with an arbitrary payload."""

    from google.cloud import tasks_v2
    import json

    # Create a client.
    client = tasks_v2.CloudTasksClient()

    # TODO(developer): Uncomment these lines and replace with your values.
    project = 'famous-strategy-323614'
    queue = 'airflow-task'
    location = 'us-central1'
    url = 'https://q70987809990c7076p-tp.appspot.com/api/experimental/dags/dag_storage_file_triggered/dag_runs'
    audience = '972358053884-p2n21tomap10b8vi2lue004l7uhpgoo3.apps.googleusercontent.com'
    service_account_email = 'airflow-runner@famous-strategy-323614.iam.gserviceaccount.com'
    payload = {
        'conf':
            json.dumps({
                'name': data['name']
            }),
            'run_id': data['name']
        
    }

    # Construct the fully qualified queue name.
    parent = client.queue_path(project, location, queue)

    # Construct the request body.
    task = {
        "http_request": {  # Specify the type of request.
            "http_method": tasks_v2.HttpMethod.POST,
            "url": url,  # The full url path that the task will be sent to.
            "oidc_token": {"service_account_email": service_account_email, "audience": audience},
        }
    }

    if payload is not None:
        # The API expects a payload of type bytes.
        converted_payload = json.dumps(payload).encode()

        # Add the payload to the request.
        task["http_request"]["body"] = converted_payload

    # Use the client to build and send the task.
    response = client.create_task(request={"parent": parent, "task": task})

    print("Created task {}".format(response.name))