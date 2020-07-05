FROM python:3

WORKDIR /moex

COPY . .
RUN pip install .

ENTRYPOINT ["python",  "moex-analyzer"]