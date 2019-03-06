FROM python:3 as intermediate
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r /src/requirements.txt
RUN python3 -m site


# COPY . .
# ENV BOT_ID
# ENV ACCESS_TOKEN
# ENV GROUP_ID

