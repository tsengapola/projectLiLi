#!/bin/bash

xhost +local:docker

xinput --list | grep keyboard

echo -n "Enter the keyboard id: " 
read keyboard_id

docker run -it --rm \
  --privileged \
  --network=host \
  --env="DISPLAY" \
  --env="QT_X11_NO_MITSHM=1" \
  --env="keyboard_id=${keyboard_id}" \
  --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
  --volume="${HOME}/projectLiLi:/root/projectLiLi" \
  --name="projectLiLi" \
  projectlili:latest \
  sh -c "python3 /root/projectLiLi/src/yolo.py"



