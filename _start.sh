#!/bin/bash

# Copy HAR file from desktop
cp /mnt/c/Users/Yxian/Desktop/LAZ/pages.lazada.sg.har .

# Run urls.py
python urls.py

echo -n "Check urls first (y/n): "
read ans

# Run main.py
if [[ `echo $ans | grep -i y` ]]; then
python main.py  
fi