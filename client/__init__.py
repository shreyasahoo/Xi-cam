import pysftp
import paramiko
from globus import GLOBUSError
from spot import SPOTError
from newt import NEWTError

__all__ = ['newt', 'spot', 'globus', 'sftp']

# Exceptions raised by clients that we care to handle
EXCEPTIONS = (pysftp.ConnectionException, paramiko.ssh_exception.BadAuthenticationType,
              GLOBUSError, SPOTError, GLOBUSError)

