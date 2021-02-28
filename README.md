Test_repo
=======

Trigo – DevOps Assignment - Configurations

General:

1.	Please Clone the following repo:
	https://github.com/trigodevops/test_repo.git
	
2.  Please work only on that repo – you got all the permissions that you need.
3.	You got 3 hours.

Stage 1:

1.	Please deploy a multi env configuration solution.
2.	You can deploy it anywhere you want with any tool that to want to use.


		http://service_name:8080/prod/service-a/config - will present production configuration of service a 
		http://service_name:8080/prod/service-b/config - will present production configuration of service b
		http://service_name:8080/dev/service-a/config  - will present dev configuration of service a. 

Stage 2:

1.	Update app version.
2.	Update configuration values and deploy. (the links should be updated as well)
3.	Promote APP from dev to prod.
4.	Promote APP Configs from dev to prod.


Solution
=======

**Requirements:**

1.	Please install minikube/kind: (kind is preferred since its lightweight - kind is a tool for running local Kubernetes clusters using Docker container “nodes”.)
     - https://minikube.sigs.k8s.io/docs/start/ https://kind.sigs.k8s.io/docs/user/quick-start/
	
2.  Please install Docker https://docs.docker.com/docker-for-mac/install/

3.	Please install kubectl to run commands against Kubernetes cluster https://kubernetes.io/docs/tasks/tools/install-kubectl/

3.	Please install Skaffold https://skaffold.dev/docs/install/ Skaffold is a command line tool that facilitates continuous development for Kubernetes-native applications.

**Guidelines:**

1.  Please clone the github repository locally.
2.	We will create the kind cluster by running: `$ kind create cluster`
3.  Skaffold knows to build the app using the Docker daemon hosted inside minikube/kind and thus avoiding any need for a registry to host the app’s container images.
4.  We will use `skaffold dev` to build and deploy the APP and services every time the code changes.
5.  We will use `skaffold run` to build and deploy the APP once, similar to a CI/CD pipeline to update the version.
6.  If needed to do it only for specific app/service, you will need to go in and run it from the relevant dir.
7.  If the _portForward_ isn't working somehow because of permissions, please run: 

`sudo kubectl port-forward deployment/multi-env-config-deployment 80:80`

8. Then you will able to download each configuration file by going to your browser and use each URLs:


		http://localhost:80/prod/service-a/config - will present production configuration of service a 
		http://127.0.0.1:80/prod/service-b/config - will present production configuration of service b
		http://127.0.0.1:80/dev/service-a/config  - will present dev configuration of service a. 
		http://localhost:80/dev/service-b/config  - will present dev configuration of service b. 

**Cleaning:**

- For stopping Skaffold you can just ctrl+c and then it will start cleaning up.
- For destroying the cluster run `$ kind delete cluster `