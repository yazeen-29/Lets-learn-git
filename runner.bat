@echo off
if "%1"=="decode" (
    python decoder.py
) else (
    echo Usage: decode.bat decode
)
