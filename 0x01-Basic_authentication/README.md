# 0x01. Basic authentication

![](https://docs.oracle.com/cd/E19879-01/819-3669/images/security-httpBasicAuthentication.gif)

## Background Context

In this project, you will learn what the authentication process means and implement a  **Basic Authentication**  on a simple API.

In the industry, you should  **not**  implement your own Basic authentication system and use a module or framework that doing it for you (like in Python-Flask:  [Flask-HTTPAuth](https://intranet.hbtn.io/rltoken/XvXTZnSvVYaLaWtAWcTkYQ "Flask-HTTPAuth")). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/5/6ccb363443a8f301bc2bc38d7a08e9650117de7c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210823%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210823T074934Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=02a9e0e74a6cd73fbaf46a457cd16c7ee2275be088e536793c8c025481412e33)

## Resources

**Read or watch**:

-   [REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY)

-   [Base64 in Python](docs.python.org/3.7/library/base64.html)

-   [HTTP header Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)

-   [Flask](https://palletsprojects.com/p/flask/)

-   [Base64 - concept](https://en.wikipedia.org/wiki/Base64)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone **without the help of Google**:

### General

-   What authentication means
-   What Base64 is
-   How to encode a string in Base64
-   What Basic authentication means
-   How to send the Authorization header

