FROM fedora:latest
RUN yum -y install tree man man-pages make gcc rpm-build
WORKDIR $HOME
ADD . rpmbuild/
RUN mv /rpmbuild $HOME/rpmbuild
