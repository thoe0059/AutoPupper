#!/usr/bin/env bash

sudo apt update
sudo apt install -y git vim screen python3-pip python-pip

#### Fixes old pip in apt repo
yes | sudo pip3 install --upgrade pip
yes | sudo pip install --upgrade pip

#### IPython is nice to have
yes | sudo pip3 install ipython
yes | sudo pip install ipython

echo "DevTools installed, Raspbian will now reboot!"

sudo reboot
