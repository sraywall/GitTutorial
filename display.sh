#!/bin/bash

echo "Report of current contents of /etc:"

if [-d /etc]
then
    echo -n "Number of directories: "
    ls -l /etc | grep "^d" | wc -l
    echo -n "Number of links: "
    ls -l /etc | grep "^l" | wc -l
    echo -n "Number of regular files: "
    ls -l /etc | grep "^-" | wc -l
fi
