# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define _with_gcj_support 1
%define gcj_support %{?_with_gcj_support:1}%{!?_with_gcj_support:%{?_without_gcj_support:0}%{!?_without_gcj_support:%{?_gcj_support:%{_gcj_support}}%{!?_gcj_support:0}}}

%define with_itests %{!?_with_itests:0}%{?_with_itests:1}
%define without_itests %{?_with_itests:0}%{!?_with_itests:1}

%define _with_bootstrap 1
%define with_bootstrap %{!?_with_bootstrap:0}%{?_with_bootstrap:1}
%define without_bootstrap %{?_with_bootstrap:0}%{!?_with_bootstrap:1}

%define maven_version   2.0.4
%define NONFREE 0

%define base_name maven
%define name maven2

%define repo_dir m2_home_local/repository
%define maven_settings_file %{_builddir}/%{name}/settings.xml

Name:           %{name}
Version:        %{maven_version}
Release:        %mkrel 10.6.7
Epoch:          0
Summary:        Java project management and project comprehension tool

Group:          Development/Java
License:        Apache Software License
URL:            http://maven.apache.org/

# svn export http://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.4 maven2
# tar czf maven2-src.tar.gz maven2
Source0:        %{name}-src.tar.gz

# svn export -r {2006-04-20} http://svn.apache.org/repos/asf/maven/plugins/trunk maven2-plugins
# tar czf maven2-plugins-060420-src.tar.gz maven2-plugins
Source2:        %{name}-plugins-060420-src.tar.gz

# No source location for these. They are ascii files generated from maven
# repositories, and are not in cvs/svn
# The files were originally aquired from: http://repo1.maven.org/maven2/
Source3:        m2_pom_repo.tar.gz

# As with above, these files are from the maven repositories, and are not in 
# cvs/svn
# The files were originally aquired from: http://repo1.maven.org/maven2/
Source4:        m2_jar_repo.tar.gz
Source5:        %{name}-script

Source6:        maven2-JPackageRepositoryLayout.java
Source7:        maven2-settings.xml

# svn export -r '{2006-03-08}' http://svn.apache.org/repos/asf/maven/plugins/trunk/maven-site-plugin maven-site-plugin
# tar czf maven2-maven-site-plugin.tar.gz maven-site-plugin 
Source8:        %{name}-maven-site-plugin.tar.gz

Source9:          %{name}-run-it-tests.sh

# svn export http://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.4/maven-model
# cd maven-model
# mvn -P all-models package 
# Find model jar in target/maven-model-2.0.4.jar
Source10:       %{name}-model-v3.jar
Source11:        %{name}-MavenJPackageDepmap.java
Source12:        %{name}-addjdom-depmap.xml
Source13:        %{name}-empty-dep.pom

# Empty jar file with just a manifest. No source destination to specify
Source14:        %{name}-empty-dep.jar
Source15:        %{name}-jpp-script
Source16:        %{name}-jpp-readme.html

# Based on http://maven.apache.org/guides/mini/guide-bash-m2-completion.html
Source17:        %{name}-bash-completion

Patch0:          maven2-disable-itests.patch
Patch1:          maven2-addjdomtobootstrappath.patch
Patch2:          maven2-plugins-plexus151.patch
Patch3:          %{name}-jpprepolayout.patch
Patch4:          %{name}-plugins-disablecglib.patch
Patch5:          %{name}-buildallplugins.patch
Patch6:          %{name}-enable-unbuilt-modules.patch
Patch7:          %{name}-fastjar-manifest-fix.patch
Patch8:          %{name}-noexternaljavadoclinks.patch 
Patch9:          %{name}-ant17.patch

BuildRequires:    jpackage-utils >= 0:1.7.2
BuildRequires:    java-1.7.0-icedtea
BuildRequires:    ant >= 1.6.5
BuildRequires:    antlr >= 2.7.4
BuildRequires:    bsh >= 1.3.0
#BuildRequires:   cglib >= 2.1.0
BuildRequires:    checkstyle >= 4.1
BuildRequires:    classworlds >= 1.1
%if %{NONFREE}
BuildRequires:    clover
%endif
BuildRequires:    dom4j >= 1.6.1
BuildRequires:    tomcat5-servlet-2.4-api
BuildRequires:  geronimo-specs
BuildRequires:    gnu.regexp >= 1.1.4
BuildRequires:    httpunit >= 1.6
BuildRequires:    jakarta-commons-beanutils >= 1.7.0
BuildRequires:    jakarta-commons-cli >= 1.0
BuildRequires:    jakarta-commons-collections >= 3.1
BuildRequires:    jakarta-commons-io >= 1.1
BuildRequires:    jakarta-commons-lang >= 2.1
BuildRequires:    jakarta-commons-logging >= 1.0.4
BuildRequires:    jakarta-commons-validator >= 1.1.4
BuildRequires:    jaxen >= 1.1
BuildRequires:    jdom >= 1.0
#BuildRequires:   jmock >= 1.0.1
BuildRequires:    jline >= 0.8.1
BuildRequires:    jsch >= 0.1.20
BuildRequires:    jtidy >= 1.0
BuildRequires:    junit >= 3.8.2
BuildRequires:    maven2-common-poms >= 1.0-4
BuildRequires:    maven-doxia >= 1.0-0.a7.3
BuildRequires:    maven-jxr >= 1.0-2
BuildRequires:    maven-surefire >= 1.5.3-2
BuildRequires:    maven-surefire-booter >= 1.5.3-2
BuildRequires:    maven-wagon >= 1.0
BuildRequires:    nekohtml >= 0.9.3
BuildRequires:    oro >= 2.0.8
BuildRequires:    plexus-ant-factory >= 1.0-0.a1.2
BuildRequires:    plexus-bsh-factory >= 1.0-0.a7s.2
BuildRequires:    plexus-archiver >= 1.0-0.a6
BuildRequires:    plexus-compiler >= 1.5.1
BuildRequires:    plexus-container-default >= 1.0
BuildRequires:    plexus-i18n >= 1.0
BuildRequires:    plexus-interactivity >= 1.0
BuildRequires:    plexus-utils >= 1.2
BuildRequires:    plexus-velocity >= 1.1.2
BuildRequires:    pmd >= 3.6
BuildRequires:    qdox >= 1.5
BuildRequires:    rhino >= 1.5
BuildRequires:    saxon-scripts
BuildRequires:    velocity >= 1.4
BuildRequires:    xerces-j2 >= 2.7.1
BuildRequires:    xalan-j2 >= 2.6.0

