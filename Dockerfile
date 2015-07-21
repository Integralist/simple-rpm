FROM fedora:latest
RUN yum -y install tree man man-pages make gcc rpm-build
WORKDIR /root/rpmbuild
ENTRYPOINT ["rpmbuild"]
CMD ["-bb", "-v", "SPECS/*.spec"]
