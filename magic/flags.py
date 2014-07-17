MAGIC_NONE = 0x000000 # No flags
MAGIC_DEBUG = 0x000001 # Turn on debugging
MAGIC_SYMLINK = 0x000002 # Follow symlinks
MAGIC_COMPRESS = 0x000004 # Check inside compressed files
MAGIC_DEVICES = 0x000008 # Look at the contents of devices
MAGIC_MIME_TYPE = 0x000010 # Return the MIME type
MAGIC_CONTINUE = 0x000020 # Return all matches
MAGIC_CHECK = 0x000040 # Print warnings to stderr
MAGIC_PRESERVE_ATIME = 0x000080 # Restore access time on exit
MAGIC_RAW = 0x000100 # Don't translate unprintable chars
MAGIC_ERROR = 0x000200 # Handle ENOENT etc as real errors
MAGIC_MIME_ENCODING = 0x000400 # Return the MIME encoding
MAGIC_MIME = (MAGIC_MIME_TYPE|MAGIC_MIME_ENCODING)
MAGIC_APPLE = 0x000800 # Return the Apple creator and type

MAGIC_NO_CHECK_COMPRESS = 0x001000 # Don't check for compressed files
MAGIC_NO_CHECK_TAR = 0x002000 # Don't check for tar files
MAGIC_NO_CHECK_SOFT = 0x004000 # Don't check magic entries
MAGIC_NO_CHECK_APPTYPE = 0x008000 # Don't check application type
MAGIC_NO_CHECK_ELF = 0x010000 # Don't check for elf details
MAGIC_NO_CHECK_TEXT = 0x020000 # Don't check for text files
MAGIC_NO_CHECK_CDF = 0x040000 # Don't check for cdf files
MAGIC_NO_CHECK_TOKENS = 0x100000 # Don't check tokens
MAGIC_NO_CHECK_ENCODING = 0x200000 # Don't check text encodings

MAGIC_NO_CHECK_FORTRAN = 0x000000 # Don't check ascii/fortran
MAGIC_NO_CHECK_TROFF = 0x000000 # Don't check ascii/troff
