# Python Monitoring App from Local to AWS Deployment: A Dockerized Journey

Description:

This project delves into the fascinating realm of monitoring system health using Python's psutil module, followed by an adventurous expedition into the world of Docker containers and Amazon Web Services (AWS) deployment. 
It chronicles the journey of crafting a Python application that:

- Monitors CPU Usage and Memory Utilization: Leverages the power of psutil to gather real-time insights into your system's resource consumption.
- Embraces Dockerization: Encapsulates the application within a Docker container, ensuring portability and consistency across diverse environments.
- Navigates the ECS Terrain: Utilizes the AWS CLI and boto3 module to seamlessly push the Docker image to AWS Elastic Container Service (ECS).
- Unveils the EKS Landscape: Deploys the application onto an Amazon Elastic Kubernetes Service (EKS) cluster, harnessing the scalability and flexibility of Kubernetes.

Challenges Conquered:

- Granting AWS CLI Access: Establishing appropriate access permissions for the AWS CLI within your AWS account was crucial. This was addressed by meticulously configuring your AWS credentials and IAM roles to ensure secure interaction with AWS services
- Late-Stage Realization: The necessity to download and install relevant AWS modules (e.g., boto3, packages to access aws CLI) emerged in the latter stages of development. This obstacle was overcome by incorporating the required dependencies into the project's environment.
