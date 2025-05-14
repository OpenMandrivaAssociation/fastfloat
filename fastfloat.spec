%define _empty_manifest_terminate_build 0
%define major 0
%define devname %mklibname fastfloat -d

Name: fastfloat
Version: 8.0.2
Release: 1
Source0: https://github.com/fastfloat/fast_float/archive/v%{version}/%{name}-%{version}.tar.gz
Summary: Fast and exact version of the C++ from_chars function for float and double types
URL: https://github.com/fastfloat/fast_float
License: Apache-2.0 or Boost or MIT
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildArch: noarch

%description
Fast and exact implementation of the C++ from_chars functions
for float and double types: 4x to 10x faster than strtod

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Fast and exact implementation of the C++ from_chars functions
for float and double types: 4x to 10x faster than strtod

%prep
%autosetup -p1 -n fast_float-%{version}
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{devname}
%{_includedir}/*
%{_datadir}/cmake/*
