#!/bin/bash

xhost +local:docker

xinput --list | grep keyboard

echo -n "Enter the keyboard id: " 
read keyboard_id

docker run -it\
  --privileged \
  --network=host \
  --runtime=nvidia \
  --env="DISPLAY" \
  --env="QT_X11_NO_MITSHM=1" \
  --env="NVIDIA_VISIBLE_DEVICES=all"\
  --env="NVIDIA_DRIVER_CAPABILITIES=all"\
  --env="keyboard_id=${keyboard_id}" \
  --volume="/dev:/dev" \
  --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
  --volume="${HOME}/projectLiLi:/root/projectLiLi" \
  --name="projectLiLi" \
  projectlili:latest \
  sh -c "python3 /root/projectLiLi/src/yolo.py"


