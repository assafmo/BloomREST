FROM python:2.7

COPY ingest.py /src/

RUN pip install pybloomfiltermmap

ENTRYPOINT ["python", "/src/ingest.py"]
CMD ["file.bloom", "100000", "0.0000001"]
