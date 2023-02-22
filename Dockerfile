FROM ahmad88me/pytadahdtentity:latest
WORKDIR /app
RUN mkdir /app/src
COPY src/*.cpp /app/src/
COPY src/*.h /app/src/
COPY src/*.cxx /app/src/
COPY *.py /app/
COPY src/*.i  /app/src/
COPY tada_hdt_entity /app/tada_hdt_entity
COPY requirements.txt /app/
COPY tests /app/tests
COPY scripts /app/scripts/
COPY .git /app/.git
#RUN sh scripts/start.sh
CMD ["sh", "scripts/start.sh"]