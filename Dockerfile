FROM chambm/wine-dotnet:wine7-net4.8-x64 AS voiceroid2

COPY ./assets /assets

RUN wine winecfg -v win10

RUN wine /assets/VOICEROID2/akane_aoi/Setup.exe /silent

RUN rm -rf /assets

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

FROM voiceroid2

RUN \
  --mount=type=cache,target=/var/lib/apt/lists \
  --mount=type=cache,target=/var/cache/apt/archives \
    apt-get update && apt-get install -y \
    curl \
    git

# install python3 and pip
ENV PYTHON_VERSION 3.10.4
ENV WINEPATH "C:\python3;C:\python3\Scripts"

RUN curl \
    https://www.python.org/ftp/python/${PYTHON_VERSION}/python-${PYTHON_VERSION}-embed-win32.zip \
    -o /tmp/python3-win32.zip
RUN unzip /tmp/python3-win32.zip -d /wineprefix64/drive_c/python3

RUN curl https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py
RUN wine python /tmp/get-pip.py
RUN sed -i  -e 's/#i/i/g' /wineprefix64/drive_c/python3/python*._pth 

# setup library and server
WORKDIR /usr/src/app
RUN git clone https://github.com/Nkyoku/pyvcroid2.git
RUN cd pyvcroid2 && wine python setup.py install

RUN git clone https://github.com/s10akir/voiceroid_tts_server.git
RUN cd voiceroid_tts_server && wine pip install -r requirements.txt

# run server
WORKDIR /usr/src/app/voiceroid_tts_server
EXPOSE 8000

CMD ["wine", "uvicorn", "main:app", "--host", "0.0.0.0"]
