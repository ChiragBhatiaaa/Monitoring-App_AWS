from kubernetes import client, config

config.load_kube_config()

api_client = client.ApiClient()

deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="monitoring-app"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "monitoring-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "monitoring-app"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="app-container",
                        image="211125317753.dkr.ecr.us-east-1.amazonaws.com/monitoring_app_image:latest",
                        ports=[client.V1ContainerPort(container_port=5000)]
                    )
                ]
            )
        )
    )
)


api_instance = client.AppsV1Api(api_client)
api_instance.create_namespaced_deployment(
    namespace="default",
    body=deployment
)


service = client.V1Service(
    metadata=client.V1ObjectMeta(name="my-flask-service"),
    spec=client.V1ServiceSpec(
        selector={"app": "my-flask-app"},
        ports=[client.V1ServicePort(port=5000)]
    )
)


api_instance = client.CoreV1Api(api_client)
api_instance.create_namespaced_service(
    namespace="default",
    body=service
)