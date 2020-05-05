FROM node:12.16.1-stretch-slim

WORKDIR /app/
COPY . .
RUN npm install

EXPOSE 35729
EXPOSE 5000

CMD ["npm", "run", "dev"]