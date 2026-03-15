# Backlog
## Switch to Poetry for dependency management

## Optimization: Check existing tags / embedded image to see if they even need to be updated
*Single* — read tags before writing and skip files that are already correct

## Producer Support
*Side* — add recording-rels include to `get_release_by_id` call and traverse relationships to extract producer credits

## One File At A Time
*Single* — watcher already handles ZIPs; extend to schedule individual audio files (`.mp3`, `.m4a`, etc.) dropped directly into staging

## Config Arguments

*Don't make me ever edit the config file: let me set config through an argument*

Running `tune-shifter config set paths.staging` lets a user set the staging path, etc.

Running `tune-shifter config show` shows the whole config.

## FLAC Support

*I want FLAC to be as well supported as MP3 and M4A for tagging*

## OGG Support

*I want OGG to be as well supported as MP3 and M4A for tagging*

## Cross-platform service installation (Linux systemd, Windows Task Scheduler)
*Side* — Linux systemd unit file is straightforward; Windows Task Scheduler adds another side; can ship incrementally

## Does Bandcamp auto-download actually work? Test poll_interval_minutes.
*Single* — manual QA task; set a short poll interval and verify downloads trigger correctly

# Needs Refinement
## Best Release
*Side* — when multiple MB results exist, prefer the release closest to the original physical format (LP/CD over digital/streaming)

⚠️ Needs scoping: what ranking heuristic? (release format field, country, date proximity?) and what's the fallback when no physical release exists?

## AcoustID Support
*LP* — fingerprint audio with `fpcalc`/chromaprint, look up recording via AcoustID API, feed MBID into existing tagger

⚠️ Needs scoping: how to handle mismatches between AcoustID result and existing MusicBrainz search? Which takes precedence?

## Nested Folders
*Side* — when a folder-of-folders is dropped into staging, recurse into subdirectories and treat each leaf folder as an album

⚠️ Needs scoping: does each subfolder get its own MusicBrainz lookup? How are mixed-album folders handled?

## Configurable Album Art Search

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

## GUI / menu bar app for sync status

## Allow a user to verify tags before they're written
⚠️ Not scoped — needs UI design (CLI prompt? TUI? GUI?) before estimating
