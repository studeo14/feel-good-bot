FROM python:3 as intermediate
WORKDIR /usr/src/app
COPY requirements.txt ./
run mkdir /pips/
ENV PYTHONUSERBASE /pips/
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3
WORKDIR /usr/src/app
COPY --from=intermediate /pips /pips
COPY scripts/run_app.sh .
COPY scripts/real_envs.sh .
RUN mkdir src
COPY src/app.py src/
COPY src/utils.py src/
ENV PYTHONUSERBASE /pips/
ENV PATH $PYTHONUSERBASE/bin:$PATH
CMD ./run_app.sh

