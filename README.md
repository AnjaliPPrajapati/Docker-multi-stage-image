# Docker-multi-stage-image
**This repository will be showing the use and explanation of docker multi-stage images by combining RabbitMQ and Python**

*In the world of Docker, it’s common to run multiple services in separate containers using Docker Compose. But what if you need to bundle everything into a single image? In this post, I’ll show you how to combine RabbitMQ and a Python script into one Docker image using Multistage Builds.*

![1_zEhVBwQmSYOfWONtBf7CMQ](https://github.com/user-attachments/assets/ba80a4b5-78dd-47e6-9044-bb9656a4bd2b)

- **The Challenge:**
  Let’s say you need to run both RabbitMQ and a Python script inside a single Docker container.
  1) You can’t use Docker Compose.
  2) You can’t have multiple Dockerfiles.
- **How can you make it work?**
  * The solution is Multistage Docker Builds!

- **What is a Multistage Build?**
  * A Multistage Build allows you to use multiple FROM statements in a single Dockerfile. Each stage can do a specific job, and at the end, you combine them into one image. This helps keep the final image clean and efficient by removing unnecessary layers and reducing size of the image.

- **How to Achieve This?**
  * This repository shows a basic example of a Multistage Dockerfile which includes both RabbitMQ and a Python script. Assuming you have your main.py file (A python script) and requirements.txt file (having all the dependencies for you main script) or you can use files from this repository.
 
- **How It Works?**
* The Dockerfile uses two stages. The first stage installs Python dependencies and prepares the Python application (python_reader), while the second stage builds the RabbitMQ image and includes the Python application inside it.

*RabbitMQ and Python Application Combined: The final image has both RabbitMQ running and the Python application (main.py) ready to be executed.*

- **Steps To Run:**
  1) Make all 3 files mentioned above available in your system in same directory.
  2) Go to the directory containing files and run following command to make docker image:
     ```bash
     docker build -t rabbitmq_test .
   
  3) To run this image follow the command:
     ```bash
      docker run  --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq_test

  4) You can now see your things up and running, to access your RabbitMQ UI, go to http://localhost:15672 on your system or change hostname accordingly in the URL.

- **Conclusion:**
  Multi-stage builds in Docker help create smaller, more efficient containers by separating the build process into multiple stages. This allows you to include only the     necessary components in your final image, reducing its size and improving performance. By using this technique, you can optimize your development and deployment processes.

*You can learn more on this topic [here](https://docs.docker.com/build/building/multi-stage/) !!!*
