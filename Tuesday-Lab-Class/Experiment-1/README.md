# Experiment 1

## Aim

Introduction to DevOps and MLOps: Understand the basic principles, differences, and lifecycle of both

## Theory

DevOps and MLOps are new software engineering paradigms that seek to automate the development, deployment, and management of applications and machine learning models respectively.

### DevOps?

DevOps is an amalgamation of Development (Dev) and Operations (Ops). It fosters a culture of collaboration between software developers and IT operations staff. The primary objective is to provide software more quickly, with increased quality, and with more reliability.

Key principles of DevOps:

- Continuous Integration (CI)
- Continuous Delivery/Deployment (CD)
- Infrastructure as Code (IaC)
- Monitoring and Logging
- Automation

### What is MLOps?

MLOps, or Machine Learning Operations, applies DevOps practices to the machine learning lifecycle. It speaks to the novel challenges of deploying and operating machine learning models in production, including:

- Data versioning
- Model training and retraining
- Model deployment
- Model monitoring and drift detection

MLOps provides reproducibility, scalability, and governance for ML workflows.

#### Lifecycle Comparison

| Phase      | DevOps                       | MLOps                                     |
| ---------- | ---------------------------- | ----------------------------------------- |
| Code       | Source code for applications | Source code + data pipelines + model code |
| Build/Test | Unit & integration testing   | Model training, validation, testing       |
| Deploy     | Web/App deployment           | Model serving/deployment                  |
| Monitor    | App performance & uptime     | Model accuracy, drift, performance        |
| Maintain   | Code fixes, infra updates    | Retraining, dataset updates               |

## Conclusion

In this experiment, we learned the basic principles of DevOps and MLOps. We discovered that both have common such as automation, CI/CD, and monitoring but with the introduction of data and model management, MLOps has other challenges. Having an understanding of their lifecycle differences aids in creating more efficient workflow for application and machine learning development. This forms the basis of learning more about real-world DevOps and MLOps implementations in subsequent experiments.
