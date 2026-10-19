Contributing
------------

Contributions are welcome. To keep this driver lean and focused, contributions
should be limited to bug fixes, maintenance, and improvements that make the
driver API more convenient to use.

The driver is intended to provide a minimal interface to the sensor. Application-
specific functionality and higher-level features should be implemented in an
application layer rather than added to the driver.


Before submitting a contribution, make sure that:

- All CI pipeline checks pass.
- The code passes the `flake8` checks.
- The code complies with the repository's `.editorconfig` configuration.

Pull requests that introduce new functionality should preserve the scope and
purpose of the driver described above.