from libprobe.probe import Probe
from lib.check.organizations import CheckOrganizations
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = (
        CheckOrganizations,
    )

    probe = Probe("meraki", version, checks)

    probe.start()
