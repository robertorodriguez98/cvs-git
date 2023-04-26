FROM debian
RUN apt-get update && apt-get install -y cvs && apt-get clean && rm -rf /var/lib/apt/lists/*
ENV CVSROOT /var/cvsroot
ENV proyecto myproject
ENV vendor myvendor
ENV release myrelease
VOLUME ["/var/cvsroot"]
RUN mkdir /var/cvsroot && chmod 1777 /var/cvsroot && cvs init
RUN mkdir sourcedir && cd sourcedir && cvs import -m "Initial import" $proyecto $vendor $release

FROM alpine
RUN apk update && apk add cvs cvsd busybox-extras && rm -rf /var/cache/apk/*
ENV CVSROOT /var/cvsroot
ENV proyecto myproject
ENV vendor myvendor
ENV release myrelease
RUN mkdir /var/lib/cvs
VOLUME ["/var/lib/cvs"]
RUN chmod 1777 /var/cvsroot && cvs -d /var/cvsroot init
RUN mkdir sourcedir && cd sourcedir && cvs import -m "Initial import" $proyecto $vendor $release




