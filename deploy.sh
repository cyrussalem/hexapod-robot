#!/bin/bash

# Deployment script for Hexapod Robot to Raspberry Pi Zero
# Usage: ./deploy.sh [pi_user@pi_ip_address]
# Example: ./deploy.sh pi@192.168.1.100

# Default Raspberry Pi connection (change as needed)
PI_USER_HOST=${1:-"pi@raspberrypi.local"}
TARGET_DIR="hexapod-robot"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Deploying Hexapod Robot to ${PI_USER_HOST}...${NC}"

# Create target directory on Pi
echo -e "${YELLOW}Creating target directory on Pi...${NC}"
ssh ${PI_USER_HOST} "mkdir -p ~/${TARGET_DIR}"

if [ $? -ne 0 ]; then
    echo -e "${RED}Failed to connect to Raspberry Pi. Please check connection and try again.${NC}"
    exit 1
fi

# Use rsync to copy files, excluding unwanted directories and files
echo -e "${YELLOW}Copying files via rsync...${NC}"
rsync -avz --progress \
    --exclude='.git/' \
    --exclude='.gitignore' \
    --exclude='__pycache__/' \
    --exclude='*.pyc' \
    --exclude='*.pyo' \
    --exclude='*.pyd' \
    --exclude='.pytest_cache/' \
    --exclude='pytest_cache/' \
    --exclude='venv/' \
    --exclude='env/' \
    --exclude='.venv/' \
    --exclude='.env/' \
    --exclude='node_modules/' \
    --exclude='.DS_Store' \
    --exclude='*.log' \
    --exclude='*.tmp' \
    --exclude='*.swp' \
    --exclude='*.swo' \
    --exclude='.idea/' \
    --exclude='.vscode/' \
    --exclude='*.egg-info/' \
    --exclude='build/' \
    --exclude='dist/' \
    --exclude='.coverage' \
    --exclude='htmlcov/' \
    --exclude='deploy.sh' \
    ./ ${PI_USER_HOST}:~/${TARGET_DIR}/

if [ $? -eq 0 ]; then
    echo -e "${GREEN}Deployment successful!${NC}"
    echo -e "${GREEN}Files copied to ${PI_USER_HOST}:~/${TARGET_DIR}/${NC}"
    
    # Optional: Install requirements on the Pi
    # echo -e "${YELLOW}Installing Python requirements on Pi...${NC}"
    # ssh ${PI_USER_HOST} "cd ~/${TARGET_DIR} && python3 -m pip install -r requirements.txt --user"
    
    echo -e "${GREEN}Deployment complete!${NC}"
    echo -e "${YELLOW}You can now SSH to your Pi and run: cd ~/${TARGET_DIR} && python3 main.py${NC}"
else
    echo -e "${RED}Deployment failed!${NC}"
    exit 1
fi