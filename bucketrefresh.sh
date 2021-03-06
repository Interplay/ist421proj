#!/bin/bash

export AWS_CONFIG_FILE="home/ubuntu/.aws/config"
export AWS_ACCESS_KEY_ID=AWS_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY=AWS_SECRET_ACCESS_KEY

/usr/bin/aws s3 rm --recursive s3://ist421proj --exclude "*.html"
/usr/bin/aws s3 rm --recursive s3://ist421proj1
/usr/bin/aws s3 rm --recursive s3://ist421proj2
/usr/bin/aws s3 rm --recursive s3://ist421proj3

sudo rm /var/www/html/OrderHistory/AprilOrders/*
sudo rm /var/www/html/OrderHistory/CustInfo/*
sudo rm /var/www/html/OrderHistory/OrderLocation/*

sudo rm /home/ubuntu/orderhis/AprilOrder/*
sudo rm /home/ubuntu/orderhis/OrderLocation/*
sudo rm /home/ubuntu/orderhis/CustInfo/*