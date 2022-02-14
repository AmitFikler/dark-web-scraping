FROM node:14.18.0-alpine
WORKDIR /dark-app-client
COPY package.json ./
COPY package-lock.json ./
RUN npm install
COPY . .
CMD ["npm", "start"]