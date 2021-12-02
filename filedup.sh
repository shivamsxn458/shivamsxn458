#!/usr/bin/bash

a=0
b=$RANDOM
echo "How many Random numbers you want?"
read numa
while [ $a -lt $numa ]
do
{
  echo  $a, $b
} 
 a=$(($a + 1))
  b=$RANDOM
done






