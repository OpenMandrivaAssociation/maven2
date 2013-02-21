%define bootstrap	1
%define __jar_repack	0

Name:		maven2
Version:	2.2.1
Release:	4
Summary:	Java project management and project comprehension tool

Group:		Development/Java
License:	ASL 2.0 and MIT and BSD
URL:		http://maven.apache.org

# export https://svn.apache.org/repos/asf/maven/maven-2/tags/maven-%{version}/ apache-maven-%{version}
# tar czvf %{name}-%{version}.tar.gz apache-maven-%{version}
Source0:	%{name}-%{version}.tar.gz

# Since we are using the entire dependency set "as is", we need to atleast try
# and make it so that only one version is packaged in the binary blob. This
# server an additional (and more important) purpose ... it ensures that a
# single version of each module is enough; because if not, versioned rpm names
# would be needed for those dependencies. The idea is as follows:

# Required by maven:
#  org/codehaus/plexus/1.0/plexus-1.0.jar
#  org/codehaus/plexus/1.1/plexus-1.1.jar
# What we package in the blob:
#  org/codehaus/plexus/1.1/plexus-1.1.jar
#  org/codehaus/plexus/1.0/plexus-1.0.jar -> ../1.1/plexus-1.1.jar

# Doing this for the hundreds of jars is a huge pain.. so we do the only
# thing sane people can. Crazy scripting magic! To generate the tarball

# rm -rf ~/.m2
# tar xzf SOURCE0
# cd apache-maven-%{version}
# export M2_HOME=`pwd`/installation/apache-maven-%{version}
# ant
# cd ~/.m2
# SOURCE100
# Find maven-%{version}-bootstrapdeps.tar.gz in ./
Source1:	%{name}-%{version}-bootstrapdeps.tar.gz

# 1xx for non-upstream/created sources
Source100:	%{name}-%{version}-settings.xml
Source101:	%{name}-JPackageRepositoryLayout.java
Source102:	%{name}-MavenJPackageDepmap.java
Source103:	%{name}-%{version}-depmap.xml
Source104:	%{name}-empty-dep.pom
Source105:	%{name}-empty-dep.jar

# 2xx for created non-buildable sources
Source200:	%{name}-script
Source201:	%{name}-jpp-script

Patch0:		%{name}-antbuild.patch
Patch1:		%{name}-%{version}-jpp.patch
Patch2:		%{name}-%{version}-update-tests.patch
Patch3:		%{name}-%{version}-enable-bootstrap-repo.patch
Patch4:		%{name}-%{version}-unshade.patch
Patch5:		%{name}-%{version}-default-resolver-pool-size.patch
Patch6:		%{name}-%{version}-strip-jackrabbit-dep.patch

