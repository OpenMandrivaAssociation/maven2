%{?_javapackages_macros:%_javapackages_macros}
%global main_pkg maven

Name:	    maven2
Version:	2.2.1
Release:	50.4
Summary:	Java project management and project comprehension tool
Group:		Development/Java
License:	ASL 2.0 and MIT and BSD
URL:		https://maven.apache.org

# export https://svn.apache.org/repos/asf/maven/maven-2/tags/maven-%{version}/ apache-maven-%{version}
# tar czvf %{name}-%{version}.tar.gz apache-maven-%{version}
Source0:	%{name}-%{version}.tar.gz

Patch2:     %{name}-%{version}-update-tests.patch
Patch4:     %{name}-%{version}-unshade.patch
Patch5:     %{name}-%{version}-default-resolver-pool-size.patch
Patch6:     %{name}-%{version}-strip-jackrabbit-dep.patch
Patch8:     %{name}-%{version}-migrate-to-plexus-containers-container-default.patch

BuildRequires: java-devel >= 1.6.0

BuildRequires: apache-resource-bundles
BuildRequires: objectweb-asm
BuildRequires: buildnumber-maven-plugin
BuildRequires: bsh
BuildRequires: jsch
BuildRequires: apache-commons-codec
BuildRequires: jakarta-commons-httpclient
BuildRequires: apache-commons-io
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-logging
BuildRequires: apache-commons-cli
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-parent
BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-shade-plugin
BuildRequires: maven-install-plugin
BuildRequires: modello
BuildRequires: plexus-containers
BuildRequires: plexus-containers-container-default


BuildArch: noarch

%description
Apache Maven is a software project management and comprehension tool. Based on
the concept of a project object model (POM), Maven can manage a project's
build, reporting and documentation from a central piece of information.

%package -n maven-artifact
Summary:        Compatibility Maven artifact artifact

%description -n maven-artifact
Maven artifact manager artifact

%package -n maven-artifact-manager
Summary:        Compatibility Maven artifact manager artifact

%description -n maven-artifact-manager
Maven artifact manager artifact

%package -n maven-error-diagnostics
Summary:        Compatibility Maven error diagnostics artifact

%description -n maven-error-diagnostics
Maven error diagnostics artifact

%package -n maven-model
Summary:        Compatibility Maven model artifact

%description -n maven-model
Maven model artifact

%package -n maven-monitor
Summary:        Compatibility Maven monitor artifact

%description -n maven-monitor
Maven monitor artifact

%package -n maven-plugin-registry
Summary:        Compatibility Maven plugin registry artifact

%description -n maven-plugin-registry
Maven plugin registry artifact

%package -n maven-profile
Summary:        Compatibility Maven profile artifact

%description -n maven-profile
Maven profile artifact

%package -n maven-project
Summary:        Compatibility Maven project artifact

%description -n maven-project
Maven project artifact

%package -n maven-settings
Summary:        Compatibility Maven settings artifact

%description -n maven-settings
Maven settings artifact

%package -n maven-toolchain
Summary:        Compatibility Maven toolchain artifact

%description -n maven-toolchain
Maven toolchain artifact

%package -n maven-plugin-descriptor
Summary:        Maven Plugin Description Model

%description -n maven-plugin-descriptor
Maven toolchain artifact

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.


%prep
%setup -q -n apache-maven-2.2.1

%patch2 -p1 -b .update-tests

%patch4 -p1 -b .unshade

# disable parallel artifact resolution
%patch5 -p1 -b .parallel-artifacts-resolution

# remove unneeded jackrabbit dependency
%patch6 -p1 -b .strip-jackrabbit-dep

%patch8 -p1 -b .plexus-container

for nobuild in apache-maven maven-artifact-test \
               maven-compat maven-core maven-plugin-api \
               maven-plugin-parameter-documenter maven-reporting \
               maven-repository-metadata maven-script; do
    %pom_disable_module $nobuild
