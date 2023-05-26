# Cloud-Native_Monitoring-Application

> Initial Requirments

Tools: Linux, Docker , AWS account, kubectl, VS Code
Language: Python-3(Flask, psutil)

> Important Note if you want to start this project 
> ```
> AWS is risky and every thing is not not free in Free tier 
>🤖😥I got bill of (4.70$ + 0.85$(TAX) = 5.55$ )  bill while working on this project
> So don't leave any EKS/ECR/ECS service active for 2-3 days just for project 💔
<img width="704" alt="image" src="https://github.com/Akashay-Anand/Cloud-Native_Monitoring-Application/assets/82114930/95d46cf5-2dc1-49c8-8769-874dcd242c63">   

> ```
> 
> some links which may help ---
>
> CloudTrail: https://aws.amazon.com/cloudtrail/getting-started/
> CloudWatch: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch.html
> Budgets: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html
> 
> ```


# // Lets Start \\\  👨‍💻🥷

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

6> kubernetes deployment and services
> kubernetes uses deployment to maintain the state
// resources   
https://kubernetes.io/docs/concepts/workloads/controllers/deployment/

> our application runs on pods and we uses Service method for exposing a network application that is running as one or more Pods in your cluster.

// terminal commands for Kubectl

// check of deployments
```kubectl
kubectl get deployment -n default 
```
// update deployments (first image url in eksfile.py then change from console); 
```kubectl
kubectl edit deployment <dep. name> -n default 
# this command will open editable file in 'vim terminal' change containers>image link
# to save and exit => 'esc + :wq'
```
// check of pods
```kubectl
kubectl get pods -n default -w
```
// all the details regarding pods
```kubectl
kubectl describe pods <pod name> -n default
```
// check of services
```kubectl
kubectl get svc -n default 
```

// port-forward ; run pods in localhost
```kubectl
kubectl port-forward svc/my-flask-service 5000:5000
```

> End now our app has been hosted on kubernetes cluster <

# Have Great Time. 🤖😶‍🌫️🌦️🌦️
