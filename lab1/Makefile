# use bash
NEW_TAG		=	$(shell date +"%Y%m%d%H%M")

.PHONY: all run build-img push-img

all:

run:
	python3 app-in-container.py

build-img:
	docker build -t myawesome-img .

push-img:
	aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin 210567265155.dkr.ecr.ap-northeast-1.amazonaws.com
	docker tag myawesome-img:latest 210567265155.dkr.ecr.ap-northeast-1.amazonaws.com/myawesome-img:latest
	docker tag myawesome-img:latest 210567265155.dkr.ecr.ap-northeast-1.amazonaws.com/myawesome-img:${NEW_TAG}
	docker push 210567265155.dkr.ecr.ap-northeast-1.amazonaws.com/myawesome-img:latest
	docker push 210567265155.dkr.ecr.ap-northeast-1.amazonaws.com/myawesome-img:${NEW_TAG}
