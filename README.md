# Cloud-Native_Monitoring-Application

> Initial Requirments

Tools: Linux, Docker , AWS account, kubectl, VS Code
Language: Python-3(Flask, psutil)

## Docker
> Install & use Docker (manage containers)    
>> https://docs.docker.com/engine/install/ubuntu/     
>> https://hub.docker.com/    
>> https://labs.play-with-docker.com/    

> 

## AWS
> AWS (Free Tier Account)
>> setup aws terminal CLI tool in linux.    
>> Create user and generate 'access key' so that we can intract with it locally.       
>> provide CLI permission with programmatic access.   

// some commands
aws configure 
aws iam list-users

> kubectl is a tool to manage multiple kubernetes containers through local terminal
setup itt as well as we have did for aws or docker or git

## Python
> Psutil >> Psutil is a Python library for retrieving information about processes and system utilization, including CPU usage, memory usage, disk I/O, network I/O, and more. The name "psutil" stands for "process and system utilities".

> Flask >> like express JS ; Flask is a lightweight and flexible web application framework for Python. It is classified as a micro-framework because it does not require particular tools or libraries, and it doesn't impose a particular way of structuring your application.


/////////////////////////////////////////////////////////

## Steps involve for creating this project

1> Create basick Flask application using 'psutil' library which displays cpu and memory status on browser root addres.

2> create html template for the app with 'plotly' framework 
>> https://plotly.com/   

3> create a docker file which will create image based on the given commands

![docker file](https://geekflare.com/wp-content/uploads/2019/07/dockerfile.png)
>> https://geekflare.com/dockerfile-tutorial/    

> some commands for docker
build imag // docker build -t my-flask-app .    
show images // docker images    
create cont.(run)   // docker run -p 5000:5000 <image id>    
login // docker exec -it <container_name_or_id> bash    
stop  // docker stop my-container     
start // docker start my-container     
remove stopped containers // docker rm my-container   


4> Create ECR repo using Boto3 API and deploy the image
(creaet ECR repo, upload docker image in ecr repo, create EKS cluster )

> create python file (ecrfile.py)
>> write python code using Boto3 API and deploy the image on aws ecr.
``` python
import boto3

ecr_client = boto3.client('ecr')

repository_name = "my-repo-app-aws"
response = ecr_client.create_repository(repositoryName = repository_name)

```
>> Now run the following commands to 

>>> Retrieve an authentication token and authenticate your Docker client to your registry.
Use the AWS CLI:
```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 404426248672.dkr.ecr.us-east-1.amazonaws.com
```
 Note: If you receive an error using the AWS CLI, make sure that you have the latest version of the AWS CLI and Docker installed.

>>>Build your Docker image using the following command. For information on building a Docker file from scratch see the instructions here . You can skip this step if your image is already built:
```
docker build -t my-repo-app-aws .
```
>>>After the build completes, tag your image so you can push the image to this repository:
```
docker tag my-repo-app-aws:latest 404426248672.dkr.ecr.us-east-1.amazonaws.com/my-repo-app-aws:latest
```
Run the following command to push this image to your newly created AWS repository:
```
docker push 404426248672.dkr.ecr.us-east-1.amazonaws.com/my-repo-app-aws:latest
```

5> Create EKS(Elastic Kubernetes Service) cluster

AWS services> EKS> Add Cluster> Create 
