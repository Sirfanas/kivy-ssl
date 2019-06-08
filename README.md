# Simple Kivy App to use any HTTPs request
# author: Sirfanas

Demonstrate Android HTTPS via the `urllib` is achievable thanks to the `SSL_CERT_DIR` environment variable.
See <https://github.com/kivy/python-for-android/issues/1827>.



## Compile:
After pulling docker Buildozer (see https://github.com/kivy/buildozer)
```
docker run --interactive --tty --rm --volume ${pwd}\.buildozer\:/home/user/.buildozer --volume ${pwd}:/home/user/hostcwd --entrypoint /bin/bash kivy/buildozer
```