done

# Don't install parent POM
%mvn_package :maven __noinstall

# Install all artifacts in Maven 3 directory.
%mvn_file ":{*}" %{main_pkg}/@1

# these parts are compatibility versions which are available in
# maven-3.x as well. We default to maven-3, but if someone asks for
# 2.x we provide few compat versions
%mvn_compat_version ":maven-{artifact,model,settings}" \
                    2.0.2 2.0.6 2.0.7 2.0.8 2.2.1

# Don't depend on backport-util-concurrent
%pom_remove_dep :backport-util-concurrent
%pom_remove_dep :backport-util-concurrent maven-artifact-manager
sed -i s/edu.emory.mathcs.backport.// `find -name DefaultArtifactResolver.java`

# Tests are skipped, so remove dependencies with scope 'test'.
for pom in $(grep -l ">test<" $(find -name pom.xml | grep -v /test/)); do
    %pom_xpath_remove "pom:dependency[pom:scope[text()='test']]" $pom
done

%build
%mvn_build -f -s -- -P all-models

%install
%mvn_install

%files -n maven-artifact -f .mfiles-maven-artifact
%doc LICENSE.txt NOTICE.txt

%files -n maven-artifact-manager -f .mfiles-maven-artifact-manager
%doc LICENSE.txt NOTICE.txt

%files -n maven-error-diagnostics -f .mfiles-maven-error-diagnostics
%doc LICENSE.txt NOTICE.txt

%files -n maven-model -f .mfiles-maven-model
%doc LICENSE.txt NOTICE.txt

%files -n maven-monitor -f .mfiles-maven-monitor
%doc LICENSE.txt NOTICE.txt

%files -n maven-plugin-registry -f .mfiles-maven-plugin-registry
%doc LICENSE.txt NOTICE.txt

%files -n maven-profile -f .mfiles-maven-profile
%doc LICENSE.txt NOTICE.txt

%files -n maven-project -f .mfiles-maven-project
%doc LICENSE.txt NOTICE.txt

%files -n maven-settings -f .mfiles-maven-settings
%doc LICENSE.txt NOTICE.txt

%files -n maven-toolchain -f .mfiles-maven-toolchain
%doc LICENSE.txt NOTICE.txt

%files -n maven-plugin-descriptor -f .mfiles-maven-plugin-descriptor
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt


%changelog
* Fri Oct 31 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-50
- Remove direct dependency on classworlds

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-48
- Add missing BR: modello