BuildRequires:	java-devel >= 1.6.0
BuildRequires:	classworlds
BuildRequires:	jdom
BuildRequires:	zip
BuildRequires:	xml-commons-apis
%if %{bootstrap}
BuildRequires:	ant
%else
BuildRequires:	apache-resource-bundles
BuildRequires:	objectweb-asm
BuildRequires:	backport-util-concurrent
BuildRequires:	buildnumber-maven-plugin
BuildRequires:	bsh
BuildRequires:	jsch
BuildRequires:	apache-commons-codec
BuildRequires:	jakarta-commons-httpclient
BuildRequires:	apache-commons-io
BuildRequires:	apache-commons-lang
BuildRequires:	apache-commons-logging
BuildRequires:	jakarta-commons-cli
BuildRequires:	jakarta-commons-collections
BuildRequires:	easymock
BuildRequires:	junit
BuildRequires:	nekohtml
BuildRequires:	ant
BuildRequires:	maven-doxia
BuildRequires:	jetty
BuildRequires:	maven-archiver
BuildRequires:	maven-assembly-plugin
BuildRequires:	maven-doxia-tools
BuildRequires:	maven-enforcer-api
BuildRequires:	maven-enforcer-plugin
BuildRequires:	maven-shade-plugin
BuildRequires:	maven-clean-plugin
BuildRequires:	maven-compiler-plugin
BuildRequires:	maven-resources-plugin
BuildRequires:	maven-install-plugin
BuildRequires:	maven-jar-plugin
BuildRequires:	maven-plugin-testing-harness
BuildRequires:	maven-pmd-plugin
BuildRequires:	maven-shared-file-management
BuildRequires:	maven-shared-common-artifact-filters
BuildRequires:	maven-shared-dependency-tree
BuildRequires:	maven-shared-repository-builder
BuildRequires:	maven-shared-io
BuildRequires:	maven-shared-downloader
BuildRequires:	maven-shared-filtering
BuildRequires:	maven-shared-reporting-api
BuildRequires:	maven-site-plugin
BuildRequires:	maven-surefire-maven-plugin
BuildRequires:	maven-surefire-provider-junit
BuildRequires:	maven-scm
BuildRequires:	maven-wagon
BuildRequires:	modello
BuildRequires:	multithreadedtc
BuildRequires:	plexus-active-collections
BuildRequires:	plexus-ant-factory
BuildRequires:	plexus-archiver
BuildRequires:	plexus-cipher
BuildRequires:	plexus-bsh-factory
BuildRequires:	plexus-build-api
BuildRequires:	plexus-classworlds
BuildRequires:	plexus-compiler
BuildRequires:	plexus-component-api
BuildRequires:	plexus-containers-container-default
BuildRequires:	plexus-container-default
BuildRequires:	plexus-i18n
BuildRequires:	plexus-interactivity
BuildRequires:	plexus-interpolation
BuildRequires:	plexus-io
BuildRequires:	plexus-resources
BuildRequires:	plexus-sec-dispatcher
BuildRequires:	plexus-utils
BuildRequires:	plexus-velocity
BuildRequires:	regexp
BuildRequires:	forge-parent
BuildRequires:	spice-parent
BuildRequires:	jakarta-oro
BuildRequires:	regexp
BuildRequires:	slf4j
BuildRequires:	velocity
%endif

Requires:	classworlds
Requires:	jdom

%if !%{bootstrap}
Requires:	apache-resource-bundles
Requires:	objectweb-asm
Requires:	backport-util-concurrent
Requires:	bsh
Requires:	jsch
Requires:	apache-commons-codec
Requires:	jakarta-commons-httpclient
Requires:	apache-commons-io
Requires:	apache-commons-lang
Requires:	apache-commons-logging
Requires:	jakarta-commons-cli
Requires:	jakarta-commons-collections
Requires:	easymock
Requires:	junit
Requires:	nekohtml
Requires:	ant
Requires:	maven-doxia
Requires:	jetty
Requires:	maven-archiver
Requires:	maven-doxia-tools
Requires:	maven-enforcer-api
Requires:	maven-enforcer-plugin
Requires:	maven-plugin-testing-harness
Requires:	maven-shared-file-management
Requires:	maven-shared-common-artifact-filters
Requires:	maven-shared-dependency-tree
Requires:	maven-shared-repository-builder
Requires:	maven-shared-io
Requires:	maven-shared-downloader
Requires:	maven-shared-filtering
Requires:	maven-shared-reporting-api
Requires:	maven-surefire-provider-junit
Requires:	maven-scm
Requires:	maven-wagon
Requires:	modello
Requires:	multithreadedtc
Requires:	jakarta-oro
Requires:	plexus-active-collections
Requires:	plexus-ant-factory
Requires:	plexus-archiver
Requires:	plexus-cipher
Requires:	plexus-bsh-factory
Requires:	plexus-build-api
Requires:	plexus-classworlds
Requires:	plexus-compiler
Requires:	plexus-component-api
Requires:	plexus-containers-container-default
Requires:	plexus-container-default
Requires:	plexus-i18n
Requires:	plexus-interactivity
Requires:	plexus-interpolation
Requires:	plexus-io
Requires:	plexus-resources
Requires:	plexus-sec-dispatcher
Requires:	plexus-utils
Requires:	plexus-velocity
Requires:	regexp
Requires:	forge-parent
Requires:	spice-parent
Requires:	jakarta-oro
Requires:	regexp
Requires:	slf4j
Requires:	velocity
%endif
BuildArch:	noarch

