
FROM node:10.13.0

WORKDIR /frontend

COPY . /frontend

# RUN npm install -g npm && \
#     npm install -g vue-cli
RUN yarn install

EXPOSE 80

# Run app.py when the container launches
CMD ["yarn", "run", "serve"]