#!/bin/bash

export AWS_CONFIG_FILE="home/ubuntu/.aws/config"
export AWS_ACCESS_KEY_ID=AWS_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY=AWS_SECRET_ACCESS_KEY

/usr/bin/aws s3 sync s3://ist421proj1 /var/www/html/OrderHistory/AprilOrders
/usr/bin/aws s3 sync s3://ist421proj2 /var/www/html/OrderHistory/CustInfo
/usr/bin/aws s3 sync s3://ist421proj3 /var/www/html/OrderHistory/OrderLocation