Now you will create the pipeline using a jenkinsfile

A Jenkinsfile is a configuration file written in code that defines and describes how a software project should be built, tested, and deployed using Jenkins. Contains step-by-step instructions that Jenkins follows to automate the entire development lifecycle, from initial build to final deployment.

The Jenkinsfile is usually stored in the project repository along with the source code.

This is a jenkinsfile example:
![Diagram imagen](../../resources/image3.png)

create a new pipeline with the name Test-2.

This time select "Pipeline" and click ok.

![Diagram imagen](../../resources/image4.png)

Now go to the "pipeline" section, click on "try sample pipeline" and select "Hello World".

you should see this jenkinsfile:

![Diagram imagen](../../resources/image5.png)

Congratulations you created your first jenkinsfile pipeline in Jenkins.

How does the jenkinsfile structure work?

- pipeline
  -  Defines a new Jenkins pipeline.
- agent any
  - Specifies that the agent can be any available node to execute the pipeline job. 
  - This allows the job to run on any node in the Jenkins cluster.
- stages
  - Defines the stages of the pipeline. In this case, there's only one stage named "Hello."
- stage('Hello')
  - Defines the "Hello" stage. This stage will contain a set of steps to be executed.
- steps 
  - Defines the steps to be executed in the "Hello" stage.
- echo 'Hello World'
  -  step that prints "Hello World" to the console output of the job.

In summary, this Jenkinsfile creates a pipeline with a single stage named "Hello," which prints "Hello World" to the console output when executed.

save the pipeline and run it.

![Diagram imagen](../../resources/image6.png)

As you can see, we perform the same task as the previous pipeline, but configured from a jenkinsfile.



