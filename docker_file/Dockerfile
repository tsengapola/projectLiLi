#FROM ubuntu:22.04
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN apt-get update

RUN apt-get install -y apt-utils && apt-get install -y curl gnupg2 && apt-get install -y lsb-release && apt-get clean all


# --- ROS2 Humble Installation
RUN locale  # check for UTF-8

RUN apt update && apt install -y locales
RUN locale-gen en_US en_US.UTF-8
RUN update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

RUN echo "export LANG=en_US.UTF-8" >> /root/.bashrc

RUN locale  # verify settings

RUN apt install -y software-properties-common
RUN add-apt-repository universe
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null

RUN apt-get update && apt-get install -y git

RUN apt install -y ros-humble-desktop
# --- Humble has been installed


#install some tool
RUN apt install -y nano openssh-server 
#for ping hardware etc...
RUN apt-get install -y iputils-ping
#for ifconfig
RUN apt-get install -y net-tools
#for ifconfig
RUN apt-get install -y htop
RUN apt-get install -y build-essential

# Install pip
RUN apt install -y python3-pip

RUN apt install -y libopencv-dev python3-opencv

# Install colcon
RUN apt update && apt install -y python3-colcon-common-extensions

#gst
RUN apt install -y libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio

# fix map tool
RUN apt install -y libfreeimage-dev

#install GDB
RUN apt install -y gdb

RUN apt install -y x11-xserver-utils

RUN pip3 install ultralytics

RUN apt install -y xinput

RUN pip3 uninstall -y numpy

RUN pip3 install "numpy<2.0"

WORKDIR /root

CMD ["bash"]
