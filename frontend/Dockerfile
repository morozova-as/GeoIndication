FROM node:12.16.1-stretch-slim

WORKDIR /app/
COPY package*.json ./
RUN npm install

COPY src .

EXPOSE 5000

CMD ["npm", "run", "start"]