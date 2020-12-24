use strict;
use warnings;

$| = 0;

package Audit;

my %checks;

sub check {
    my $filename = shift;
    print "### Checking: \e[35;1m$filename\e[0m\n";
    my $fh;
    open $fh, $filename;
    my $contents;
    {
        local $/;
        $contents = <$fh>;
    }
    my $parsed = `rpmspec -P $filename`;

    my $all_ok = 1;
    while(my ($name, $class) = each %checks) {
        next if $contents =~ /RPM-Audit-Skip $class/;
        my $rc = $class->can('check')->($filename, $contents, $parsed);
        if($rc < 0) {
            print "\e[1m$name\e[0m: \e[1m-\e[0m\n";
        } elsif($rc) {
            print "\e[1m$name\e[0m: \e[32m✔\e[0m\n";
        } else {
            print "\e[1m$name\e[0m: \e[31m✘\e[0m\n";
            $all_ok = 0;
        }
    }
    return $all_ok;
}

sub register {
    my $name = shift;
    my $class = shift;
    $checks{$name} = $class;
    return 1;
}

1;

package Audit::SHA256Present;

sub check {
    my $filename = shift;
    my $contents = shift;
    my $parsed = shift;

    if($parsed =~ /Source0/) {
        return $parsed =~ /shasum -a256/;
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

    print "\e[1mchecking package dependencies...\e[0m\n";
    my $rc = 1;
    foreach my $rpm (`rpmspec -q --rpms $filename`) {
        chomp $rpm;
        print "  \e[34;1m$rpm.rpm\e[0m:\n";
        $rpm =~ /.*\.(.*)$/;
        my $dirname = dirname $filename;
        foreach my $requirement (`rpm -q --requires $dirname/../RPMS/$1/$rpm.rpm`) {
            chomp $requirement;
            next if $requirement =~ /^rpmlib/;
            print "    $requirement ";
            my $dnf_output = `dnf provides "$requirement" 2>&1`;
            if($dnf_output =~ /No Matches found/m) {
                print " \e[31m✘\e[0m\n";
                $rc = 0;
            } else {
                print " \e[32m✔\e[0m\n";
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

    print "\e[1mchecking package build dependencies...\e[0m\n";
    my $rc = 1;
    foreach my $requirement (`rpmspec -q --buildrequires $filename`) {
        chomp $requirement;
        print "    \e[1m$requirement\e[0m ";
        my $dnf_output = `dnf provides "$requirement" 2>&1`;
        if($dnf_output =~ /No Matches found/m) {
            print " \e[31m✘\e[0m\n";
            $rc = 0;
        } else {
            print " \e[32m✔\e[0m\n";
        }
    }
    return $rc;
}

Audit::register("package build dependencies exist", "Audit::Buildable");

package main;

exit !(Audit::check shift);