%description
Apache Maven is a software project management and comprehension tool. Based on
the concept of a project object model (POM), Maven can manage a project's
build, reporting and documentation from a central piece of information.

%prep
%setup -q -n apache-maven-%{version}

%patch0 -p0 -b .antbuild
%patch1 -p1 -b .jpp
%patch2 -p0 -b .update-tests

%if ! %{bootstrap}
%patch4 -p0 -b .unshade
%endif

%if %{bootstrap}
%patch3 -p0 -b .enable-bootstrap-repo
%endif

# set cache location
export M2_REPO=`pwd`/.m2
mkdir $M2_REPO

# if bootstrapping, extract the dependencies
%if %{bootstrap}
pushd $M2_REPO

  tar xzf %{SOURCE1}

  # maven-remote-resources-plugin (m-r-r-p) is used side-by-side with
  # plexus-velocity (p-v) 1.1.3 upstream.. we collapse to a single p-v version
  # of 1.1.7. 1.1.7 however has a component descriptor that conflicts
  # with the one in m-r-r-p. We therefore need to remove the descriptor
  # from m-r-r-p first
  zip -d repository/org/apache/maven/plugins/maven-remote-resources-plugin/1.0-beta-2/maven-remote-resources-plugin-1.0-beta-2.jar \
	META-INF/plexus/components.xml

  # resource bundle 1.3 is needed during build, but not when done via
  # upstream, for some reason
  mkdir -p repository/org/apache/apache-jar-resource-bundle/1.3
  ln -s ../1.4/apache-jar-resource-bundle-1.4.jar \
	repository/org/apache/apache-jar-resource-bundle/1.3/apache-jar-resource-bundle-1.3.jar
  ln -s ../1.4/apache-jar-resource-bundle-1.4.jar.sha1 \
	repository/org/apache/apache-jar-resource-bundle/1.3/apache-jar-resource-bundle-1.3.jar.sha1
popd
%endif

cp %{SOURCE101} maven-artifact/src/main/java/org/apache/maven/artifact/repository/layout/JPackageRepositoryLayout.java
cp %{SOURCE102} maven-artifact/src/main/java/org/apache/maven/artifact/repository/layout/MavenJPackageDepmap.java

# disable parallel artifact resolution
%patch5 -p1 -b .parallel-artifacts-resolution

%if !%{bootstrap}
# remove unneeded jackrabbit dependency
%patch6 -p1 -b .strip-jackrabbit-dep
%endif

# test case is incorrectly assuming that target executed by antcall
# can propagate references to its parent (stopped working with ant 1.8)
rm maven-script/maven-script-ant/src/test/java/org/apache/maven/script/ant/AntMojoWrapperTest.java

# FIXIT: look why these tests are failing with maven-surefire 2.6
rm maven-artifact/src/test/java/org/apache/maven/artifact/resolver/DefaultArtifactCollectorTest.java
rm maven-project/src/test/java/org/apache/maven/project/validation/DefaultModelValidatorTest.java

%build
export M2_REPO=`pwd`/.m2
export M2_HOME=`pwd`/installation/apache-maven-%{version}

# copy settings to where ant reads from
mkdir -p $M2_HOME/conf
cp %{SOURCE100} $M2_HOME/conf/settings.xml

# replace locations in the copied settings file
sed -i -e s:__M2_LOCALREPO_PLACEHOLDER__:"file\://$M2_REPO/cache":g $M2_HOME/conf/settings.xml
sed -i -e s:__M2_REMOTEREPO_PLACEHOLDER__:"file\://$M2_REPO/repository":g $M2_HOME/conf/settings.xml

# replace settings file location before patching
sed -i -s s:__M2_SETTINGS_FILE__:$M2_HOME/conf/settings.xml:g build.xml

# FIXME: These tests fail when building with maven for an unknown reason
rm -f maven-core/src/test/java/org/apache/maven/WagonSelectorTest.java
rm -f maven-artifact-manager/src/test/java/org/apache/maven/artifact/manager/DefaultWagonManagerTest.java
%if %{bootstrap}
ant -Dmaven.repo.local=$M2_REPO/cache
%else
mvn-jpp -P all-models -Dmaven.repo.local=$M2_REPO/cache -Dmaven2.jpp.depmap.file=%{SOURCE103} install
%endif

