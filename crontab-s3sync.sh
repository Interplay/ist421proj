#!/bin/bash

export AWS_CONFIG_FILE="home/ubuntu/.aws/config"
export AWS_ACCESS_KEY_ID=AWS_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY=AWS_SECRET_ACCESS_KEY

/usr/bin/aws s3 sync /home/ubuntu/orderhis/AprilOrder s3://ist421proj
/usr/bin/aws s3 sync /home/ubuntu/orderhis/CustInfo s3://ist421proj
/usr/bin/aws s3 sync /home/ubuntu/orderhis/OrderLocation s3://ist421proj

/usr/bin/aws s3 sync /home/ubuntu/orderhis/AprilOrder s3://ist421proj1 
/usr/bin/aws s3 sync /home/ubuntu/orderhis/CustInfo s3://ist421proj2
/usr/bin/aws s3 sync /home/ubuntu/orderhis/OrderLocation s3://ist421proj3
