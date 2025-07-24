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


**How to Update**: Make changes to .station files and submit pull requests. Do not edit vATIS profiles except for releaseSerial.

## Compiler and Dev Compilers

Compiler.py combines the stations files and outputs the non-DEV, non-static .json files listed above. 

DevCompiler.py compiles DEV versions of the .json files. 

DO NOT SUBMIT PRs WITH COMPILED .JSON FILES. See above; PR .station files only. 

![GitHub repo size](https://img.shields.io/github/repo-size/ZLA-ARTCC/vatis-profiles?style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors-anon/ZLA-ARTCC/vatis-profiles?style=for-the-badge)
![GitHub commits since latest release](https://img.shields.io/github/commits-since/ZLA-ARTCC/vatis-profiles/latest?style=for-the-badge)
