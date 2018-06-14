#!/bin/bash 

find_path() {
	SQUEALER_DIR=$(find /* -name $1 -exec dirname {} \; 2>&1 | grep -v "Permission denied" )
	echo $SQUEALER_DIR
}

msg_squealer() { 
	SQUEALER_DIR=$(find_path "squealer_sub.py")
	echo $SQUEALER_DIR

	if [[ -n $SQUEALER_DIR  ]]; then
	    echo "Squealer is present on the server at $SQUEALER_DIR, msging $1"

	    EXECUTE='python3.6 '"$SQUEALER_DIR"'/squealer_pub.py --msg="$1" '
	    echo "executing: $EXECUTE"
	    eval $EXECUTE

	else
		echo 'no'
	fi
}