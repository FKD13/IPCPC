# IPCPC

IP Camera Python Client.
I personaly use it in combination with this [app](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=nl&gl=US)

## Description

A simple python script that fetches an image and sends it to your v4l2loopback device.

## Installation

Install `v4l2loopback-dkms` and enable using `modprobe v4l2loopback`.
Install the requirements: `pip install -r requirements.txt` in a virtual envirionment.

## Use

Execute `python3 ipcpc.py`. Tweak some parameters in the script if necessary.
