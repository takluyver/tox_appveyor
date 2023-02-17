**Deprecated**: This plugin doesn't work with tox 4.x. One alternative is
to use ``tox run --discover path\\to\\python.exe`` to specify which Python
to use. If you want to make a new plugin, see `tox's plugin docs
<https://tox.wiki/en/stable/plugins.html>`_.

This is a tiny Tox plugin to allow selecting 32-bit or 64-bit Python
on `AppVeyor <https://www.appveyor.com/>`_ Windows CI builds.

In your ``appveyor.yml`` file, specify the different builds like this:

.. code-block:: yaml

    environment:
      matrix:
        # Python 2.7, 64-bit
        - TOXENV: "py27"
          TOX_APPVEYOR_X64: 1

        # Python 2.7, 32-bit
        - TOXENV: "py27"
          TOX_APPVEYOR_X64: 0

        # Python 3.7, 64-bit
        - TOXENV: "py37"
          TOX_APPVEYOR_X64: 1

        # Python 3.7, 32-bit
        - TOXENV: "py37"
          TOX_APPVEYOR_X64: 0

    build: off

    # For the sections below, the Python version doesn't matter:
    # tox will make an environment based on the environment variables.

    install:
      - "py -3.6 -m pip install wheel tox tox-appveyor"

    test_script:
      - "py -3.6 -m tox"

`Supporting Windows using Appveyor <https://packaging.python.org/guides/supporting-windows-using-appveyor/#testing-with-tox>`_
in the Python Packaging User Guide has more background info about testing Python
projects on Appveyor.