%if %{with_itests}
BuildRequires:    log4j >= 1.2.13
BuildRequires:    xml-commons-apis >= 1.3.02
%endif

%if %{without_bootstrap}
BuildRequires:    %{name} = %{epoch}:%{version}
BuildRequires:    maven2-plugin-assembly
BuildRequires:    maven2-plugin-clean
BuildRequires:    maven2-plugin-compiler
BuildRequires:    maven2-plugin-install
BuildRequires:    maven2-plugin-jar
BuildRequires:    maven2-plugin-javadoc
BuildRequires:    maven2-plugin-plugin
BuildRequires:    maven2-plugin-release
BuildRequires:    maven2-plugin-resources
BuildRequires:    maven2-plugin-site
BuildRequires:    maven2-plugin-surefire
BuildRequires:    maven-scm >= 0:1.0-0.b3.2
BuildRequires:    maven-scm-test >= 0:1.0-0.b3.2
BuildRequires:    maven-shared-file-management >= 1.0-4
BuildRequires:    maven-shared-plugin-testing-harness >= 1.0-4
BuildRequires:  modello >= 1.0-0.a8.3
BuildRequires:    modello-maven-plugin >= 1.0-0.a8.3
%endif

Requires:        ant >= 1.6.5
Requires:        antlr >= 2.7.4
Requires:        bsh >= 1.3.0
#Requires:       cglib >= 2.1.0
Requires:        checkstyle >= 4.1
Requires:        classworlds >= 1.
Requires(post):  classworlds >= 1.1
%if %{NONFREE}
Requires:        clover
%endif
Requires:        dom4j >= 1.6.1
Requires:        tomcat5-servlet-2.4-api
Requires:        gnu.regexp >= 1.1.4
Requires:        httpunit >= 1.6
Requires:        jakarta-commons-beanutils >= 1.7.0
Requires:        jakarta-commons-cli >= 1.0
Requires(post):  jakarta-commons-cli >= 1.0
Requires:        jakarta-commons-collections >= 3.1
Requires:        jakarta-commons-io >= 1.1
Requires:        jakarta-commons-lang >= 2.1
Requires(post):  jakarta-commons-lang >= 2.1
Requires:        jakarta-commons-logging >= 1.0.4
Requires(post):  jakarta-commons-logging >= 1.0.4
Requires:        jakarta-commons-validator >= 1.1.4
Requires:        jaxen >= 1.1
Requires:        jdom >= 1.0
Requires(post):  jdom >= 1.0
#Requires:       jmock >= 1.0.1
Requires:        jline >= 0.8.1
Requires:        jsch >= 0.1.20
Requires(post):  jsch >= 0.1.20
Requires:        jtidy >= 1.0
Requires:        junit >= 3.8.2
Requires:        maven2-common-poms >= 1.0-4
Requires:        maven-doxia >= 1.0-0.a7.3
Requires(post):  maven-doxia >= 1.0-0.a7.3
Requires:        maven-jxr >= 1.0
Requires:        maven-surefire >= 1.5.3-2
Requires:        maven-surefire-booter >= 1.5.3-2
Requires:        maven-wagon >= 1.0
Requires(post):  maven-wagon >= 1.0
Requires:        nekohtml >= 0.9.3
Requires:        oro >= 2.0.8
Requires:        plexus-ant-factory >= 1.0-0.a1.2
Requires:        plexus-bsh-factory >= 1.0-0.a7s.2
Requires:        plexus-archiver >= 1.0-0.a6
Requires:        plexus-compiler >= 1.5.1
Requires:        plexus-container-default >= 1.0
Requires(post):  plexus-container-default >= 1.0
Requires:        plexus-i18n >= 1.0
Requires:        plexus-interactivity >= 1.0
Requires(post):  plexus-interactivity >= 1.0
Requires:        plexus-utils >= 1.2
Requires(post):  plexus-utils >= 1.2
Requires:        plexus-velocity >= 1.1.2
Requires:        pmd >= 3.6
Requires:        qdox >= 1.5
Requires:        rhino >= 1.5
Requires:        velocity >= 1.4
Requires:        xerces-j2 >= 2.7.1
Requires:        xalan-j2 >= 2.6.0

%if %{without_bootstrap}
Requires:        maven-scm >= 0:1.0-0.b3.2
Requires:        maven-scm-test >= 0:1.0-0.b3.2
Requires:        maven-shared-file-management >= 1.0-4
Requires:        maven-shared-plugin-testing-harness >= 1.0-4
Requires:        modello >= 1.0-0.a8.3
Requires:        modello-maven-plugin >= 1.0-0.a8.3
%endif

Requires(post):    jpackage-utils >= 0:1.7.2
Requires(postun):  jpackage-utils >= 0:1.7.2

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%if ! %{gcj_support}
BuildArch:      noarch
%endif

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
ExcludeArch:         ppc64
%endif

%description
Maven is a software project management and comprehension tool. Based on the 
concept of a project object model (POM), Maven can manage a project's build,
reporting and documentation from a central piece of information.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java

%description    javadoc
%{summary}.

%package        manual
Summary:        Documents for %{name}
Group:          Development/Java

%description    manual
%{summary}.

%package        plugin-ant
Summary:        Ant plugin for maven
Group:          Development/Java
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-ant
Generates an Ant build file for the project.

%package        plugin-antlr
Summary:        Antlr plugin for maven
Group:          Development/Java
Requires:       antlr >= 2.7.4
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-antlr
Generates sources from an Antlr grammar.

%package        plugin-antrun
Summary:        Antrun plugin for maven
Group:          Development/Java
Requires:       ant >= 1.6.5
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-antrun
Runs a set of ant tasks from a phase of the build.


%package        plugin-assembly
Summary:        Assembly plugin for maven
Group:          Development/Java
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}
%if %{without_bootstrap}
Requires:       modello >= 1.0-0.a8.3
%endif
Requires:       plexus-archiver >= 1.0
Requires:       plexus-utils >= 1.2

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-assembly
Builds an assembly (distribution) of sources and/or binaries.


