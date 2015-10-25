Wrapping a C++ library using Cython in a way that it can be installed and used
transparently by average Python user in an unnecessarily harrowing and novel
experience.

This example hopefully points out (and helps you avoid) some of the more
interesting pitfalls encountered on that path.

In particular this project shows how to wrap C++/C code that present in your
source repository, perhaps you wrote it or perhaps because it is an existing
library that you will copy into your project or include as a git submodule.
It does not show how to wrap a library that a user has installed (say via
brew or apt-get) although some parts may still be applicable.
