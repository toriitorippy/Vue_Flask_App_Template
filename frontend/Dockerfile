
FROM node:10.13.0

WORKDIR /frontend

COPY . /frontend

RUN yarn install

EXPOSE 80

CMD ["yarn", "run", "serve"]