%package        plugin-checkstyle
Summary:        Checkstyle plugin for maven
Group:          Development/Java
Requires:       checkstyle >= 4.1
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}
Requires:       plexus-utils >= 1.2
Requires:       plexus-velocity >= 1.1.2

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-checkstyle
Generates a checkstyle report.


%package        plugin-clean
Summary:        Clean plugin for maven
Group:          Development/Java
Requires:       junit >= 3.8.2
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}
Requires:       plexus-utils >= 1.2

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-clean
Cleans up files generated during build.

%if %{NONFREE}
%package        plugin-clover
Summary:        Clover plugin for maven
Group:          Development/Java
Requires:       ant >= 1.6.5
Requires:       jmock >= 1.0.1
Requires:       junit >= 3.8.2
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}
Requires:       plexus-compiler >= 1.5.1

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-clover
Generates a Clover report.
%endif


%package        plugin-compiler
Summary:        Compiler plugin for maven
Group:          Development/Java
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}
Requires:       plexus-compiler >= 1.5.1
Requires:       plexus-utils >= 1.2

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-compiler
Compiles Java sources.


%package        plugin-dependency
Summary:        Dependency plugin for maven
Group:          Development/Java
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}
Requires:       plexus-archiver >= 1.0
Requires:       plexus-utils >= 1.2

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-dependency
The dependency plugin provides the capability to manipulate artifacts. It can
copy and/or unpack artifacts from local or remote repositories to a specified
location.


%package        plugin-deploy
Summary:        Deploy plugin for maven
Group:          Development/Java
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-deploy
Deploys the built artifacts to a remote repository.


%package        plugin-ear
Summary:        Ear plugin for maven
Group:          Development/Java
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}
Requires:       plexus-utils >= 1.2

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-ear
Generates an EAR from the current project.


%package        plugin-eclipse
Summary:        Eclipse plugin for maven
Group:          Development/Java
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}
Requires:       plexus-utils >= 1.2

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-eclipse
Generates an Eclipse project file for the current project.


%package        plugin-ejb
Summary:        Ejb plugin for maven
Group:          Development/Java
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-ejb
Builds an EJB (and optional client) from the current project.


%package        plugin-help
Summary:        Help plugin for maven
Group:          Development/Java
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-help
Gets information about the working environment for the project.


%package        plugin-idea
Summary:        Idea plugin for maven
Group:          Development/Java
Requires:       dom4j >= 1.6.1
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}
Requires:       maven-wagon >= 1.0
Requires:       plexus-utils >= 1.2

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-idea
Creates/updates an IDEA workspace for the current project 
(individual modules are created as IDEA modules).


%package        plugin-install
Summary:        Install plugin for maven
Group:          Development/Java
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-install
Installs the built artifact into the local repository.


%package        plugin-jar
Summary:        Jar plugin for maven
Group:          Development/Java
Requires:       jakarta-commons-lang >= 2.1
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-jar
Builds a JAR from the current project.


%package        plugin-javadoc
Summary:        Javadoc plugin for maven
Group:          Development/Java
Requires:       jakarta-commons-lang >= 2.1
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}
%if %{without_bootstrap}
Requires:       modello >= 1.0-0.a8.3
%endif
Requires:       plexus-archiver >= 1.0

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-javadoc
Generates Javadoc for the project.


%package        plugin-jxr
Summary:        Jxr plugin for maven
Group:          Development/Java
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-jxr
Generate a source cross reference.


%package        plugin-one
Summary:        One plugin for maven
Group:          Development/Java
Requires:       junit >= 3.8.2
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}
Requires:       plexus-archiver >= 1.0
Requires:       plexus-utils >= 1.2

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-one
A plugin for interacting with legacy Maven 1.x repositories and builds.


%package        plugin-plugin
Summary:        Plugin plugin for maven
Group:          Development/Java
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-plugin
Creates a Maven plugin descriptor for any Mojo's found in the source tree, 
to include in the JAR.


%package        plugin-pmd
Summary:        Pmd plugin for maven
Group:          Development/Java
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}
Requires:       plexus-utils >= 1.2
Requires:       pmd >= 3.3

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-pmd
Generates a PMD report.


%package        plugin-project-info-reports
Summary:        Project-info-reports plugin for maven
Group:          Development/Java
Requires:       httpunit >= 1.6
Requires:       jakarta-commons-validator >= 1.1.4
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}
Requires:       plexus-i18n >= 1.0

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-project-info-reports
Generates standard project reports.

%package        plugin-rar
Summary:        Rar plugin for maven
Group:          Development/Java
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-rar
Builds a RAR from the current project.

%package        plugin-release
Summary:        Release plugin for maven
Group:          Development/Java
#Requires:       jmock >= 1.0.1
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}
Requires:       plexus-interactivity >= 1.0

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-release
Releases the current project - updating the POM and tagging in the SCM.

%package        plugin-repository
Summary:        Repository plugin for maven
Group:          Development/Java
Requires:       junit >= 3.8.2
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}
Requires:       plexus-archiver >= 1.0

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-repository
Plugin to help with repository-based tasks.

%package        plugin-resources
Summary:        Resources plugin for maven
Group:          Development/Java
Requires:       jakarta-commons-io >= 1.1
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-resources
Copies the resources to the output directory for including in the JAR.

%package        plugin-site
Summary:        Site plugin for maven
Group:          Development/Java
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}
Requires:       maven-doxia >= 1.0
Requires:       plexus-utils >= 1.2

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-site
Generates a site for the current project.

%package        plugin-source
Summary:        Source plugin for maven
Group:          Development/Java
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}
Requires:       plexus-archiver >= 1.0
Requires:       plexus-container-default >= 1.0

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-source
Builds a JAR of sources for use in IDEs and distribution to the repository.

%package        plugin-surefire
Summary:        Surefire plugin for maven
Group:          Development/Java
Requires:       junit >= 3.8.2
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}
Requires:       maven-surefire >= 1.5.2
Requires:       maven-surefire-booter >= 1.5.2
Requires:       plexus-utils >= 1.2

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-surefire
Runs the Junit tests in an isolated classloader.

