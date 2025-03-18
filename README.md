# ZLA vATIS Profile

**vATIS-Profile-DEV-ZLA.json**: This file is for testing.

**vATIS-Profile-DEV-SCT.json**: This file is for testing.

**vATIS-Profile-ZLA.json**: This is the auto-updating profile for general use. If you import this file to vATIS v4.1.0-beta.1 or newer, it will automatically update.

**vATIS-Profile-ZLA-2.json**: This file is for airports when SBA, L30, and SCT are all already online. Contains IFP, GCN, BFL. Auto-updating.

**vATIS-Profile-[TRACON].json**: Each of these profiles contains more airports for specific TRACONs. Auto-updating.

**vATIS-Profile-ZLA-Static.json**: Archived, legacy static copy. This file will not auto-update in vATIS.

**Download the latest release at (https://github.com/ZLA-ARTCC/vatis-profiles/releases/latest).**

**How to Update**: Make changes to .station files and submit pull requests. Do not edit vATIS profiles except for releaseSerial.

## Compiler and Dev Compilers

Compiler.py combines the stations files and outputs the non-DEV, non-static .json files listed above. 
DevCompiler.py compiles DEV versions of the .json files. 
DO NOT SUBMIT PRs WITH COMPILED .JSON FILES. See above; PR .station files only. 
