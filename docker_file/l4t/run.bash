#!/bin/bash

xhost +local:docker

xinput --list | grep keyboard

echo -n "Enter the keyboard id: " 
read keyboard_id

docker run -it --rm \
  --privileged \
  --network=host \
  --runtime=nvidia\
  --env="DISPLAY" \
  --env="QT_X11_NO_MITSHM=1" \
  --env="NVIDIA_VISIBLE_DEVICES=all"\
  --env="NVIDIA_DRIVER_CAPABILITIES=all"\
  --volume="/usr/bin/tegrastats:/usr/bin/tegrastats" \
  --volume="/usr/local/cuda-11.4:/usr/local/cuda-11.4" \
  --volume="/usr/lib/aarch64-linux-gnu/tegra:/usr/lib/aarch64-linux-gnu/tegra" \
  --volume="/lib/modules:/lib/modules" \
  --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
  --env="keyboard_id=${keyboard_id}" \
  --volume="${HOME}/projectLiLi:/root/projectLiLi" \
  --name="projectLiLi" \
  projectlili:r35



