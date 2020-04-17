FROM ahmad88me/pytadahdtentity:latest
WORKDIR /app
COPY *.cpp /app/
COPY *.h /app/
COPY *.cxx /app/
COPY *.py /app/
COPY *.i  /app/
COPY tada_hdt_entity /app/tada_hdt_entity
COPY requirements.txt /app/
COPY scripts /app/scripts/
RUN sh scripts/start.sh