%package        plugin-surefire-report
Summary:        Surefire report plugin for maven
Group:          Development/Java
Requires:       junit >= 3.8.2
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}
Requires:       maven-surefire >= 1.5.2
Requires:       maven-surefire-booter >= 1.5.2
Requires:       plexus-utils >= 1.2

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-surefire-report
Generates a report based on the results of unit tests.

%package        plugin-verifier
Summary:        Verifier plugin for maven
Group:          Development/Java
Requires:       junit >= 3.8.2
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}
%if %{without_bootstrap}
Requires:       modello >= 1.0-0.a8.3
%endif
Requires:       plexus-utils >= 1.2

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-verifier
Useful for integration tests - verifies the existence of certain conditions.

%package        plugin-war
Summary:        War plugin for maven
Group:          Development/Java
Requires:       maven2 = %{epoch}:%{version}-%{release}
Requires(postun): maven2 = %{epoch}:%{version}-%{release}
Requires:       plexus-utils >= 1.2

%if %{gcj_support}
BuildRequires:       java-gcj-compat-devel
%endif

%description    plugin-war
Builds a WAR from the current project.

%prep
%setup -q -c -n %{name}

# Extract the plugins
tar xzf %{SOURCE2}

# Use an older version of site plugin because newer one requires newer doxia 
# (1.0a8) which is not compatible with the older one (1.0a7) which is needed 
# by other parts of maven
rm -rf maven2-plugins/maven-site-plugin
tar xzf %{SOURCE8}

# Remove dependencies on org.codehaus.doxia.* (it is now
# org.apache.maven.doxia, and in the interest of maintaining just one
# doxia jar, we substitute things accordingly)

for i in     maven2-plugins/maven-plugin-plugin/src/main/java/org/apache/maven/plugin/plugin/PluginReport.java \
            maven2-plugins/maven-checkstyle-plugin/src/main/java/org/apache/maven/plugin/checkstyle/CheckstyleReport.java \
            maven2-plugins/maven-checkstyle-plugin/src/main/java/org/apache/maven/plugin/checkstyle/CheckstyleReportGenerator.java \
            maven2-plugins/maven-pmd-plugin/src/main/java/org/apache/maven/plugin/pmd/AbstractPmdReport.java \
            maven2-plugins/maven-pmd-plugin/src/main/java/org/apache/maven/plugin/pmd/PmdReport.java \
            maven2-plugins/maven-pmd-plugin/src/main/java/org/apache/maven/plugin/pmd/PmdReportListener.java \
            maven2-plugins/maven-pmd-plugin/src/main/java/org/apache/maven/plugin/pmd/CpdReportGenerator.java \
            maven2-plugins/maven-pmd-plugin/src/main/java/org/apache/maven/plugin/pmd/CpdReport.java \
            maven2-plugins/maven-surefire-report-plugin/src/main/java/org/apache/maven/plugins/surefire/report/SurefireReportGenerator.java \
            maven2-plugins/maven-surefire-report-plugin/src/main/java/org/apache/maven/plugins/surefire/report/SurefireReportMojo.java; do

    sed -i -e s:org.codehaus.doxia.sink.Sink:org.apache.maven.doxia.sink.Sink:g $i
    sed -i -e s:org.codehaus.doxia.site.renderer.SiteRenderer:org.apache.maven.doxia.siterenderer.Renderer:g $i
    sed -i -r -e s:\(\\s+\)SiteRenderer\(\\s+\):\\1Renderer\\2:g $i
done

# Remove existing binaries from source trees
#find . -name "*.jar" -exec rm -f '{}' \;

%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav
%patch3 -b .sav
%patch4 -b .sav
%patch5 -b .sav
%patch6 -b .sav
%patch7 -b .sav
%patch8 -b .sav
%patch9 -b .sav

