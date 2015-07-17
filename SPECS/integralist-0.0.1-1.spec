Summary: A test package to see how rpmbuild works
Name: integralist
Version: 0.0.1
Release: 1
License: None
Group: None
Source0: testapp
BuildRoot: /var/tmp/%{name}-buildroot

%description
A longer description of the package we're building
The working directory (pwd) for each step (prep/build etc) is /root/rpmbuild/BUILD
The %{buildroot} and $RPM_BUILD_ROOT are always the directory /root/rpmbuild/BUILDROOT/integralist-0.0.1-1.x86_64

%prep
# This is used to get the sources ready to build
# Here you need to do anything necessary to get the sources setup like they need to be

# Note:
# The prep section has two macros available: setup and patch (both prefixed with a percentage sign)
# The macros have their own flags/options and execute commands based on a directory/file convention
# You don't need to use prep in order to use setup or patch; they're added as two separate sections

%build
# Compile any files/binaries needed to be added to your RPM (added via the install section)
make tester -f ../Makefile

%pre
# This is a macro that is supposed to run before the 'install' step
# But seemingly never does?

%install
# You install your software into the temporary "BUILDROOT" directory
# /root/rpmbuild/BUILDROOT/integralist-0.0.1-1.x86_64
# So for us, "installing" is simply copying the relevant files into the "BUILDROOT" directory
cp %{SOURCE0} %{buildroot}/$(basename %{SOURCE0})
cp ./generated-appfile %{buildroot}/generated-appfile

# Note:
# The install step has an automated check for the "BUILDROOT" directory
# You can see this when using the -v flag for verbose output
# Effectively it checks to see if the directory exists and then removes/recreates it
# This leaves you with an empty folder to "install" your files into (as demonstrated above)

%post
# This is a macro that runs after the 'install' step

%clean
# This is a macro that runs after the 'post' step
rm ./generated-appfile

%files
# The 'files' step is mandatory: it states which files should be included in the binary package
# Listed below are the files we'll add to the binary package
# They need to be absolute paths and interestingly seems to be 'scoped' to the "buildroot" directory
/testapp
/generated-appfile

# Although the 'files' step is after the 'install' step,
# the 'install' step uses 'files' to confirm the content matches
# If they don't match (e.g. you don't "install" testapp or generated-appfile) then the build will fail

# Note:
# There are other directives you can use under 'files' which are things like:
# %attr(<mode>, <user>, <group>) file
# %defattr(<file mode>, <user>, <group>, <dir mode>)
# %ghost file
# %verify
# For full details see: http://www.rpm.org/max-rpm-snapshot/s1-rpm-inside-files-list-directives.html

%changelog
* Fri Jul 17 2015 Mark McDonnell <mark.mcdx@gmail.com>
- Cleaned up the descriptions in the spec file

* Thu Jul 16 2015 Mark McDonnell <mark.mcdx@gmail.com>
- Initial setup of spec file to test building an RPM
