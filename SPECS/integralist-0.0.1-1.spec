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
# This is a macro that is supposed to run before the install section
# But seemingly never does?

%install
# You install your software into the temporary "Build Root"
# There's an automated check for the directory: /root/rpmbuild/BUILDROOT/integralist-0.0.1-1.x86_64
# If the directory exists, then remove it and recreate it (so you have an empty folder)
cp %{SOURCE0} %{buildroot}/$(basename %{SOURCE0})
cp ./generated-appfile %{buildroot}/generated-appfile

%post
echo "POST"
# This is a macro that runs after the install section
pwd
ls

%clean
rm ./generated-appfile

%files
# "This section is mandatory: it states the files that should be included in the binary package"
# "Listed below (in the spec file that is) are the files we'll add to the binary package"
/testapp
/generated-appfile

# Although the files section is after the install step,
# the install step uses this to confirm its content matches

%changelog
* Thu Jul 16 2015 Mark McDonnell <mark.mcdx@gmail.com>
- Initial setup of spec file to test building an RPM
