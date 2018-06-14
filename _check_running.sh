#!/bin/bash 
source utils/bash_includes.sh 

# Array of screens/files associated with squealer to check are running 
array=(
	# screen :: file.py 
	'squealer_subscriber::squealer_sub.py'
)

for i in "${array[@]}"
do
	SPLIT=(${i//::/ })

	SCREENNAME=${SPLIT[0]}
	SQUEALER_DIR=$(find_path ${SPLIT[1]})
	FILE=${SPLIT[1]}
	
	BASHCMD="python3.6 $SQUEALER_DIR/$FILE"
	EXECUTE="screen -d -m -S $SCREENNAME bash -c \"$BASHCMD\""

	if pgrep -f $FILE > /dev/null
	then
		echo "Screen '$SCREENNAME' is active, nothing to do"
	else
		echo "----"
		echo "Unable to find active screen: $SCREENNAME"
		echo "Restarting: $EXECUTE"
		eval $($EXECUTE)
		# sleep 5 
		# msg_squealer "Restarted $FILE"
	fi

done