# FIXME: Maven eclipse plugin tests are disabled for now, until a way
# is found to stop it from connecting to the web despite offline mode.
rm -rf maven2-plugins/maven-eclipse-plugin/src/test/*

# FIXME: Disabled items:

#Disabled goal (because we don't want a jetty dependency)
rm -f maven2-plugins/maven-site-plugin/src/main/java/org/apache/maven/plugins/site/SiteRunMojo.java

# Disabled test because it needs cglib
rm -f maven2-plugins/maven-release-plugin/src/test/java/org/apache/maven/plugins/release/PrepareReleaseMojoTest.java

# extract poms and jars (if any)
tar xzf %{SOURCE3}

# extract jars iff in bootstrap mode
%if %{with_bootstrap}
tar xzf %{SOURCE4}
%endif

# Copy model-v3
cp -p %{SOURCE10} m2_repo/repository/JPP/maven2/model-v3.jar

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

cp -p %{SOURCE6} maven2/maven-artifact/src/main/java/org/apache/maven/artifact/repository/layout/JPackageRepositoryLayout.java
cp -p %{SOURCE11} maven2/maven-artifact/src/main/java/org/apache/maven/artifact/repository/layout/MavenJPackageDepmap.java

# FIXME: bootstrap-mini has no dependencies, so we copy the file there 
# (for now). Since bootstrap classes are not in the final package, there 
# will be no duplicates.
mkdir -p maven2/bootstrap/bootstrap-mini/src/main/java/org/apache/maven/artifact/repository/layout/
cp -p %{SOURCE11} maven2/bootstrap/bootstrap-mini/src/main/java/org/apache/maven/artifact/repository/layout/MavenJPackageDepmap.java

cp -p %{SOURCE7} %{maven_settings_file}
sed -i -e "s|<url>__INTERNAL_REPO_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" %{maven_settings_file}

%if %{with_bootstrap}
sed -i -e "s|<url>__EXTERNAL_REPO_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" %{maven_settings_file}
%else
sed -i -e "s|<url>__EXTERNAL_REPO_PLACEHOLDER__</url>|<url>file://%{_datadir}/%{name}/repository</url>|g" %{maven_settings_file}
%endif

sed -i -e "s|__INTERNAL_REPO_PLACEHOLDER__|file://`pwd`/m2_repo/repository|g" maven2/bootstrap/bootstrap-mini/src/main/java/org/apache/maven/bootstrap/download/OnlineArtifactDownloader.java

%if %{with_bootstrap}
sed -i -e "s|__EXTERNAL_REPO_PLACEHOLDER__|file://`pwd`/external_repo|g" maven2/bootstrap/bootstrap-mini/src/main/java/org/apache/maven/bootstrap/download/OnlineArtifactDownloader.java
%else
sed -i -e "s|__EXTERNAL_REPO_PLACEHOLDER__|file://%{_datadir}/%{name}/repository|g" maven2/bootstrap/bootstrap-mini/src/main/java/org/apache/maven/bootstrap/download/OnlineArtifactDownloader.java
%endif

# Copy the empty dependency jar/pom in place
mkdir -p m2_repo/repository/JPP/maven2/default_poms
cp -p %{SOURCE13} m2_repo/repository/JPP/maven2/default_poms/JPP.maven2-empty-dep.pom
cp -p %{SOURCE14} m2_repo/repository/JPP/maven2/empty-dep.jar

%build

# Wire in jdom dependency
cp -p maven2/maven-artifact/pom.xml maven2/maven-artifact/pom.xml.withoutjdom
saxon -o maven2/maven-artifact/pom.xml maven2/maven-artifact/pom.xml.withoutjdom /usr/share/java-utils/xml/maven2jpp-mapdeps.xsl map=%{SOURCE12}

cp -p maven2/bootstrap/bootstrap-installer/pom.xml maven2/bootstrap/bootstrap-installer/pom.xml.withoutjdom
saxon -o maven2/bootstrap/bootstrap-installer/pom.xml maven2/bootstrap/bootstrap-installer/pom.xml.withoutjdom /usr/share/java-utils/xml/maven2jpp-mapdeps.xsl map=%{SOURCE12}

# Build maven2
export MAVEN_REPO_LOCAL=`pwd`/%{repo_dir}
export M2_SETTINGS_FILE=%{maven_settings_file}

# In bootstrap mode, we want it looking at default poms only (controlled via 
# maven2-common-poms). This enables us to change naming structures without 
# breaking build.

export MAVEN_OPTS="-Dmaven.repo.local=$MAVEN_REPO_LOCAL -Dmaven2.ignore.versions -Dmaven2.offline.mode -Dmaven.test.failure.ignore=true"
export M2_HOME=`pwd`/maven2/home/%{base_name}-%{version}

# pushd maven2/ ...
pushd %{name} >& /dev/null

export JAVA_HOME=%{_jvmdir}/java-icedtea

mkdir bootstrap/lib
ln -s $(build-classpath jdom) bootstrap/lib/jdom.jar
export CLASSPATH=`pwd`/bootstrap/lib/jdom.jar
export JDOMCLASS=$CLASSPATH
./bootstrap.sh --prefix=`pwd`/home  --settings=%{maven_settings_file}
unset CLASSPATH

popd >& /dev/null

# Update the classworlds jar name in the mvn script
sed -i -e s:"/core/boot/classworlds-\*.jar":/core/boot/classworlds\*.jar:g $M2_HOME/bin/mvn

# Build plugins
pushd maven2-plugins >& /dev/null

# Build the plugin-plugin first, as it is needed to build itself later on
# NOTE: Build of this plugin for the first time is expected to cause errors. 
# That is why we build it first with -fn . Subsequent builds should not have 
# errors, and if they do, they will be caught when all plugins are built 
# again below. See: http://mail-archives.apache.org/mod_mbox/maven-users/200511.mbox/%3c4374C819.7090609@commonjava.org%3e

(cd maven-plugin-plugin
$M2_HOME/bin/mvn -e --batch-mode -s %{maven_settings_file} $MAVEN_OPTS -npu --no-plugin-registry -fn clean install 
)

%if ! %{NONFREE}
# Disable clover plugin. We don't have a clover package yet.
sed -i -e s:"<module>maven-clover-plugin</module>"::g pom.xml
%endif

# Now build everything
# FIXME: Need to build in two stages to get around gcj bug that causes plugin reload to fail
$M2_HOME/bin/mvn -e --batch-mode -s %{maven_settings_file} $MAVEN_OPTS -npu --no-plugin-registry -fn verify  
$M2_HOME/bin/mvn -e --batch-mode -s %{maven_settings_file} $MAVEN_OPTS -npu --no-plugin-registry --fail-at-end jar:jar install:install 

popd >& /dev/null

# Build complete. Run it tests.

%if %{with_itests}

(cd maven2

# One of the tests (#63) needs tools.jar. Fix the path for it
sed -i -e s:"<systemPath>\${java.home}/../lib/tools.jar</systemPath>":"<systemPath>$JAVA_HOME/lib/tools.jar</systemPath>":g maven-core-it/it0063/pom.xml 

(cd integration-tests/maven-core-it-plugin
$M2_HOME/bin/mvn -s %{maven_settings_file} $MAVEN_OPTS org.apache.maven.plugins:maven-plugin-plugin:2.1.1-SNAPSHOT:descriptor org.apache.maven.plugins:maven-resources-plugin:2.2-SNAPSHOT:resources org.apache.maven.plugins:maven-compiler-plugin:2.1-SNAPSHOT:compile org.apache.maven.plugins:maven-jar-plugin:2.1-SNAPSHOT:jar org.apache.maven.plugins:maven-install-plugin:2.2-SNAPSHOT:install
$M2_HOME/bin/mvn -s %{maven_settings_file} $MAVEN_OPTS org.apache.maven.plugins:maven-install-plugin:2.2-SNAPSHOT:install-file -DgroupId=org.apache.maven.plugins -DartifactId=maven-core-it-plugin -Dversion=2.0.4-JPP -Dpackaging=maven-plugin -Dfile=target/maven-core-it-plugin-1.0-SNAPSHOT.jar
)

for i in `find integration-tests/maven-core-it-support -name pom.xml`; do
    pushd `dirname $i`
        $M2_HOME/bin/mvn -s %{maven_settings_file} $MAVEN_OPTS org.apache.maven.plugins:maven-plugin-plugin:2.1.1-SNAPSHOT::descriptor org.apache.maven.plugins:maven-resources-plugin:2.2-SNAPSHOT:resources org.apache.maven.plugins:maven-compiler-plugin:2.1-SNAPSHOT:compile  org.apache.maven.plugins:maven-jar-plugin:2.1-SNAPSHOT:jar org.apache.maven.plugins:maven-install-plugin:2.2-SNAPSHOT:install
    popd
done

# Test 41 expects core-it-support 1.2 to be packed as a coreit-artifact
(cd integration-tests/maven-core-it-support/1.2
$M2_HOME/bin/mvn -s %{maven_settings_file} $MAVEN_OPTS org.apache.maven.plugins:maven-install-plugin:2.2-SNAPSHOT:install-file -DgroupId=org.apache.maven -DartifactId=maven-core-it-support -Dversion=1.2 -Dpackaging=coreit-artifact -Dfile=target/maven-core-it-support-1.2.jar
)

OLD_MAVEN_OPTS=$MAVEN_OPTS
MAVEN_OPTS="$MAVEN_OPTS -Dmaven.settings.file=$M2_SETTINGS_FILE -Dmaven2.ignore.versions  -Dmaven2.jpp.mode -Dmaven2.jpp.mode=true"
sh -x %{SOURCE9}
export MAVEN_OPTS=$OLD_MAVEN_OPTS
)

%endif

# Build docs
(cd maven2
$M2_HOME/bin/mvn -s %{maven_settings_file} $MAVEN_OPTS org.apache.maven.plugins:maven-javadoc-plugin:2.0-SNAPSHOT:javadoc
)
(cd maven2-plugins
$M2_HOME/bin/mvn -s %{maven_settings_file} $MAVEN_OPTS org.apache.maven.plugins:maven-javadoc-plugin:2.0-SNAPSHOT:javadoc
)

%install
rm -rf $RPM_BUILD_ROOT

# Repository
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/repository

# /usr/bin/mvn
install -dm 755 $RPM_BUILD_ROOT%{_bindir}
install -pm 755 %{SOURCE5} $RPM_BUILD_ROOT%{_bindir}/mvn
install -pm 755 %{SOURCE15} $RPM_BUILD_ROOT%{_bindir}/mvn-jpp

# maven.home
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
cp -p %{name}/home/%{base_name}-%{version}/bin/* $RPM_BUILD_ROOT%{_datadir}/%{name}/bin

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/lib

for library in maven-artifact \
        maven-artifact-manager\
        maven-core \
        maven-error-diagnostics \
        maven-model \
        maven-monitor \
        maven-plugin-api \
        maven-plugin-descriptor \
        maven-plugin-parameter-documenter \
        maven-plugin-registry \
        maven-profile \
        maven-project \
        maven-reporting-api \
        maven-repository-metadata \
        maven-settings; do

            install -pm 644 %{name}/home/%{base_name}-%{version}/lib/$library-%{version}.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/lib
done

# Also, link maven jars from /usr/share/java
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
for library in $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/*-%{version}.jar; do
    ln -s ../../%{name}/lib/`basename $library` $RPM_BUILD_ROOT%{_javadir}/%{name}/`basename $library | sed -e s:^maven-::g`
done

# Some things are not in lib/ by default, and we don't want them there
# either, otherwise the maven classloader loads them and weird things
# happen... but there is no harm in putting in javadir/maven2

for project in maven-archiver maven-artifact-test maven-model-converter; do
    installname=`echo $project | sed -e s:^maven-::g`
    install -pm 644 %{name}/$project/target/$project-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$installname-%{version}.jar
done

install -pm 644 %{name}/maven-embedder/target/maven-embedder-2.0.4-SNAPSHOT.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/embedder-%{version}.jar
install -pm 644 %{name}/maven-reporting/maven-reporting-impl/target/maven-reporting-impl-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/reporting-impl-%{version}.jar
install -pm 644 %{name}/maven-script/maven-script-ant/target/maven-script-ant-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/script-ant-%{version}.jar
install -pm 644 %{name}/maven-script/maven-script-beanshell/target/maven-script-beanshell-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/script-beanshell-%{version}.jar

for i in `find %{name}/maven-plugin-tools -maxdepth 1 -mindepth 1 -type d`; do
    install -pm 644 $i/target/`basename $i`-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/`basename $i | sed -e s:^maven-::g`-%{version}.jar
done

# These items have a version other than 2.0.4.. 
install -pm 644 %{name}/maven-artifact-ant/target/maven-artifact-ant-2.0.4-SNAPSHOT.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/artifact-ant-2.0.4-SNAPSHOT.jar
install -pm 644 %{name}/maven-meeper/target/maven-meeper-0.1-SNAPSHOT.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/meeper-0.1-SNAPSHOT.jar

ln -s artifact-ant-2.0.4-SNAPSHOT.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/artifact-ant.jar
ln -s meeper-0.1-SNAPSHOT.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/meeper.jar

# model-v3
install -pm 644 %{repo_dir}/org/apache/maven/maven-model-v3/2.0/maven-model-v3-2.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/model-v3-2.0.jar
ln -s model-v3-2.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/model-v3.jar
%add_to_maven_depmap org.apache.maven maven-model-v3 2.0 JPP/%{name} model-v3

# Create versionless symlinks
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar | sed  "s|-%{version}||g"`; done)

# For backwards compatibility with older maven2 rpm
ln -s core.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/mavencore.jar

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/core
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/core/boot

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/conf
install -pm 644 %{name}/home/%{base_name}-%{version}/conf/* $RPM_BUILD_ROOT%{_datadir}/%{name}/conf

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/

# plugins
pushd %{repo_dir}/org/apache/maven/plugins
    for plugin in `find -maxdepth 1 -type d -not -name "maven-core-it-plugin" -not -name "maven-it00*-plugin" -not -name "." -not -name ".." | sed -e s:^\./::g`; do
        # Find the latest created version
        latest_ver=`ls -tdF $plugin/* | grep /$ | head -n 1`

        # Proceed only if this plugin has a jar
        if [ -n "`find $latest_ver -type f -name '*.jar'`" ]; then
            cp -p $latest_ver/*jar $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/`echo $plugin | sed -e s:^maven-::g`.jar
        fi
    done
popd

# Install poms
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/poms
pushd %{repo_dir}/org/apache/maven
    for project in maven-archiver \
        maven-artifact \
        maven-artifact-manager \
        maven-artifact-test \
        maven-core \
        maven-embedder \
        maven-error-diagnostics \
        maven-model \
        maven-model-converter \
        maven-monitor \
        maven-plugin-api \
        maven-plugin-descriptor \
        maven-plugin-parameter-documenter \
        maven-plugin-registry \
        maven-plugin-tools \
        maven-plugin-tools-ant \
        maven-plugin-tools-api \
        maven-plugin-tools-beanshell \
        maven-plugin-tools-java \
        maven-plugin-tools-model \
        maven-plugin-tools-pluggy \
        maven-profile \
        maven-project \
        maven-repository-metadata \
        maven-script \
        maven-script-ant \
        maven-script-beanshell \
        maven-settings \
        maven; do 

        artifactname=`echo $project | sed -e s:^maven-::g`
        cp -p $project/%{version}/$project-%{version}.pom $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.%{name}-$artifactname.pom

        # dependency fragments
        %add_to_maven_depmap org.apache.maven $project %{version} JPP/%{name} $artifactname

    done
popd

pushd %{repo_dir}/org/apache/maven/reporting
    for project in maven-reporting \
        maven-reporting-api \
        maven-reporting-impl; do
        
        artifactname=`echo $project | sed -e s:^maven-::g`
        cp -p $project/%{version}/$project-%{version}.pom $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.%{name}-$artifactname.pom
        %add_to_maven_depmap org.apache.maven.reporting $project %{version} JPP/%{name} $artifactname
    done
popd

pushd %{repo_dir}/org/apache/maven/plugins
    for plugin in `find -maxdepth 1 -type d -not -name "maven-core-it-plugin" -not -name "maven-it00*-plugin" -not -name "." -not -name ".." | sed -e s:^\./::g`; do
        # Find the latest created version
        latest_ver=`ls -tdF $plugin/* | grep /$ | head -n 1`

        artifactname=`echo $plugin | sed -e s:^maven-::g`
        latest_ver_num=`basename $latest_ver`
        cp -p $latest_ver/*pom $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.%{name}.plugins-$artifactname.pom
        %add_to_maven_depmap org.apache.maven.plugins $plugin $latest_ver_num JPP/%{name}/plugins $artifactname
    done
popd
# artifact-ant and meeper have versions other than 2.0.4
cp -p %{repo_dir}/org/apache/maven/maven-artifact-ant/2.0.4-SNAPSHOT/*pom $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.maven2-artifact-ant.pom
%add_to_maven_depmap org.apache.maven maven-artifact-ant 2.0.4-SNAPSHOT JPP/%{name} artifact-ant

cp -p %{repo_dir}/org/apache/maven/maven-meeper/0.1-SNAPSHOT/*pom $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.maven2-meeper.pom
%add_to_maven_depmap org.apache.maven maven-meeper 0.1-SNAPSHOT JPP/%{name} meeper

# g=org.apache.maven.plugins a=maven-plugins needs to be copied manually, as 
# it get's changed to a=plugins (a=plugins and a=maven-plugins is the same 
# file, but the former is needed for compatiblity while newer projects use 
# the latter)
cp -p maven2-plugins/pom.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.maven2.plugins-maven-plugins.pom
%add_to_maven_depmap org.apache.maven.plugins maven-plugins 2-SNAPSHOT JPP/%{name}/plugins maven-plugins

# The empty dependencies
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/poms
mkdir -p $RPM_BUILD_ROOT%{_javadir}/%{name}
cp -p %{SOURCE13} $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.maven2-empty-dep.pom
cp -p %{SOURCE14} $RPM_BUILD_ROOT%{_javadir}/%{name}/empty-dep.jar

# For backwards compatibility
ln -s JPP.maven2-core.pom $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.maven2-mavencore.pom

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

(cd maven2
    for doc_dir in `find . -type d -name apidocs`; do 
        targetdir=$RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/`dirname \`dirname $doc_dir\``
        install -dm 755  $targetdir
        cp -pr $doc_dir/* $targetdir
    done
)

(cd maven2-plugins
    for doc_dir in `find . -type d -name apidocs`; do 
        targetdir=$RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/plugins/`dirname \`dirname $doc_dir\``
        install -dm 755 $targetdir
        cp -pr $doc_dir/* $targetdir
    done
)

# manual and jpp readme
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p %{name}/home/%{base_name}-%{version}/*.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p %{SOURCE16} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# create appropriate links in /usr/share/java
ln -sf %{_datadir}/%{name}/poms $RPM_BUILD_ROOT%{_javadir}/%{name}
ln -sf %{_datadir}/%{name}/plugins $RPM_BUILD_ROOT%{_javadir}/%{name}

# Create repository links
ln -s %{_javadir} $RPM_BUILD_ROOT%{_datadir}/%{name}/repository/JPP

# Install bash-completion support
%{__mkdir_p} %{buildroot}%{_sysconfdir}/bash_completion.d
%{__cp} -a %{SOURCE17} %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
build-jar-repository -s -p %{_datadir}/%{name}/core plexus/container-default plexus/utils
build-jar-repository -s -p %{_datadir}/%{name}/core/boot classworlds

build-jar-repository -s -p %{_datadir}/%{name}/lib \
                commons-cli \
                commons-lang \
                commons-logging \
                jdom \
                jsch \
                maven-doxia/sink-api \
                maven-wagon/file \
                maven-wagon/http-lightweight \
                maven-wagon/provider-api \
                maven-wagon/ssh \
                maven-wagon/ssh-external \
                plexus/interactivity-api

%update_maven_depmap

%if %{gcj_support}
%{update_gcjdb}
%endif

# We create links in %post in the dir's below. rm -rf them.
%preun -n %{name}
[ $1 = 0 ] || exit 0
rm -rf %{_datadir}/%{name}/lib/*
rm -rf %{_datadir}/%{name}/core/*

%postun
# FIXME: This doesn't always remove the plugins dir. It seems that rpm doesn't
# honour the Requires(postun) as it should, causing maven to get uninstalled 
# before some plugins are
if [ -d %{_javadir}/%{name} ] ; then rmdir --ignore-fail-on-non-empty %{_javadir}/%{name} >& /dev/null; fi
%update_maven_depmap

%if %{gcj_support}
%{clean_gcjdb}
%endif

%if %{gcj_support}
%post plugin-source
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-source
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{NONFREE}
%if %{gcj_support}
%post plugin-clover
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-clover
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif
%endif

%if %{gcj_support}
%post plugin-ejb
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-ejb
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-repository
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-repository
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-pmd
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-pmd
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-idea
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-idea
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-site
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-site
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-plugin
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-plugin
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-one
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-one
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-eclipse
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-eclipse
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-surefire-report
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-surefire-report
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-release
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-release
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-ear
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-ear
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-project-info-reports
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-project-info-reports
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-antlr
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-antlr
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-clean
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-clean
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-rar
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-rar
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-jar
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-jar
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-checkstyle
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-checkstyle
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-jxr
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-jxr
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-ant
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-ant
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-antrun
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-antrun
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-help
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-help
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-verifier
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-verifier
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-compiler
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-compiler
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-surefire
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-surefire
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-install
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-install
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-javadoc
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-javadoc
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-assembly
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-assembly
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-deploy
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-deploy
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-resources
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-resources
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post plugin-dependency
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun plugin-dependency
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%files -n %{name}
%defattr(-,root,root,-)
%doc %{name}/maven-core/*.txt
%attr(0755,root,root) %{_bindir}/mvn
%attr(0755,root,root) %{_bindir}/mvn-jpp
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/bin
%{_datadir}/%{name}/bin/*.bat
%config(noreplace) %{_datadir}/%{name}/bin/*.conf
%attr(0755,root,root) %{_datadir}/%{name}/bin/m2
%attr(0755,root,root) %{_datadir}/%{name}/bin/mvn
%{_datadir}/%{name}/conf
%{_datadir}/%{name}/core
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/poms
%{_datadir}/%{name}/repository
%dir %{_mavendepmapfragdir}
%config(noreplace) %{_mavendepmapfragdir}/*
%{_javadir}/%{name}
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/plugin-tools-pluggy-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/model-v3-2.0.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/plugin-tools-api-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/plugin-tools-ant-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/reporting-impl-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/plugin-tools-java-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/plugin-tools-model-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/script-ant-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/artifact-ant-2.0.4-SNAPSHOT.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/artifact-test-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/script-beanshell-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/embedder-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/plugin-tools-beanshell-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/model-converter-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/archiver-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/maven-error-diagnostics-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/maven-repository-metadata-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/maven-artifact-manager-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/maven-plugin-parameter-documenter-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/maven-artifact-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/maven-plugin-registry-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/maven-plugin-descriptor-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/maven-settings-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/maven-project-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/maven-profile-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/maven-reporting-api-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/maven-plugin-api-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/maven-core-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/maven-monitor-2.0.4.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/maven-model-2.0.4.jar.*
%endif

%files javadoc
%defattr(-,root,root,-)
%doc %{_javadocdir}/*

%files manual
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}-%{version}

%files plugin-ant
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/ant-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-plugin.jar.*
%endif

%files plugin-antlr
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/antlr-plugin.jar


%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/antlr-plugin.jar.*
%endif

%files plugin-antrun
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/antrun-plugin.jar


%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/antrun-plugin.jar.*
%endif

%files plugin-assembly
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/assembly-plugin.jar


%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/assembly-plugin.jar.*
%endif

%files plugin-checkstyle
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/checkstyle-plugin.jar


%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/checkstyle-plugin.jar.*
%endif

%files plugin-clean
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/clean-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/clean-plugin.jar.*
%endif

%if %{NONFREE}
%files plugin-clover
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/clover-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/clover-plugin.jar.*
%endif
%endif

%files plugin-compiler
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/compiler-plugin.jar


%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/compiler-plugin.jar.*
%endif

%files plugin-dependency
%defattr(-,root,root,-)
%doc maven2-plugins/maven-dependency-plugin/LICENSE.txt
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/dependency-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/dependency-plugin.jar.*
%endif

%files plugin-deploy
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/deploy-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/deploy-plugin.jar.*
%endif


%files plugin-ear
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/ear-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ear-plugin.jar.*
%endif


%files plugin-eclipse
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/eclipse-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/eclipse-plugin.jar.*
%endif


%files plugin-ejb
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/ejb-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ejb-plugin.jar.*
%endif


%files plugin-help
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/help-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/help-plugin.jar.*
%endif


%files plugin-idea
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/idea-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/idea-plugin.jar.*
%endif


%files plugin-install
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/install-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/install-plugin.jar.*
%endif

%files plugin-jar
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/jar-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/jar-plugin.jar.*
%endif


%files plugin-javadoc
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/javadoc-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/javadoc-plugin.jar.*
%endif


%files plugin-jxr
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/jxr-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/jxr-plugin.jar.*
%endif


%files plugin-one
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/one-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/one-plugin.jar.*
%endif


%files plugin-plugin
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/plugin-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/plugin-plugin.jar.*
%endif


%files plugin-pmd
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/pmd-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/pmd-plugin.jar.*
%endif


%files plugin-project-info-reports
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/project-info-reports-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/project-info-reports-plugin.jar.*
%endif


%files plugin-rar
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/rar-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/rar-plugin.jar.*
%endif


%files plugin-release
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/release-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/release-plugin.jar.*
%endif


%files plugin-repository
%defattr(-,root,root,-)
%doc maven2-plugins/maven-repository-plugin/LICENSE.txt
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/repository-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/repository-plugin.jar.*
%endif

%files plugin-resources
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/resources-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/resources-plugin.jar.*
%endif


%files plugin-site
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/site-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/site-plugin.jar.*
%endif


%files plugin-source
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/source-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/source-plugin.jar.*
%endif


%files plugin-surefire
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/surefire-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/surefire-plugin.jar.*
%endif


%files plugin-surefire-report
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/surefire-report-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/surefire-report-plugin.jar.*
%endif


%files plugin-verifier
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/verifier-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/verifier-plugin.jar.*
%endif


%files plugin-war
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/war-plugin.jar

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/war-plugin.jar.*
%endif
