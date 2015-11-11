#!/bin/bash

if [ ! -d flask ]; then
	virtualenv --clear flask
fi

source flask/bin/activate
pip install -r requirements
