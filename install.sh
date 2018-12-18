#!/bin/bash
BS4="pip install beautifulsoup4"
BIN_DIR="mkdir ~/bin"
COPY="cp google ~/bin"

eval "chmod +x google.py"
eval "mv google.py google"

if [ -x "$(command -v python)" ]; then
	echo "Python installed"
else
	if [[ $OSTYPE == "linux-gnu" ]]; then
		python = "sudo apt-get install python3"
		eval $python
	elif [[ $OSTYPE == "darwin"* ]]; then
		[ ! -x "$(command -v brew)" ] && eval "usr/bin/ruby -e '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)'"
		eval "brew install python3"
	fi
fi

eval $BS4

[ -d ~/bin ] && echo "Directory exists!" || eval "$BIN_DIR"
[ -f ~/bin/google ] && echo "File exists!" || eval $COPY

echo 'export PATH=$PATH":$HOME/bin"' >> ~/.bash_profile
echo "Finished installing!"
echo "Restart the terminal to see the effects"
exit 1
