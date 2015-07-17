# Simple RPM

This repository demonstrates how to build a simple RPM (with the help of Docker)

## Build Docker Image

`docker build -t integralist/simplerpm .`

## Run Docker Container

`docker run -it integralist/simplerpm bash`

> Save changes inside container:  
> `docker commit <running_container_id> integralist/simplerpm:<tag>`

## Generate RPM

- `cd $HOME/rpmbuild`
- `rpmbuild -bb -v SPECS/integralist-0.0.1-1.spec`

> RPM filename convention:  
> `<package_name>-<version_number>-<release_number>.spec`

Once built, running `tree` should display something like:

```bash
.
|-- BUILD
|-- BUILDROOT
|   `-- integralist-0.0.1-1.x86_64
|       |-- generated-appfile
|       `-- testapp
|-- Dockerfile
|-- Makefile
|-- README.md
|-- RPMS
|   `-- x86_64
|       `-- integralist-0.0.1-1.x86_64.rpm
|-- SOURCES
|   `-- testapp
|-- SPECS
|   `-- integralist-0.0.1-1.spec
`-- SRPMS
```

## Other Commands

- `rpm -q  <package>`: check if package is installed
- `whereis <command>`: check binary location
- `man rpmbuild`: documentation for building an RPM

## Notes

### Spec file

I was using http://www.tldp.org/HOWTO/RPM-HOWTO/build.html as my reference and this suggested using `Copyright` within the header section; but this caused the `rpmbuild` command to throw an error because it didn't recognise that particular key. Instead I swapped it for `License` and that seemed to work OK.

### Build directory

More importantly, it seems I was forced to build the RPM from a specific directory, i.e. `~/rpmbuild`. Originally I created the relevant RPM directory structure within the folder `~/testing-rpmbuild` and when I ran the `rpmbuild` command it automatically created `~/rpmbuild` for me and then started to fail as my spec file (which was in `~/testing-rpmbuild`) had referenced other files outside of `~/rpmbuild` which at that point in time was empty. So in the end I just moved all my files from `~/testing-rpmbuild` to `~/rpmbuild` and everything worked fine. But I'm not sure how you're expected to build multiple different RPMs when you're restricted to a single `~/rpmbuild` directory?

### Dockerfile

The following contents of the dockerfile do not work as I expected them to:

```Dockerfile
WORKDIR $HOME
ADD . rpmbuild/
```

I would've expected this to have set the working directory to `/root/` and then added the contents to `/root/rpmbuild`; but it doesn't, it adds it to `/rpmbuild` instead? So this means I have to then move the folder separately:

```Dockerfile
RUN mv /rpmbuild $HOME/rpmbuild
```

It also means when you run the container you have to manually execute `cd $HOME/rpmbuild` as well instead of being dropped into the location I was expecting. Maybe someone can help clarify this for me.
