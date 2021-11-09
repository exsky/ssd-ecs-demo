# use bash
CURR_DIR	:=	$(shell pwd)
NEW_TAG		=	$(shell date +"%Y%m%d%H%M")

.PHONY: all install run build-img push-img update-pippkg install-pippkg deploy-model

all:

install:
	echo "Install toolkits for regeneration of security report"
	pip3 install mxnet_cu102-1.6.0-py2.py3-none-linux_aarch64.whl
	# npm install

run:
	echo "Run node.js index.js ..."
	python3 app-in-container.py

build-img:
	docker build -t cht-ad-player .

push-img:
	aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin 210567265155.dkr.ecr.ap-northeast-1.amazonaws.com
	docker tag cht-ad-player:latest 210567265155.dkr.ecr.ap-northeast-1.amazonaws.com/cht-face-ad:latest
	docker push 210567265155.dkr.ecr.ap-northeast-1.amazonaws.com/cht-face-ad:latest

update-pippkg:
	pipenv sync
	pipenv run pip freeze > requirements.txt

install-pippkg:
	pip install -r requirements.txt

deploy-model:
	rm -rf incubator-mxnet
	git clone -b v1.x --single-branch https://github.com/apache/incubator-mxnet.git
	cp trained-model/ssd_vgg16_512-0000.params incubator-mxnet/example/ssd/model/
	cp trained-model/ssd_vgg16_512-symbol.json incubator-mxnet/example/ssd/model/
	cp -R images/* incubator-mxnet/example/ssd/data/

