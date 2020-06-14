FROM python:3

WORKDIR /moex

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python",  "./main_moex_analysis.py"]