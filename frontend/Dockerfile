FROM node:12.16.1-stretch-slim

WORKDIR /app/
COPY . .
RUN npm install

RUN npm run build

EXPOSE 5000

CMD ["npm", "run", "start-docker"]
#CMD ["npm", "run", "dev"]