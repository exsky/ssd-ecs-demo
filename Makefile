# use bash
CURR_DIR	:=	$(shell pwd)
NEW_TAG		=	$(shell date +"%Y%m%d%H%M")

.PHONY: all install run build-img

all:

install:
	echo "Install toolkits for regeneration of security report"
	# npm install

run:
	echo "Run node.js index.js ..."
	python3 app-in-container.py

build-img:
	docker build -t cht-ad-player .
