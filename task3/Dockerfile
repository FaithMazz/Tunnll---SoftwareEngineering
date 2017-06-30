
#Dockerfile

#From directive instructing base image to build upon
FROM python:3.5-onbuild

#Copy startup script into known file location in container
COPY start.sh /start.sh

#Expose port 8000 to allow communication to/from server
EXPOSE 8000

#CMD specifies the command to execute to start the server running.
CMD ["/start.sh"]

#done
