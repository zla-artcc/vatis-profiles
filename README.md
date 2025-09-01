# ZLA vATIS Profile

### **Get the [latest release here](https://github.com/ZLA-ARTCC/vatis-profiles/releases/latest)**

![GitHub release (latest by date)](https://img.shields.io/github/v/release/ZLA-ARTCC/vatis-profiles?style=for-the-badge)

## Profile Descriptions

**vATIS-Profile-D-ATIS.json**: Contains only airports that have a real-world Digital ATIS.

**vATIS-Profile-DEV-ZLA.json**: This file is for testing.

**vATIS-Profile-DEV-SCT.json**: This file is for testing.

**vATIS-Profile-[TRACON].json**: Each of these profiles contains more airports for specific TRACONs. Auto-updating.

**vATIS-Profile-ZLA.json**: This is the auto-updating profile for general use. If you import this file to vATIS v4.1.0-beta.1 or newer, it will automatically update.

**vATIS-Profile-ZLA-2.json**: This file is for airports when SBA, L30, and SCT are all already online. Contains IFP, GCN, BFL. Auto-updating.

**vATIS-Profile-ZLA-Static.json**: Archived, legacy static copy. This file will not auto-update in vATIS.


**How to Update**: Make changes to .station files and submit pull requests. Do not edit vATIS profiles directly.

## Compiler and Dev Compilers

Compiler.py combines the stations files and outputs the non-DEV, non-static .json files listed above. It also automatically generates an `updateSerial`.

DevCompiler.py compiles DEV versions of the .json files. 

**Do not submit PRs with compiled .json files. See above; PR .station files only.**

## Releasing

Releases are automatic when station files are changed. The release version depends on your commit message.

### Major versions

If you want to generate a new major version (i.e. increment v1.2.0 to v2.0.0), start your commit message with `feat!:` (note the exclamation point). **This is usually reserved for breaking changes.**

### Minor versions

If you want to generate a new minor version (i.e. increment v1.2.0 to v1.3.0), start your commit message with `feat:`. Most changes should be this type.

### Patch versions

If you want to generate a patch version (i.e. increment v1.2.0 to v1.2.1 instead of v1.3.0), start your commit message with `fix:`. This should be used when fixing a mistake rather than changing functionality.

![GitHub repo size](https://img.shields.io/github/repo-size/ZLA-ARTCC/vatis-profiles?style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors-anon/ZLA-ARTCC/vatis-profiles?style=for-the-badge)
![GitHub commits since latest release](https://img.shields.io/github/commits-since/ZLA-ARTCC/vatis-profiles/latest?style=for-the-badge)
