from libprobe.probe import Probe
from lib.check.organizations import check_organizations
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'organizations': check_organizations,
    }

    probe = Probe("meraki", version, checks)

    probe.start()
