#!/bin/bash

for num in {1..5}
do
     echo $num
done

for file in *.log
do
    tar -czvf $file.tar.gz $file
done
