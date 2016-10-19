Name:           ros-indigo-pcl-1-8
Version:        1.8.0
Release:        0%{?dist}
Summary:        ROS pcl_1_8 package

Group:          Development/Libraries
License:        BSD
URL:            http://www.pointclouds.org
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       eigen3-devel
Requires:       flann
Requires:       flann-devel
Requires:       libusbx-devel
Requires:       python-sphinx
Requires:       qhull-devel
Requires:       ros-indigo-catkin
Requires:       vtk-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  flann-devel
BuildRequires:  libusbx-devel
BuildRequires:  python-sphinx
BuildRequires:  qhull-devel
BuildRequires:  vtk-devel

%description
The Point Cloud Library (or PCL) for point cloud processing - development The
PCL framework contains numerous state-of-the art algorithms including filtering,
feature estimation, surface reconstruction, registration, model fitting and
segmentation.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Oct 19 2016 William Woodall <william@osrfoundation.org> - 1.8.0-0
- Autogenerated by Bloom

