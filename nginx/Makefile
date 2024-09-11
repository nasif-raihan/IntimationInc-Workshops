one:
	python server_one/main.py

two:
	python server_two/main.py

docker-one:
	docker build -t server-one ./server_one
	docker run --name server-one -p 8001:8001 server-one

docker-two:
	docker build -t server-two ./server_two
	docker run --name server-two -p 8002:8002 server-two

docker-nginx:
	docker build -t nginx ./nginx
	docker run --name nginx -p 80:80 nginx

docker-front-end:
	docker build -t frontend ./front-end
	docker run --name frontend -p 3000:3000 frontend