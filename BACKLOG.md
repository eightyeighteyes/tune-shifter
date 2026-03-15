## Backlog

### Config Arguments

*Don't make me ever edit the config file: let me set config through an argument*

Running `tune-shifter config set paths.staging` lets a user set the staging path, etc.

Running `tune-shifter config show` shows the whole config.

### One File At A Time

*I only want to copy one file into the staging folder and let tune-shifter process it*

### Nested Folders

*I want to copy a folder of folders into the staging folder and let tune-shifter process all files in all sub-folders*

### Switch to Poetry for dependency management

### Code Coverage

CI runs a code coverage tool.

The application has 95% code coverage in its testing.

### Configurable Album Art Search

*I want to be able to configure where album art is retrieved from*

The default setting should be "default" and retrieve the art from musicbrainz.

*I want to be able to retrieve album art from bandcamp*

The configuration setting for this should be `"bandcamp"`

*I want to be able to retrieve album art from iTunes / Apple Music*

The configuration setting for this should be `"apple"`.

*I want to be able to retrieve album art from Spotify*

The configuration setting for this should be `"spotify"`.

*I want to be able to retrieve album art from Qobuz*

The configuration settings for this should be `"qobuz"`

### Improved Tag Sourcing

*I want ALL the tags from MusicBrainz*

The following is a list of tags that are currently not populated:
  - AcoustID
  - Album Artist Sort Order
  - Artist Sort Order
  - Artists
  - ASIN
  - Barcode
  - Catalog Number
  - Disc Number
  - MusicBrainz Artist ID
  - MusicBrainz Recording ID
  - MusicBrainz Release Artist ID
  - MusicBrainz Release Group ID
  - MusicBrainz Release ID
  - Original Release Date
  - Original Year
  - Producer
  - Record Label
  - Release Country
  - Release Status
  - Release Type
  - Script
  - Total Discs
  - Total Tracks

### Better Cleanup

Fully delete folders from staging after moving files to library.

### GUI / menu bar app for sync status

### Allow a user to verify tags before they're written

### Cross-platform service installation (Linux systemd, Windows Task Scheduler)

### Does Bandcamp auto-download actually work?  Test poll_interval_minutes.



