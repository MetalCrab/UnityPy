from enum import IntFlag


class CompressionFlags(IntFlag):
    NONE = 0
    LZMA = 1
    LZ4 = 2
    LZ4HC = 3
    # LZHAM = 4
    COMPRESSION_4 = 4
    COMPRESSION_5 = 5


class ArchiveFlagsOld(IntFlag):
    CompressionTypeMask = 0x3F
    BlocksAndDirectoryInfoCombined = 0x40
    BlocksInfoAtTheEnd = 0x80
    OldWebPluginCompatibility = 0x100
    UsesAssetBundleEncryption = 0x200


class ArchiveFlags(IntFlag):
    CompressionTypeMask = 0x3F
    BlocksAndDirectoryInfoCombined = 0x40
    BlocksInfoAtTheEnd = 0x80
    OldWebPluginCompatibility = 0x100
    BlockInfoNeedPaddingAtStart = 0x200
    UsesAssetBundleEncryption = 0x1400  # old: 0x400, new: 0x1000