* Tue Sep 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-47
- Remove code related to bootstrapping
- Remove empty-dep JAR and POM
- Remove local depmap
- Use mfiles to simplify %%files sections
- Remove handling of custom settings.xml
- Build with XMvn

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 Michal Srb <msrb@redhat.com> - 2.2.1-45
- Add missing BR: maven-install-plugin (Resolves: #979504)
- Migrate to plexus-containers-container-default

* Wed Apr 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-44
- Don't depend on plexus-container-default
- Unset M2_HOME before calling mvn-rpmbuild
- Remove test dependencies

* Mon Mar 11 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-43
- Rebuild to generate mvn(*) versioned provides

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.2.1-41
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Nov 23 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-40
- Add license to javadoc subpackage

* Thu Nov 22 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-39
- Add license and notice files to packages
- Add javadoc subpackage

* Fri Nov  9 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-38
- Don't depend on backport-util-concurrent

* Mon Aug 20 2012 Michel Salim <salimma@fedoraproject.org> - 2.2.1-37
- Provide compatibility versions for maven-artifact and -settings

* Thu Jul 26 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-36
- Remove mistaken epoch use in requires

* Wed Jul 25 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-35
- Move artifacts together with maven-3 files
- Provide compatibility versions for maven-model

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May  9 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-33
- Completely remove main package since it was just confusing

* Wed Jan 25 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-32
- Stip down maven 2 to bare minimum
- Remove scripts and most of home

* Mon Jan 23 2012 Tomas Radej <tradej@redhat.com> - 2.2.1-31
- Fixed Requires for plugin-descriptor

* Mon Jan 23 2012 Tomas Radej <tradej@redhat.com> - 2.2.1-30
- Moved plugin-descriptor into subpackage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 11 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-28
- Provide mvn2 script instead of mvn (maven provides that now)

* Tue Jul 19 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-27
- Add maven-error-diagnostics subpackage
- Order subpackages according to alphabet

* Tue Jul 19 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-26
- Unown jars contained in subpackages (#723124)

* Mon Jun 27 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-25
- Add maven-toolchain subpackage

* Fri Jun 24 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-24
- Add few new subpackages
- Add several missing requires to new subpackages

* Fri Jun 24 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-23
- Split artifact-manager and project into subpackages
- Fix resolver to process poms and fragments from datadir
- No more need to update_maven_depmap after this update

* Mon Apr 18 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-22
- Fix jpp script to limit maven2.jpp.mode scope

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 19 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-20
- Add maven-artifact-test to installation

* Tue Jan 18 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-19
- Print plugin collector debug output only when maven2.jpp.debug mode is on

* Wed Dec 22 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-18
- Add xml-commons-apis to lib directory
- fixes NoClassDefFoundError org/w3c/dom/ElementTraversal

* Fri Dec 10 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-17
- Add conditional BRs to enable ff merge between f14 and f15
- Remove jackrabbit dependency from pom files

* Fri Dec 10 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-16
- Fix installation of pom files for artifact jars

* Mon Nov 22 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-15
- Add apache-commons-parent to BR/R
- Rename BRs from jakarta-commons to apache-commons

* Thu Nov 11 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-14
- Remove old depmaps from -depmap.xml file
- Fix argument quoting for mvn scripts (Resolves rhbz#647945)

* Mon Sep 20 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-13
- Create dangling symlinks during install (Resolves rhbz#613866)

* Fri Sep 17 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-12
- Update JPackageRepositoryLayout to handle "signature" packaging

* Mon Sep 13 2010 Yong Yang <yyang@redhat.com> 2.2.1-11
- Add -P all-models to generate maven model v3

* Wed Sep 1 2010 Alexander Kurtakov <akurtako@redhat.com> 2.2.1-10
- Remove buildnumber-maven-plugins deps now that is fixed.
- Use new package names in BR/R.
- Use global instead of define.

* Fri Aug 27 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-9
- Remove failing tests after maven-surefire 2.6 update

* Thu Aug 26 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-8
- Remove incorrect testcase failing with ant 1.8
- Cleanup whitespace

* Tue Jun 29 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-7
- Updated previous patch to only modify behaviour in JPP mode

* Mon Jun 28 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-6
- Disable parallel artifact resolution

* Wed Jun 23 2010 Yong Yang <yyang@redhat.com> 2.2.1-5
- Add Requires: maven-enforcer-plugin

* Fri Jun 18 2010 Deepak Bhole <dbhole@redhat.com> 2.2.1-4
- Final non-bootstrap build against non-bootstrap maven

* Fri Jun 18 2010 Deepak Bhole <dbhole@redhat.com> 2.2.1-3
- Added buildnumber plugin requirements
- Rebuild in non-bootstrap

* Thu Jun 17 2010 Deepak Bhole <dbhole@redhat.com> - 0:2.2.1-2
- Added support for dumping mapping info (in debug mode)
- Add a custom depmap
- Added empty-dep
- Added proper requirements
- Fixed classworlds jar name used at runtime
- Install individual components
- Install poms and mappings
- Remove non maven items from shaded uber jar
- Create dependency links in $M2_HOME/lib at install time

* Thu Nov 26 2009 Deepak Bhole <dbhole@redhat.com> - 0:2.2.1-1
- Initial bootstrap build
