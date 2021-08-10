#!/bin/bash
sudo qemu-system-arm -kernel kernel-buster -cpu arm1176 -m 256 -M versatilepb -serial stdio -append "root=/dev/sda2 rootfstype=ext4 rw" -hda ~/qemu_vms/rasbian-wheezy.img -net nic -net tap,ifname=tap0,script=no,downscript=no -no-reboot
