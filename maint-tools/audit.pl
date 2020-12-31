use strict;
use warnings;

$| = 0;

package Audit;

my %checks;
my $current_file;
my $errors_found;

sub check {
    my $filename = shift;
    my $fh;
    open $fh, $filename;
    my $contents;
    {
        local $/;
        $contents = <$fh>;
    }
    my $parsed = `rpmspec -P $filename`;

    $current_file = $filename;
    $errors_found = 0;
    while(my ($name, $class) = each %checks) {
        next if $contents =~ /RPM-Audit-Skip $class/;
        $class->can('check')->($filename, $contents, $parsed);
    }
    return !$errors_found;
}

sub register {
    my $name = shift;
    my $class = shift;
    $checks{$name} = $class;
    return 1;
}

sub emit_warning {
    my $message = shift;
    print "\e[33m!\e[0m $current_file: $message\n";
}

sub emit_error {
    my $message = shift;
    print "\e[31m✘\e[0m $current_file: $message\n";
    $errors_found = 1;
}

1;

package Audit::SHA256Present;

sub check {
    my $filename = shift;
    my $contents = shift;
    my $parsed = shift;

    if($parsed =~ /Source0/) {
        if(!($parsed =~ /shasum -a256/)) {
            Audit::emit_warning("No Source0 SHA256 check");
        }
    } else {
        return -1;
    }
}

Audit::register("sha256 check present", "Audit::SHA256Present");

package Audit::Installable;

use File::Basename qw(dirname);

sub check {
    my $filename = shift;
    my $contents = shift;
    my $parsed = shift;

    my $rc = 1;
    foreach my $rpm (`rpmspec -q --rpms $filename`) {
        chomp $rpm;
        $rpm =~ /.*\.(.*)$/;
        my $dirname = dirname $filename;
        foreach my $requirement (`rpm -q --requires $dirname/../RPMS/$1/$rpm.rpm`) {
            chomp $requirement;
            next if $requirement =~ /^rpmlib/;
            my $dnf_output = `dnf provides "$requirement" 2>&1`;
            if($dnf_output =~ /No Matches found/m) {
                Audit::emit_error("Run-time requirement '$requirement' is not resolvable");
                $rc = 0;
            }
        }
    }

    return $rc;
}

Audit::register("package dependencies exist", "Audit::Installable");

package Audit::Buildable;

sub check {
    my $filename = shift;
    my $contents = shift;
    my $parsed = shift;

    my $rc = 1;
    foreach my $requirement (`rpmspec -q --buildrequires $filename`) {
        chomp $requirement;
        my $dnf_output = `dnf provides "$requirement" 2>&1`;
        if($dnf_output =~ /No Matches found/m) {
            Audit::emit_error("Build-time requirement '$requirement' is not resolvable");
            $rc = 0;
        }
    }
    return $rc;
}

Audit::register("package build dependencies exist", "Audit::Buildable");

package Audit::PkgConfigNotDevel;

sub check {
    my $filename = shift;
    my $contents = shift;
    my $parsed = shift;

    foreach my $requirement (`rpmspec -q --buildrequires $filename`) {
        chomp $requirement;
        next unless $requirement =~ /-devel/;
        my $dnf_output = `dnf repoquery --provides "$requirement" 2>&1`;
        if($dnf_output =~ /pkgconfig\((\w+)\)/) {
            Audit::emit_warning("$requirement provides pkgconfig($1), use that instead");
        }
    }
}

Audit::register("pkgconfig() is used instead of -devel where possible", "Audit::PkgConfigNotDevel");

package Audit::RedundantDependencies;

use File::Basename qw(dirname);

sub check {
    my $filename = shift;
    my $contents = shift;
    my $parsed = shift;

    my $rc = 1;
    foreach my $rpm (`rpmspec -q --rpms $filename`) {
        chomp $rpm;
        $rpm =~ /.*\.(.*)$/;
        my $dirname = dirname $filename;
        my %seen;
        foreach my $requirement (`rpm -q --requires $dirname/../RPMS/$1/$rpm.rpm`) {
            chomp $requirement;
            next if $requirement =~ /^rpmlib/;
            my $dnf_output = `dnf repoquery --whatprovides "$requirement" 2>/dev/null | grep -v -- '-universal' | tail -n1`;
            chomp $dnf_output;
            # skip things like apple-bsdutils where multiple auto-generated requires may exist
            next if $dnf_output =~ /^apple-/;
            # skip the libfoo%{?_isa} = %{version}-%{release} types on -devel etc
            next if $requirement =~ /^\S+\(aarch-64|x86_64\) = /;
            if(exists $seen{$dnf_output}) {
                # again, avoid some false-positive generated requires
                last if $requirement =~ /\.dylib/ && $seen{$dnf_output} =~ /\.dylib/;
                last if $requirement =~ /^pkgconfig/ && $seen{$dnf_output} =~ /^pkgconfig/;

                Audit::emit_warning("$requirement and $seen{$dnf_output} both resolve to $dnf_output");
            } else {
                $seen{$dnf_output} = $requirement;
            }
        }
    }
}

Audit::register("run-time dependencies are not redundant", "Audit::RedundantDependencies");

package Audit::MacOSBinaryShadowing;

use File::Basename qw(dirname);

sub check {
    my $filename = shift;
    my $contents = shift;
    my $parsed = shift;

    my $rc = 1;
    foreach my $rpm (`rpmspec -q --rpms $filename`) {
        chomp $rpm;
        $rpm =~ /.*\.(.*)$/;
        my $dirname = dirname $filename;
        foreach my $file (`rpm -ql $dirname/../RPMS/$1/$rpm.rpm`) {
            chomp $file;
            next unless $file =~ m|^/usr/local/bin/(.*)$|;
            if(-e "/usr/bin/$1" || -e "/bin/$1") {
                Audit::emit_error("$1 is already provided by macOS");
            }
        }
    }
}

Audit::register("macOS-provided binaries are not shadowed", "Audit::MacOSBinaryShadowing");

package main;

exit !(Audit::check shift);
