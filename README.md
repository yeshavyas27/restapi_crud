
# Flask Application for CRUD operations on MongoDB

## I have used docker for mongoDB, 

* Open the terminal and run the following command to download the MongoDB Docker image:
  ```sh
  docker pull mongo
  ```
* Once the image is downloaded, you can start a MongoDB container by running the following command:
  ```sh
  docker run --name mymongodb -p 27017:27017 -d mongo
  ```
* Verify that the container is running by executing the following command:
  ```sh
  docker ps
  ```
 * To connect to the instance using the MongoDB shell, run the following command in a new terminal window:
  ```sh
  mongo --host localhost:27017
  ```
 * Now, if have already created the container before, you can simply skip the above steps and type the following command
  ```sh
  docker start mymongodb
  ```
 * When you're done using the container, you can stop it by running the following command:
  ```sh
  docker stop mymongodb
  ```
 <br>
  
## Make sure that you have installed all the packages required for the file and then simply run app.py
## Here is my video, performing CRUD operations through Postman

https://user-images.githubusercontent.com/103744693/236623756-969991ad-4a2b-4489-b29a-e20263d68066.mp4



