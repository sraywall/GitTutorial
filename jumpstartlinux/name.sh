#!/bin/bash

#name.sh

echo "Enter your name"

read name

if [ -n "$name" ]

then
    echo "Thank you!"

else
    echo "hey, you didn't give a name!"
fi
