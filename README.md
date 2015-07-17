# Simple RPM

This repository demonstrates how to build a simple RPM (with the help of Docker)

## Build Docker Image

`docker build -t integralist/simplerpm .`

## Run Docker Container

`docker run integralist/simplerpm`

> Save changes inside container:  
> `docker commit <running_container_id> integralist/simplerpm:<tag>`

## Generate RPM

`rpmbuild -bb -v integralist-0.0.1-1.spec`

> RPM filename convention:  
> `<package_name>-<version_number>-<release_number>.spec`

## Other Commands

- `rpm -q  <package>`: check if package is installed
- `whereis <command>`: check binary location
- `man rpmbuild`: documentation for building an RPM

## Notes

I was using http://www.tldp.org/HOWTO/RPM-HOWTO/build.html as my reference and this suggested using `Copyright` within the header section; but this caused the `rpmbuild` command to throw an error because it didn't recognise that particular key. Instead I swapped it for `License` and that seemed to work OK.

More importantly, it seems I was forced to build the RPM from a specific directory, i.e. `~/rpmbuild`. Originally I created the relevant RPM directory structure within the folder `~/testing-rpmbuild` and when I ran the `rpmbuild` command it automatically created `~/rpmbuild` for me and then started to fail as my spec file (which was in `~/testing-rpmbuild`) had referenced other files outside of `~/rpmbuild` which at that point in time was empty. So in the end I just moved all my files from `~/testing-rpmbuild` to `~/rpmbuild` and everything worked fine. But I'm not sure how you're expected to build multiple different RPMs when you're restricted to a single `~/rpmbuild` directory?
