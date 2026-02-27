# KUBERNETES SHORT NOTES!

- **K8s is now your oyster!😎**

1. Why Kubernetes Exists (Start Here or Get Lost)
The Problem Before Kubernetes

Imagine you run:

1 web app

On 1 server

Using Docker

Life is good… until:

Traffic spikes → app crashes

Server dies → app gone

You update code → downtime

You need 10 copies → chaos

Kubernetes Solves:

Scaling → run more copies automatically

Self-healing → restart crashed apps

Deployment → zero downtime updates

Resource management → CPU & memory control

Infrastructure abstraction → same setup everywhere

📌 Mental Model

Kubernetes is an operating system for distributed applications, not servers.

2. Core Kubernetes Architecture (The Big Picture)
Cluster = Control Plane + Worker Nodes
Control Plane (The Brain 🧠)

Decides what should run and where.

API Server – Front door of the cluster

etcd – Database storing cluster state

Scheduler – Chooses which node runs a pod

Controller Manager – Fixes deviations (desired vs actual)

Worker Nodes (The Muscle 💪)

Actually run your apps.

kubelet – Talks to control plane, runs containers

Container Runtime – Docker / containerd

kube-proxy – Handles networking

📌 Analogy

Control plane = factory management
Worker nodes = factory workers
Pods = machines doing work

3. Pods — The Smallest Unit (CRUCIAL)
What is a Pod?

A pod is:

One or more containers

Sharing:

IP address

Storage

Network namespace

📌 Kubernetes does NOT run containers directly — it runs pods.

Why Pods?

Because some containers:

Must run together

Communicate via localhost

📌 Example

App container + logging sidecar

App container + metrics exporter

Reality Check

You almost never create pods directly.
Controllers do that for you.

4. Controllers — The Real Power

Controllers maintain desired state.

Deployment (MOST IMPORTANT)

Manages stateless apps.

Ensures N replicas running

Handles rolling updates

Replaces crashed pods

📌 Example:

replicas: 3


If one pod dies → Kubernetes creates another automatically.

📌 Analogy

Deployment = manager saying
“I want 3 cashiers working at all times.”

ReplicaSet

Created by Deployment

Tracks number of pods

You rarely touch it directly.

StatefulSet (Advanced but Important)

Used for:

Databases

Stateful apps

Features:

Stable pod names

Persistent storage

Ordered startup/shutdown

📌 Example

MySQL, PostgreSQL, Kafka

DaemonSet

Runs one pod per node.

📌 Example:

Log collectors

Monitoring agents

5. Services — How Pods Talk
The Problem

Pods:

Die

Get recreated

Change IPs

Service Solves This

Provides:

Stable IP

Stable DNS

Load balancing

Types of Services
ClusterIP (Default)

Internal access only

NodePort

Exposes app via node IP + port

LoadBalancer

Creates cloud load balancer (AWS, GCP)

📌 Analogy

Service = receptionist
Pods = employees who come and go

6. Ingress — Smart Traffic Routing

Ingress:

Routes HTTP/HTTPS traffic

Based on:

Domain

Path

📌 Example:

/api → backend
/ → frontend


Ingress needs:

Ingress Controller (NGINX, ALB, Traefik)

7. ConfigMaps & Secrets — Configuration Management
ConfigMap

Stores:

Environment variables

App configs

Secret

Stores:

Passwords

Tokens

Keys (base64 encoded)

📌 Rule

Never bake config into Docker images.

8. Volumes & Persistent Storage
Why?

Pods are ephemeral.

PersistentVolume (PV)

Actual storage

PersistentVolumeClaim (PVC)

Request for storage

📌 Analogy

PVC = asking landlord for space
PV = the actual apartment

9. Scheduling, Resources & Limits (Often Ignored → Disaster)

Each pod can request:

CPU

Memory

requests:
  cpu: "250m"
limits:
  cpu: "500m"


📌 Prevents:

Noisy neighbors

Node crashes

10. Kubernetes Networking (Simplified)

Rules:

Every pod gets its own IP

Pods can talk to each other freely

No NAT between pods

CNI plugins:

Calico

Flannel

AWS VPC CNI (EKS)