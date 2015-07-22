FROM fedora:latest
RUN dnf -y install tree man man-pages make gcc rpm-build
WORKDIR /root/rpmbuild
ENTRYPOINT ["rpmbuild", "-bb", "-v"]
