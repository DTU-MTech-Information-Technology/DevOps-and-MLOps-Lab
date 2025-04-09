# Experiment 1

## Aim

Introduction to DevOps and MLOps: Understand the basic principles, differences, and lifecycle of both

## Theory

Today's software development and machine learning practices demand efficient processes, inter-team collaboration, and automation to manage complex systems effectively. Two practices that have emerged to address these demands are DevOps and MLOps.

### DevOps

DevOps is a technical and cultural movement that closes the gap between software development and IT operations. Historically, both teams operated in silos, which resulted in slow delivery, unreliable environments, and deployment failures. DevOps strives to dismantle these silos by encouraging cooperation, continuous feedback, and end-to-end automation.

_Major Objectives of DevOps:_

- **Faster Deployment**: Build, testing, and release automation to ship features quickly.
- **Better Quality**: Regular testing and monitoring to identify problems early.
- **Scalability**: Infrastructure as Code (IaC) and containerization enable scaling applications with ease.
- **Reliability**: Continuous monitoring keeps systems stable and responsive.

_DevOps Lifecycle:_

- **Plan**: Determine features, objectives, and project scope.
- **Develop**: Writing and managing application code.
- **Build**: Compile code and create executable artifacts.
- **Test**: Automated and manual testing for assurance of quality.
- **Release**: Deployment to production environments.
- **Operate**: Monitoring and upkeep of systems in real-time.
- **Monitor**: Gathering data, logs, and performance metrics.

These tools such as _Git_, _Jenkins_, _Docker_, _Kubernetes_, and _Ansible_ are commonly utilized in DevOps pipelines.

### MLOps

MLOps refers to the application of DevOps practices to machine learning systems. Although sharing similar philosophy, MLOps mitigates special issues that emerge owing to the data-driven and experimentation-based nature of ML development.

Machine learning models are not simply code—they depend significantly on data, model training, and performance testing. In contrast to standard software, ML models can get worse over time due to changing data distributions (referred to as model drift). MLOps practices seek to ensure models are versioned, tested, deployed, and monitored regularly.

_MLOps Lifecycle:_

- **Data Collection & Preparation**: Collecting and cleaning data sets.
- **Model Development**: Developing and testing ML models.
- **Model Training**: Training the model with data.
- **Model Evaluation**: Performance validation through metrics (accuracy, precision, etc.).
- **Model Deployment**: Deploying the model through APIs or integrating it into apps.
- **Model Monitoring**: Monitoring predictions, performance, and drift.
- **Model Retraining**: Periodically updating the model with new data.

Some of the popular MLOps tools are _MLflow_, _Kubeflow_, _TensorFlow Extended (TFX)_, _DVC (Data Version Control)_, and _Seldon Core_.

### Differences

| Category    | DevOps                               | MLOps                                                    |
| ----------- | ------------------------------------ | -------------------------------------------------------- |
| Main Focus  | Application development and delivery | Managing the ML lifecycle and model operations           |
| Artifacts   | Application code                     | Code, datasets, trained models, and metrics              |
| Automation  | Build, test, deploy                  | Data pipeline automation, training, and model deployment |
| Testing     | Unit & integration tests             | Data validation, model validation, performance tests     |
| Monitoring  | System performance, errors           | Model accuracy, prediction quality, drift detection      |
| Reusability | High (same code runs consistently)   | Harder (data changes may require retraining)             |

MLOps can be considered a superset of DevOps with additional complexity due to the involvement of large datasets, model behavior, and continuous evaluation needs.

## Conclusion

In this experiment, we learned the basic principles of DevOps and MLOps. We discovered that both have common such as automation, CI/CD, and monitoring but with the introduction of data and model management, MLOps has other challenges. Having an understanding of their lifecycle differences aids in creating more efficient workflow for application and machine learning development. This forms the basis of learning more about real-world DevOps and MLOps implementations in subsequent experiments.
