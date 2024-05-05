#! /usr/bin/env bash

mkdir -p out

ext=.jpg
file_a=$1
file_b=$2

python src/3d.py $file_a $file_b out/3d_$(basename $file_a $ext)_$(basename $file_b $ext)_$(date +%s)$ext &
python src/1chan.py $file_a $file_b out/1c_$(basename $file_a $ext)_$(basename $file_b $ext)_$(date +%s)$ext
python src/3chan.py $file_a $file_b out/3c_$(basename $file_a $ext)_$(basename $file_b $ext)_$(date +%s)$ext
