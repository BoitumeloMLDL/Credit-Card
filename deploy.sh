#!/bin/bash

# Colors for output
GREEN="\033[0;32m"
YELLOW="\033[1;33m"
RED="\033[0;31m"
NC="\033[0m" # No color

# Configuration
SERVER_USER="root"
SERVER_IP="161.35.87.43"
DEPLOY_PATH="/home/boitumelo/shard_app/"

# Ensure required environment variables are set
if [ -z "$SERVER_USER" ] || [ -z "$SERVER_IP" ] || [ -z "$DEPLOY_PATH" ]; then
	echo -e "${RED}Error: SERVER_USER, SERVER_IP, and DEPLOY_PATH must be configured in the script.${NC}"
	exit 1
fi

echo -e "${GREEN}Starting deployment to $SERVER_USER@$SERVER_IP...${NC}"

# Step 1: Package application files
echo -e "${YELLOW}Packaging application...${NC}"
tar -czf deploy_package.tar.gz backend compose.yaml || {
	echo -e "${RED}Failed to package files.${NC}"
	exit 1
}

# Step 2: Upload to server
echo -e "${YELLOW}Uploading package to server...${NC}"
scp -i ~/.ssh/id_ed25519 deploy_package.tar.gz $SERVER_USER@$SERVER_IP:$DEPLOY_PATH || {
	echo -e "${RED}Failed to upload package.${NC}"
	exit 1
}

# Step 3: SSH into server and deploy
echo -e "${YELLOW}Deploying application on server...${NC}"
ssh $SERVER_USER@$SERVER_IP <<EOF
  set -e

  echo -e "${YELLOW}Navigating to deployment directory...${NC}"
  cd $DEPLOY_PATH

  echo -e "${YELLOW}Extracting package...${NC}"
  tar -xzf deploy_package.tar.gz && rm deploy_package.tar.gz || { echo -e "${RED}Failed to extract package.${NC}"; exit 1; }

  echo -e "${YELLOW}Restarting Docker containers...${NC}"
  docker compose down || { echo -e "${RED}Failed to stop containers.${NC}"; exit 1; }
  docker compose up -d --build || { echo -e "${RED}Failed to start containers.${NC}"; exit 1; }

  echo -e "${GREEN}Deployment complete!${NC}"
EOF

# Step 4: Cleanup local package
echo -e "${YELLOW}Cleaning up local files...${NC}"
rm deploy_package.tar.gz || {
	echo -e "${RED}Failed to clean up local files.${NC}"
	exit 1
}

echo -e "${GREEN}Deployment finished successfully!${NC}"
