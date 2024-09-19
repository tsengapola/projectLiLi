FROM nvcr.io/nvidia/l4t-base:r35.2.1

ENV PATH=/usr/local/cuda-11.4/bin:$PATH
ENV LD_LIBRARY_PATH=/usr/local/cuda-11.4/lib64:$LD_LIBRARY_PATH

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN apt-get update

RUN apt-get install -y apt-utils && apt-get install -y curl gnupg2 && apt-get install -y lsb-release && apt-get clean all


#install some tool
RUN apt install -y nano openssh-server 
#for ping hardware etc...
RUN apt-get install -y iputils-ping
#for ifconfig
RUN apt-get install -y net-tools
#for ifconfig
RUN apt-get install -y htop
RUN apt-get install -y build-essential
RUN apt-get install -y git

RUN apt update

# Install pip
RUN apt install -y python3-pip


# fix map tool
RUN apt install -y libfreeimage-dev

#install GDB
RUN apt install -y gdb

RUN apt install -y x11-xserver-utils

RUN pip3 install ultralytics

RUN apt install -y xinput

#install jetson torch
RUN pip3 uninstall -y torch torchvision

RUN apt-get install -y libopenblas-base libopenmpi-dev
RUN wget https://developer.download.nvidia.com/compute/redist/jp/v512/pytorch/torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl -O torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl
RUN pip install torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl

RUN apt install -y libcudnn8
RUN apt install -y libcudnn8-dev

RUN apt install -y libjpeg-dev zlib1g-dev
RUN cd /tmp && git clone https://github.com/pytorch/vision torchvision

#RUN cd /tmp/torchvision && git checkout v0.16.2 && python3 setup.py install

WORKDIR /root

CMD ["bash"]
