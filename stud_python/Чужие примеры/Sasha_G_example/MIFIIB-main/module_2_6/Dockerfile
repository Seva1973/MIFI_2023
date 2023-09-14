FROM php:7.4-apache
#WORKDIR /var/www/html
LABEL Alexandr Ganitev, module 2.6 <g.alexanders@gmail.com>
RUN apt-get clean && apt-get update
RUN docker-php-ext-install mysqli pdo pdo_mysql
