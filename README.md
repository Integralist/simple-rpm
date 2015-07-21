# Simple RPM

This repository demonstrates how to build a simple RPM (with the help of Docker)

## Build Docker Image

`docker build -t integralist/simplerpm .`

## Run Docker Container

`docker run -v $(pwd):/root/rpmbuild integralist/simplerpm SPECS/integralist-0.0.1-1.spec`

If you want to debug the running container:

> `docker run -v $(pwd):/root/rpmbuild -it --entrypoint=/bin/bash integralist/simplerpm`

If you want to save changes inside container:  

> `docker commit <running_container_id> integralist/simplerpm:<tag>`

## Generating the RPM

The RPM filename convention is:  

> `<package_name>-<version_number>-<release_number>.spec`

Once built, your mounted work directory should look something like:

```bash
.
├── BUILD
├── BUILDROOT
│   └── integralist-0.0.1-1.x86_64
│       ├── generated-appfile
│       └── testapp
├── Dockerfile
├── Makefile
├── README.md
├── RPMS
│   └── x86_64
│       └── integralist-0.0.1-1.x86_64.rpm
├── SOURCES
│   └── testapp
├── SPECS
│   └── integralist-0.0.1-1.spec
└── SRPMS
```

## Other Commands

If you want to have a poke around inside the container while it's running:

- `rpm -q  <package>`: check if package is installed
- `whereis <command>`: check binary location
- `man rpmbuild`: documentation for building an RPM
