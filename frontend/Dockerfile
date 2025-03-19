# Use Node.js LTS version as base image
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all files
COPY . .

# Build the app if it's a production build
RUN npm run build

# Expose port
EXPOSE 3000

# Start the application
CMD ["npm", "start"]