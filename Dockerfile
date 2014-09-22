FROM ubuntu:trusty

RUN sudo apt-get update

RUN sudo apt-get install -y git wget make libtool automake pkg-config python-pip

### PyTox Install

# installing libsodium, needed for Core
RUN git clone https://github.com/jedisct1/libsodium.git
RUN cd libsodium && git checkout tags/0.7.0 && ./autogen.sh && ./configure --prefix=/usr && make && make install

# installing libopus, needed for audio encoding/decoding
RUN wget http://downloads.xiph.org/releases/opus/opus-1.0.3.tar.gz
RUN tar xzf opus-1.0.3.tar.gz
RUN cd opus-1.0.3 && ./configure && make && make install

# installing vpx
RUN apt-get install -y yasm
RUN git clone http://git.chromium.org/webm/libvpx.git
RUN cd libvpx && ./configure --enable-shared && make && make install

# creating librarys' links and updating cache
RUN ldconfig
RUN git clone https://github.com/irungentoo/ProjectTox-Core.git toxcore
RUN cd toxcore && autoreconf -i
RUN cd toxcore && ./configure --prefix=/usr --disable-tests --disable-ntox
RUN cd toxcore && make
RUN cd toxcore && make install

# PyTox
RUN git clone https://github.com/aitjcize/PyTox.git PyTox
RUN apt-get install -y python-dev
RUN cd PyTox && pip install .

### Serve the Toxin front end
RUN apt-get install -y apache2 nodejs nodejs-legacy npm
RUN npm install -g bower
ADD toxin-client /srv/app
RUN cd /srv/app && yes | bower install --allow-root

### Supervisor
RUN apt-get install -y supervisor

ADD etc /etc

CMD ["/usr/bin/supervisord"]

EXPOSE 80

