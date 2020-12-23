%define system_cmake 3.19

Name:           libopencascade
Version:        7.5.0
Release:        1%{?dist}
Summary:        C++ CAD/CAM library

License:        LGPLv2 with exceptions
URL:            https://www.opencascade.com/content/overview
%undefine       _disable_source_fetch
Source0:        https://git.dev.opencascade.org/gitweb/?p=occt.git;a=snapshot;h=refs/tags/V%(echo %{version} | tr . _);sf=tgz#/%{name}-%{version}.tar.gz
%define         SHA256SUM0 c8df7d23051b86064f61299a5f7af30004c115bdb479df471711bab0c7166654

# X10-Update-Spec: { "type": "webscrape", "url": "https://www.opencascade.com/content/latest-release", "pattern": "href=.*?opencascade[._-]v?(\\d+(?:\\.\\d+)+)\\.t"}

BuildRequires:  cmake%{system_cmake}
BuildRequires:  doxygen
BuildRequires:  librapidjson-devel
BuildRequires:  libfreetype-devel

Requires:       libfreetype

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n occt-V%(echo %{version} | tr . _)

%build

mkdir build
cd build

cmake \
    -DINSTALL_DOC_Overview=ON \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} ..

%make_build

%install
cd build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%exclude %{_bindir}
%{_libdir}/libTKBin.*.dylib
%{_libdir}/libTKBinL.*.dylib
%{_libdir}/libTKBinTObj.*.dylib
%{_libdir}/libTKBinXCAF.*.dylib
%{_libdir}/libTKBO.*.dylib
%{_libdir}/libTKBool.*.dylib
%{_libdir}/libTKBRep.*.dylib
%{_libdir}/libTKCAF.*.dylib
%{_libdir}/libTKCDF.*.dylib
%{_libdir}/libTKDCAF.*.dylib
%{_libdir}/libTKDraw.*.dylib
%{_libdir}/libTKernel.*.dylib
%{_libdir}/libTKFeat.*.dylib
%{_libdir}/libTKFillet.*.dylib
%{_libdir}/libTKG2d.*.dylib
%{_libdir}/libTKG3d.*.dylib
%{_libdir}/libTKGeomAlgo.*.dylib
%{_libdir}/libTKGeomBase.*.dylib
%{_libdir}/libTKHLR.*.dylib
%{_libdir}/libTKIGES.*.dylib
%{_libdir}/libTKLCAF.*.dylib
%{_libdir}/libTKMath.*.dylib
%{_libdir}/libTKMesh.*.dylib
%{_libdir}/libTKMeshVS.*.dylib
%{_libdir}/libTKOffset.*.dylib
%{_libdir}/libTKOpenGl.*.dylib
%{_libdir}/libTKPrim.*.dylib
%{_libdir}/libTKQADraw.*.dylib
%{_libdir}/libTKRWMesh.*.dylib
%{_libdir}/libTKService.*.dylib
%{_libdir}/libTKShHealing.*.dylib
%{_libdir}/libTKStd.*.dylib
%{_libdir}/libTKStdL.*.dylib
%{_libdir}/libTKSTEP.*.dylib
%{_libdir}/libTKSTEP209.*.dylib
%{_libdir}/libTKSTEPAttr.*.dylib
%{_libdir}/libTKSTEPBase.*.dylib
%{_libdir}/libTKSTL.*.dylib
%{_libdir}/libTKTObj.*.dylib
%{_libdir}/libTKTObjDRAW.*.dylib
%{_libdir}/libTKTopAlgo.*.dylib
%{_libdir}/libTKTopTest.*.dylib
%{_libdir}/libTKV3d.*.dylib
%{_libdir}/libTKVCAF.*.dylib
%{_libdir}/libTKViewerTest.*.dylib
%{_libdir}/libTKVRML.*.dylib
%{_libdir}/libTKXCAF.*.dylib
%{_libdir}/libTKXDEDRAW.*.dylib
%{_libdir}/libTKXDEIGES.*.dylib
%{_libdir}/libTKXDESTEP.*.dylib
%{_libdir}/libTKXMesh.*.dylib
%{_libdir}/libTKXml.*.dylib
%{_libdir}/libTKXmlL.*.dylib
%{_libdir}/libTKXmlTObj.*.dylib
%{_libdir}/libTKXmlXCAF.*.dylib
%{_libdir}/libTKXSBase.*.dylib
%{_libdir}/libTKXSDRAW.*.dylib
%{_datadir}/opencascade

%files devel
%{_includedir}/opencascade
%{_libdir}/cmake/opencascade
%{_libdir}/libTKBin.dylib
%{_libdir}/libTKBinL.dylib
%{_libdir}/libTKBinTObj.dylib
%{_libdir}/libTKBinXCAF.dylib
%{_libdir}/libTKBO.dylib
%{_libdir}/libTKBool.dylib
%{_libdir}/libTKBRep.dylib
%{_libdir}/libTKCAF.dylib
%{_libdir}/libTKCDF.dylib
%{_libdir}/libTKDCAF.dylib
%{_libdir}/libTKDraw.dylib
%{_libdir}/libTKernel.dylib
%{_libdir}/libTKFeat.dylib
%{_libdir}/libTKFillet.dylib
%{_libdir}/libTKG2d.dylib
%{_libdir}/libTKG3d.dylib
%{_libdir}/libTKGeomAlgo.dylib
%{_libdir}/libTKGeomBase.dylib
%{_libdir}/libTKHLR.dylib
%{_libdir}/libTKIGES.dylib
%{_libdir}/libTKLCAF.dylib
%{_libdir}/libTKMath.dylib
%{_libdir}/libTKMesh.dylib
%{_libdir}/libTKMeshVS.dylib
%{_libdir}/libTKOffset.dylib
%{_libdir}/libTKOpenGl.dylib
%{_libdir}/libTKPrim.dylib
%{_libdir}/libTKQADraw.dylib
%{_libdir}/libTKRWMesh.dylib
%{_libdir}/libTKService.dylib
%{_libdir}/libTKShHealing.dylib
%{_libdir}/libTKStd.dylib
%{_libdir}/libTKStdL.dylib
%{_libdir}/libTKSTEP.dylib
%{_libdir}/libTKSTEP209.dylib
%{_libdir}/libTKSTEPAttr.dylib
%{_libdir}/libTKSTEPBase.dylib
%{_libdir}/libTKSTL.dylib
%{_libdir}/libTKTObj.dylib
%{_libdir}/libTKTObjDRAW.dylib
%{_libdir}/libTKTopAlgo.dylib
%{_libdir}/libTKTopTest.dylib
%{_libdir}/libTKV3d.dylib
%{_libdir}/libTKVCAF.dylib
%{_libdir}/libTKViewerTest.dylib
%{_libdir}/libTKVRML.dylib
%{_libdir}/libTKXCAF.dylib
%{_libdir}/libTKXDEDRAW.dylib
%{_libdir}/libTKXDEIGES.dylib
%{_libdir}/libTKXDESTEP.dylib
%{_libdir}/libTKXMesh.dylib
%{_libdir}/libTKXml.dylib
%{_libdir}/libTKXmlL.dylib
%{_libdir}/libTKXmlTObj.dylib
%{_libdir}/libTKXmlXCAF.dylib
%{_libdir}/libTKXSBase.dylib
%{_libdir}/libTKXSDRAW.dylib
%doc %{_docdir}/opencascade

%changelog