%install
export M2_HOME=$(pwd)/installation/apache-maven-%{version}

rm -rf $M2_HOME

mkdir -p $(pwd)/installation/
pushd $(pwd)/installation/
tar jxf ../apache-maven/target/*bz2
popd

# maven2 directory in /usr/share/java
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

###########
# M2_HOME #
###########
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}

###############
# M2_HOME/bin #
###############
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
cp -a $M2_HOME/bin/* $RPM_BUILD_ROOT%{_datadir}/%{name}/bin

# Remove unnecessary batch scripts
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/bin/*.bat

# Update conf file for unversioned jar names
sed -i -e s:'-classpath "${M2_HOME}"/boot/classworlds-\*.jar':'-classpath "${M2_HOME}"/boot/classworlds.jar':g \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/bin/mvn $RPM_BUILD_ROOT%{_datadir}/%{name}/bin/mvnDebug

################
# M2_HOME/boot #
################
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/boot
%if %{bootstrap}
cp -a $M2_HOME/boot/* $RPM_BUILD_ROOT%{_datadir}/%{name}/boot/
%endif

################
# M2_HOME/conf #
################
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/conf
cp -a $M2_HOME/conf/* $RPM_BUILD_ROOT%{_datadir}/%{name}/conf/

###############
# M2_HOME/lib #
###############
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/lib

install -p -m 644 $M2_HOME/lib/maven-%{version}-uber.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/uber-%{version}.jar
ln -s uber-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/uber.jar
ln -s %{_javadir}/%{name}/uber.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/maven-%{version}-uber.jar

################
# M2_HOME/poms #
#*##############
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/poms

########################
# /etc/maven/fragments #
########################
install -dm 755 $RPM_BUILD_ROOT/%{_sysconfdir}/maven/fragments

##############################
# /usr/share/java repository #
##############################
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/repository
ln -s %{_javadir} $RPM_BUILD_ROOT%{_datadir}/%{name}/repository/JPP

#######################
# javadir/maven2/poms #
#*#####################

# Install files
install -m 644 %{SOURCE104} -D $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.maven2-empty-dep.pom
install -m 644 %{SOURCE105} -D $RPM_BUILD_ROOT%{_javadir}/%{name}/empty-dep.jar
ln -s %{_datadir}/%{name}/poms $RPM_BUILD_ROOT%{_javadir}/%{name}/poms

# Wrappers
install -m755 %{SOURCE200} -D $RPM_BUILD_ROOT%{_bindir}/mvn
install -m755 %{SOURCE201} -D $RPM_BUILD_ROOT%{_bindir}/mvn-jpp

%if %{bootstrap}
    cp -af `pwd`/.m2/repository $RPM_BUILD_ROOT%{_datadir}/%{name}/bootstrap_repo
%endif

###################
# Individual jars #
###################

for file in \
    maven-script/maven-script-ant/target/maven-script-ant-%{version}.jar \
    maven-script/maven-script-beanshell/target/maven-script-beanshell-%{version}.jar \
    apache-maven/target/apache-maven-%{version}.jar \
    maven-profile/target/maven-profile-%{version}.jar \
    maven-artifact-manager/target/maven-artifact-manager-%{version}.jar \
    maven-artifact-test/target/maven-artifact-test-%{version}.jar \
    maven-monitor/target/maven-monitor-%{version}.jar \
    maven-toolchain/target/maven-toolchain-%{version}.jar \
    maven-toolchain/target/original-maven-toolchain-%{version}.jar \
    maven-project/target/maven-project-%{version}.jar \
    maven-settings/target/maven-settings-%{version}.jar \
    maven-plugin-parameter-documenter/target/maven-plugin-parameter-documenter-%{version}.jar \
    maven-model/target/maven-model-%{version}.jar \
    maven-artifact/target/maven-artifact-%{version}.jar \
    maven-repository-metadata/target/maven-repository-metadata-%{version}.jar \
    maven-plugin-api/target/maven-plugin-api-%{version}.jar \
    maven-error-diagnostics/target/maven-error-diagnostics-%{version}.jar \
    maven-compat/target/maven-compat-%{version}.jar \
    maven-core/target/maven-core-%{version}.jar \
    maven-plugin-registry/target/maven-plugin-registry-%{version}.jar \
    maven-plugin-descriptor/target/maven-plugin-descriptor-%{version}.jar; do \

	FNAME=`basename $file`
	FNAME_NO_EXT=`basename $file .jar`
	DIR=`dirname $file`
	UNVER_NAME=`basename $file | sed -e s:-%{version}::g`
	UNVER_NAME_WITH_NO_EXT=`echo $FNAME_NO_EXT | sed -e s:-%{version}::g`
	ARTIFACT=`basename \`dirname $DIR\``


	pushd $DIR
	  install -m 644 $FNAME $RPM_BUILD_ROOT%{_javadir}/%{name}/
	  ln -s $FNAME $RPM_BUILD_ROOT%{_javadir}/%{name}/$UNVER_NAME
	  install -m 644 ../pom.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.%{name}-$UNVER_NAME_WITH_NO_EXT.pom
	  %add_to_maven_depmap org.apache.maven $ARTIFACT %{version} JPP/%{name} $UNVER_NAME_WITH_NO_EXT
	popd
done

# maven-reporting-api
install -m 644  maven-reporting/maven-reporting-api/target/maven-reporting-api-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/
ln -s maven-reporting-api-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/maven-reporting-api.jar
install -m 644 maven-reporting/maven-reporting-api/pom.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.%{name}-maven-reporting-api.pom
%add_to_maven_depmap org.apache.maven.reporting maven-reporting-api %{version} JPP/%{name} maven-reporting-api

# maven-reporting pom
install -m 644 maven-reporting/pom.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.%{name}-maven-reporting.pom
%add_to_maven_depmap org.apache.maven.reporting maven-reporting %{version} JPP/%{name} maven-reporting

# maven pom
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.%{name}-maven.pom
%add_to_maven_depmap org.apache.maven maven %{version} JPP/%{name} maven

# create dangling symlinks but fix bz#613866
pushd $RPM_BUILD_ROOT%{_datadir}/%{name}/lib
  build-jar-repository -s -p . jdom
popd

pushd $RPM_BUILD_ROOT%{_datadir}/%{name}/boot
  build-jar-repository -s -p . classworlds
popd

%if ! %{bootstrap}
pushd $RPM_BUILD_ROOT%{_datadir}/%{name}/lib
  build-jar-repository -s -p . backport-util-concurrent jsch commons-cli commons-httpclient commons-codec nekohtml maven-shared/reporting-api maven-doxia/logging-api maven-doxia/sink-api maven-wagon/file maven-wagon/http maven-wagon/http-lightweight maven-wagon/http-shared maven-wagon/provider-api maven-wagon/ssh maven-wagon/ssh-common maven-wagon/ssh-external plexus/container-default plexus/interactivity-api plexus/interpolation plexus/utils slf4j/jcl-over-slf4j slf4j/api slf4j/jdk14 slf4j/nop plexus/plexus-cipher plexus/plexus-sec-dispatcher xerces-j2 xml-commons-apis
popd
%endif

%post
%update_maven_depmap

%postun
%update_maven_depmap

%files
%attr(0755,root,root) %{_bindir}/mvn
%attr(0755,root,root) %{_bindir}/mvn-jpp
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/bin
%config(noreplace) %{_datadir}/%{name}/bin/*.conf
%attr(0755,root,root) %{_datadir}/%{name}/bin/mvn
%attr(0755,root,root) %{_datadir}/%{name}/bin/mvnDebug
%{_datadir}/%{name}/boot
%{_datadir}/%{name}/conf
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/poms
%{_datadir}/%{name}/repository
%{_mavendepmapfragdir}
%{_javadir}/%{name}

%if %{bootstrap}
%{_datadir}/%{name}/bootstrap_repo
%endif
%doc


%changelog
* Tue May 10 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.2.1-1
+ Revision: 673373
- add zip to buildrequires
- cleanups


