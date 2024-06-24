# Changelog

All notable changes to the project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.2] - 06/24/2024

### Added

- Support for Claude 3.5 Sonnet model
- New anthropic_version variable in configuration

### Changed

- Updated default model to Claude 3.5 Sonnet (claude-3-5-sonnet-20240620)
- Renamed version to claude_version in configuration for clarity
- Updated Client class to use new anthropic_version and claude_version variables
- Adjusted headers in Client class to include dynamic anthropic-version from config
- Modified URL construction in Client class to use claude_version instead of version

## [1.0.1] - 03/13/2024

### Added
- Added support for new model: 'Haiku'.

### Changed
- Changed CLI tag for stream mode from `-st` to `-s`.

## [1.0.0] - 03/04/2024

### Added
- Initial release.
