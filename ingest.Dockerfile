FROM python:2.7

COPY ingest.py /src/

RUN pip install pybloomfiltermmap

EXPOSE 4096

WORKDIR /data/

ENTRYPOINT ["python", "/src/ingest.py"]
CMD ["file.bloom", "100000", "0.0000001"]
