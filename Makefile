build:
	sudo docker build -t toxin_image .

kill:
	- sudo docker stop toxin
	- sudo docker rm toxin

run: kill build
	sudo docker run -d -t --name toxin toxin_image
	sudo docker inspect --format='{{.NetworkSettings.IPAddress}}' toxin

run-interactive: kill build
	sudo docker run -i -t --name toxin toxin_image bash

