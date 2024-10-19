if [ "$1" == "decode" ]; then
    python3 decoder.py
else
    echo "Usage: $0 decode"
fi
