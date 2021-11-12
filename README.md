# ssd-ecs-demo
This repository show how we build an AD machine that recognize face and deliver different ads.

## Build mxnet from source
* COPY config.mk and replace some parameters
```
sed -i 's/USE_CUDA = 0/USE_CUDA = 1/' config.mk
sed -i 's/USE_CUDA_PATH = NONE/USE_CUDA_PATH = \/usr\/local\/cuda/' config.mk
sed -i 's/USE_CUDNN = 0/USE_CUDNN = 1/' config.mk
sed -i '/USE_CUDNN/a CUDA_ARCH := -gencode arch=compute_53,code=sm_53' config.mk
```

* Add these lines in build-mxnet container
```
export PATH=/usr/local/cuda-10.2/bin:$PATH
export CUDA_HOME=/usr/local/cuda-10.2
export MXNET_HOME=/source/mxnet/
export PYTHONPATH=$MXNET_HOME/python:$PYTHONPATH
export LD_LIBRARY_PATH=/usr/local/cuda-10.2/targets/aarch64-linux/lib/:/usr/include
```
