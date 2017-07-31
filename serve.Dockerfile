FROM python:2.7

COPY serve.py /src/

RUN pip install pybloomfiltermmap

EXPOSE 4096

ENTRYPOINT ["python", "/src/serve.py"]
CMD ["/data/file.bloom", "4096"]
