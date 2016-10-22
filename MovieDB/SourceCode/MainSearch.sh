#!/bin/bash
# My first script

python MovieDB.py

grep -i $1 '/home/sachinpc/git/MovieDBProject/MovieDB/English.txt'
grep -i $1 '/home/sachinpc/git/MovieDBProject/MovieDB/Hindi.txt'
grep -i $1 '/home/sachinpc/git/MovieDBProject/MovieDB/Malayalam.txt'
grep -i $1 '/home/sachinpc/git/MovieDBProject/MovieDB/Tamil.txt'
