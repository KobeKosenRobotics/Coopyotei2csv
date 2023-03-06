FROM python:3.10

RUN apt update && \
    apt install -y git default-jre vim curl wget && \
    pip install --upgrade pip && \
    pip install numpy scipy matplotlib openpyxl pandas tabula tabula-py && \
    apt update && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo "succesfully"

WORKDIR /home