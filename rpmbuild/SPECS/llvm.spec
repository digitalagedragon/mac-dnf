# Heavily cribbed from Homebrew's

%define system_python 3.9

Name:           llvm
Version:        11.0.0
Release:        1%{?dist}
Summary:        Next-gen compiler infrastructure

License:        Apache-2.0 with exceptions
URL:            https://llvm.org/
%undefine       _disable_source_fetch
Source0:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/llvm-project-%{version}.tar.xz
%define         SHA256SUM0 b7b639fc675fa1c86dd6d0bc32267be9eb34451748d2efd03f674b773000e92b

Patch1:         https://github.com/llvm/llvm-project/commit/c86f56e32e724c6018e579bb2bc11e667c96fc96.patch?full_index=1#/llvm-0001-standalone-zlib.patch
Patch2:         https://github.com/llvm/llvm-project/commit/31e5f7120bdd2f76337686d9d169b1c00e6ee69c.patch?full_index=1#/llvm-0002-zlib-from-cmake.patch
#Patch3:         https://github.com/llvm/llvm-project/commit/3c7bfbd6831b2144229734892182d403e46d7baf.patch?full_index=1#/llvm-0003-use-system-ncurses.patch
#Patch4:         https://github.com/llvm/llvm-project/commit/c4d7536136b331bada079b2afbb2bd09ad8296bf.patch?full_index=1#/llvm-0004-use-system-libxml2.patch
Patch5:         https://raw.githubusercontent.com/Homebrew/formula-patches/6166a68c/llvm/openmp_arm.patch#/llvm-0005-openmp-apple-silicon.patch

BuildRequires:  cmake
BuildRequires:  python%{system_python}
BuildRequires:  libffi-devel
BuildRequires:  doxygen

Requires:       libffi
Requires:       libclang%{?_isa} = %{version}-%{release}

%description
Note: macOS provides its own LLVM, so this installs under /usr/local/opt/llvm.

%package -n libclang
Summary:    just libclang.dylib so you don't have to install 15 GB of llvm stuff

%description -n libclang

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n llvm-project-%{version} -p1

%build
mkdir -p llvm/build
cd llvm/build
# this should build LLDB as well but it has problems
# similarly with the libunwind runtime (may be arm64 specific)
CXXFLAGS="-stdlib=libc++" cmake -Wno-dev \
    -DLLVM_ENABLE_PROJECTS='clang;clang-tools-extra;lld;openmp;polly;mlir' \
    -DLLVM_ENABLE_RUNTIMES='compiler-rt;libcxx;libcxxabi' \
    -DLLVM_POLLY_LINK_INTO_TOOLS=ON \
    -DLLVM_BUILD_EXTERNAL_COMPILER_RT=ON \
    -DLLVM_LINK_LLVM_DYLIB=ON \
    -DLLVM_BUILD_LLVM_C_DYLIB=ON \
    -DLLVM_ENABLE_EH=ON \
    -DLLVM_ENABLE_FFI=ON \
    -DLLVM_ENABLE_LIBCXX=ON \
    -DLLVM_ENABLE_RTTI=ON \
    -DLLVM_INCLUDE_DOCS=OFF \
    -DLLVM_INCLUDE_TESTS=OFF \
    -DLLDB_INCLUDE_TESTS=OFF \
    -DLLVM_INSTALL_UTILS=ON \
    -DLLVM_ENABLE_Z3_SOLVER=OFF \
    -DLLVM_OPTIMIZED_TABLEGEN=ON \
    -DLLVM_TARGETS_TO_BUILD=all \
    -DLLVM_CREATE_XCODE_TOOLCHAIN=OFF \
    -DLLDB_USE_SYSTEM_DEBUGSERVER=ON \
    -DLLDB_ENABLE_PYTHON=OFF \
    -DLLDB_ENABLE_LUA=OFF \
    -DLLDB_ENABLE_LZMA=OFF \
    -DLIBOMP_INSTALL_ALIASES=OFF \
    -DCLANG_PYTHON_BINDINGS_VERSIONS=%{system_python} \
    -DCMAKE_INSTALL_PREFIX=%{_prefix}/opt/llvm \
    -G "Unix Makefiles" ..

cmake --build . %{?_smp_mflags}
# TODO figure out why this doesn't build at -j8, it can on linux and this
# runs for literal hours
#%%make_build -j4

%install
cd llvm/build
%make_install

%{__install} -dm755 %{buildroot}%{_bindir}
ln -sv ../opt/llvm/bin/llvm-config %{buildroot}%{_bindir}/llvm-config

%{__install} -dm755 %{buildroot}%{_libdir}
for f in $(ls %{buildroot}%{_prefix}/opt/llvm/lib/*.dylib); do
    mv $f %{buildroot}%{_libdir}/$(basename $f)
    ln -sv ../../../lib/$(basename $f) $f
done

find %{buildroot} -type f | xargs sed -i "" -e '1s:/usr/bin/python:/usr/local/bin/python3:'

%post
echo Note: macOS provides its own LLVM, so LLVM has been installed under /usr/local/opt/llvm.

%files
%{_bindir}/llvm-config
%{_prefix}/opt/llvm

%files -n libclang
%{_libdir}/*.dylib

%changelog
