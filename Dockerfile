FROM fedora:latest
RUN yum check-update
RUN yum update
RUN yum install tree man man-pages make gcc rpm-build
WORKDIR $HOME
ADD . rpmbuild/
